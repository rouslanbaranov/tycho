"""Guard the Vercel deployment-budget policy for issue branches."""

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class VercelDeploymentPolicyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config_path = ROOT / "vercel.json"
        cls.config = json.loads(config_path.read_text(encoding="utf-8"))

    def test_config_uses_the_vercel_schema(self):
        self.assertEqual(
            self.config.get("$schema"),
            "https://openapi.vercel.sh/vercel.json",
        )

    def test_only_main_branch_deploys_automatically(self):
        # Vercel treats an unspecified branch as enabled, and a true match
        # wins over a false match. The explicit deny-all pattern therefore
        # keeps production deployment while stopping every preview branch.
        self.assertEqual(
            self.config.get("git", {}).get("deploymentEnabled"),
            {"main": True, "**": False},
            "automatic Vercel deployments must remain limited to main",
        )
