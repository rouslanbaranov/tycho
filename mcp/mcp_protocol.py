"""MCP protocol, validation and stdio transport helpers."""
import json
import sys

from mcp_contract import (
    MAX_MESSAGE_CHARS,
    SNAPSHOT_RE,
)


class ProtocolFailure(Exception):
    def __init__(self, code, message, data=None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.data = data


def error_response(request_id, code, message, data=None):
    error = {"code": code, "message": message}
    if data is not None:
        error["data"] = data
    return {"jsonrpc": "2.0", "id": request_id, "error": error}


def is_int(value):
    return isinstance(value, int) and not isinstance(value, bool)


def require_object(value, name):
    if not isinstance(value, dict):
        raise ProtocolFailure(-32602, name + " must be an object")
    return value


def reject_unknown(args, allowed):
    require_object(args, "arguments")
    unknown = sorted(set(args) - set(allowed))
    if unknown:
        raise ProtocolFailure(
            -32602,
            "Unknown argument(s): " + ", ".join(unknown),
            {"unknown": unknown},
        )


def arg_string(args, name, required=False, maximum=2000):
    value = args.get(name)
    if value is None:
        if required:
            raise ProtocolFailure(-32602, name + " is required")
        return None
    if not isinstance(value, str) or not value.strip():
        raise ProtocolFailure(-32602, name + " must be a non-empty string")
    if len(value) > maximum:
        raise ProtocolFailure(
            -32602, name + " exceeds " + str(maximum) + " characters")
    return value


def arg_int(args, name, default, minimum, maximum):
    value = args.get(name, default)
    if not is_int(value) or value < minimum or value > maximum:
        raise ProtocolFailure(
            -32602,
            name + " must be an integer in " + str(minimum) + ".." +
            str(maximum),
        )
    return value


def arg_bool(args, name, default):
    value = args.get(name, default)
    if not isinstance(value, bool):
        raise ProtocolFailure(-32602, name + " must be boolean")
    return value


def arg_hash(args, name):
    value = args.get(name)
    if value is None:
        return None
    if not isinstance(value, str) or not SNAPSHOT_RE.fullmatch(value):
        raise ProtocolFailure(
            -32602, name + " must be 64 lowercase hexadecimal characters")
    return value


def arg_snapshot(args):
    return arg_hash(args, "snapshot_id")


def serve(server, stdin=None, stdout=None):
    stdin = sys.stdin if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    for line in stdin:
        if not line.strip():
            continue
        if len(line) > MAX_MESSAGE_CHARS:
            response = error_response(
                None, -32700, "Message exceeds the configured size limit")
            stdout.write(json.dumps(response, sort_keys=True) + "\n")
            stdout.flush()
            continue
        try:
            message = json.loads(line)
        except json.JSONDecodeError:
            response = error_response(None, -32700, "Invalid JSON")
            stdout.write(json.dumps(response, sort_keys=True) + "\n")
            stdout.flush()
            continue
        request_id = message.get("id") if isinstance(message, dict) else None
        try:
            if isinstance(message, list):
                raise ProtocolFailure(-32600, "Batch requests are not supported")
            response = server.handle(message)
        except ProtocolFailure as exc:
            response = error_response(
                request_id, exc.code, exc.message, exc.data)
        except Exception:
            response = error_response(
                request_id, -32603, "Internal server error")
        if response is not None:
            stdout.write(json.dumps(
                response, ensure_ascii=False, sort_keys=True) + "\n")
            stdout.flush()
