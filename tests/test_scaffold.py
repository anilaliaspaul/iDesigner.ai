import json, re, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ScaffoldTests(unittest.TestCase):
    def test_manifests_are_valid_json(self):
        for rel in [
            "plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json",
            ".claude-plugin/marketplace.json", ".cursor-plugin/marketplace.json",
            "gemini-extension.json", "config/studio-config.json"
        ]:
            with self.subTest(rel=rel):
                json.loads((ROOT / rel).read_text(encoding="utf-8"))

    def test_repository_contains_only_generic_brand_template(self):
        brands = ROOT / "resources" / "brands"
        folders = {p.name for p in brands.iterdir() if p.is_dir()}
        self.assertEqual(folders, {"_template"})
        template = json.loads((brands / "_template" / "brand.json").read_text(encoding="utf-8"))
        self.assertEqual(template["status"], "proposed")
        self.assertIsNone(template["logo_assets"]["primary"])
        self.assertTrue(template["logo_rules"]["logo_optional"])

    def test_brand_first_wizard_searches_before_creating(self):
        wizard = (ROOT / "skills/graphic-design-studio/references/design-wizard.md").read_text(encoding="utf-8").lower()
        self.assertIn("search for the brand", wizard)
        self.assertIn("no saved brand kit was found", wizard)
        self.assertIn("ask permission", wizard)
        self.assertIn("if there is no website", wizard)
        self.assertIn("reload brand context", wizard)

    def test_reference_path_collects_objects_and_exact_assets(self):
        wizard = (ROOT / "skills/graphic-design-studio/references/design-wizard.md").read_text(encoding="utf-8").lower()
        self.assertIn("identify every visible meaningful object", wizard)
        self.assertIn("upload the exact image", wizard)
        self.assertIn("suggest 2–3 suitable alternatives", wizard)
        self.assertIn("typography", wizard)

    def test_no_reference_path_uses_research_and_ten_to_three(self):
        wizard = (ROOT / "skills/graphic-design-studio/references/design-wizard.md").read_text(encoding="utf-8").lower()
        self.assertIn("research the broader visual landscape", wizard)
        self.assertIn("ten genuinely distinct creative concepts", wizard)
        self.assertIn("best three", wizard)

    def test_qa_rework_loop_is_mandatory(self):
        wizard = (ROOT / "skills/graphic-design-studio/references/design-wizard.md").read_text(encoding="utf-8").lower()
        self.assertIn("independent senior qa", wizard)
        self.assertIn("if qa is fail", wizard)
        self.assertIn("repeat until qa returns pass", wizard)
        self.assertIn("only after qa pass", wizard)

    def test_design_safeguards_and_typography_are_documented(self):
        skill = (ROOT / "skills/graphic-design-studio/SKILL.md").read_text(encoding="utf-8")
        typography = (ROOT / "skills/layout-typography/SKILL.md").read_text(encoding="utf-8")
        qa = (ROOT / "skills/graphic-design-studio/references/quality-review.md").read_text(encoding="utf-8")
        self.assertIn("A logo is optional", skill)
        self.assertIn("Malayalam", typography)
        self.assertIn("pseudo-text", qa.lower())

    def test_config_enforces_brand_search_and_reference_qa(self):
        config = json.loads((ROOT / "config/studio-config.json").read_text(encoding="utf-8"))
        onboarding = config["brand_onboarding"]
        self.assertTrue(onboarding["search_workspace_registry_before_creation"])
        self.assertTrue(onboarding["require_user_consent_before_creation"])
        self.assertFalse(onboarding["bundled_client_brand"])
        self.assertTrue(onboarding["if_no_website_request_recent_poster"])
        reference = config["reference_workflow"]
        self.assertTrue(reference["classify_every_meaningful_object"])
        self.assertTrue(reference["request_exact_user_assets_for_identity_critical_objects"])
        self.assertEqual(reference["concepts_without_reference"]["generate"], 10)
        self.assertEqual(reference["concepts_without_reference"]["shortlist"], 3)
        quality = config["quality"]
        self.assertTrue(quality["require_mobile_feed_and_thumbnail_readability"])
        self.assertTrue(quality["require_accessibility_and_contrast_review"])
        self.assertTrue(quality["require_independent_rework_until_pass"])

    def test_create_brand_saves_complete_kit_in_active_workspace(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([
                sys.executable, str(ROOT / "scripts/create_brand.py"),
                "--slug", "sample-brand", "--name", "Sample Brand",
                "--workspace", tmp
            ], check=True, capture_output=True, text=True)
            brand = Path(tmp) / "resources/brands/sample-brand"
            self.assertTrue((brand / "brand.json").exists())
            self.assertTrue((brand / "design-readme.md").exists())
            self.assertTrue((brand / "01-Logos").is_dir())
            self.assertTrue((brand / "04-Reference-Design").is_dir())
            self.assertTrue((brand / "05-Photography").is_dir())
            self.assertTrue((brand / "research").is_dir())
            profile = json.loads((brand / "brand.json").read_text(encoding="utf-8"))
            self.assertEqual(profile["name"], "Sample Brand")
            self.assertEqual(profile["status"], "proposed")
            self.assertIsNone(profile["logo_assets"]["primary"])

    def test_create_brand_slug_rules(self):
        valid = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
        self.assertIsNotNone(valid.fullmatch("sample-brand"))
        self.assertIsNone(valid.fullmatch("Bad Brand"))

if __name__ == "__main__":
    unittest.main()
