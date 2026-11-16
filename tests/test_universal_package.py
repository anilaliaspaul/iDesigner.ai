import json, re, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class UniversalPackageTests(unittest.TestCase):
    def test_all_manifests_are_valid_json(self):
        for rel in [
            "plugin.json", ".codex-plugin/plugin.json",
            ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json",
            ".cursor-plugin/marketplace.json", "gemini-extension.json",
            ".agents/plugins/marketplace.json", "config/studio-config.json"
        ]:
            with self.subTest(rel=rel):
                json.loads((ROOT / rel).read_text(encoding="utf-8"))

    def test_all_platform_adapters_exist(self):
        paths = [
            "AGENTS.md", "CLAUDE.md", "GEMINI.md",
            ".cursor/rules/idesigner-ai.mdc",
            ".agents/skills/graphic-design-studio/SKILL.md",
            ".muse-plugin/README.md", "skills/graphic-design-studio/SKILL.md"
        ]
        for rel in paths:
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_canonical_and_muse_mirror_skills_match(self):
        canonical = ROOT / "skills"
        mirror = ROOT / ".agents/skills"
        names = {p.name for p in canonical.iterdir() if p.is_dir() and (p/"SKILL.md").exists()}
        mirrored = {p.name for p in mirror.iterdir() if p.is_dir() and (p/"SKILL.md").exists()}
        self.assertEqual(names, mirrored)
        for name in names:
            self.assertEqual((canonical/name/"SKILL.md").read_bytes(),
                             (mirror/name/"SKILL.md").read_bytes(), name)

    def test_manifests_share_version(self):
        versions = [
            (lambda data: data.get("version") or data.get("metadata", {}).get("version"))(json.loads((ROOT / p).read_text()))
            for p in ["plugin.json", ".codex-plugin/plugin.json",
                      ".claude-plugin/plugin.json", ".cursor-plugin/marketplace.json",
                      "gemini-extension.json"]
        ]
        self.assertEqual(len(set(versions)), 1)

    def test_brand_kit_is_retained(self):
        brand = ROOT / "resources/brands/ststephen"
        self.assertTrue((brand/"brand-kit.json").exists())
        self.assertTrue((brand/"St-Stephen-Brand-Guide.pdf").exists())
        self.assertTrue((brand/"01-Logos/st-stephen-logo.png").exists())

    def test_all_skills_have_valid_frontmatter(self):
        for skill in (ROOT/"skills").glob("*/SKILL.md"):
            body = skill.read_text(encoding="utf-8")
            self.assertTrue(body.startswith("---\n"), skill)
            match = re.search(r"^name:\s*([a-z0-9-]+)$", body, re.M)
            self.assertIsNotNone(match, skill)

if __name__ == "__main__":
    unittest.main()
