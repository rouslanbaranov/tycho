"""Shared imports for MCP feature modules.

Feature mixins use this module to avoid duplicating the standard imports,
contract constants, protocol helpers and search dependencies.
"""
import argparse
import hashlib
import json
import os
import re
import sqlite3
import stat
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

import best_search
import mcp_contract
import route_index
import section_search
from mcp_contract import *  # noqa: F401,F403
from mcp_protocol import *  # noqa: F401,F403
from mcp_shared import *  # noqa: F401,F403
