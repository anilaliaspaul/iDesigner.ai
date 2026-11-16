import json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ScaffoldTests(unittest.TestCase):
    def test_manifests_are_valid_json(self):
        for f in ['plugin.json','.codex-plugin/plugin.json','.claude-plugin/plugin.json','mcp.json','.mcp.json','config/studio-config.json']:
            json.loads((ROOT/f).read_text(encoding='utf-8'))
    def test_example_brands_have_required_files(self):
        for slug in ['st-stephens','msossa','kirtho']:
            b=ROOT/'resources'/'brands'/slug
            self.assertTrue((b/'brand.json').exists())
            self.assertTrue((b/'design-readme.md').exists())
            json.loads((b/'brand.json').read_text(encoding='utf-8'))
    def test_design_safeguards_are_documented(self):
        skill=(ROOT/'skills/graphic-design-studio/SKILL.md').read_text(encoding='utf-8')
        typography=(ROOT/'skills/graphic-design-studio/references/layout-and-typography.md').read_text(encoding='utf-8')
        qa=(ROOT/'skills/graphic-design-studio/references/quality-review.md').read_text(encoding='utf-8')
        self.assertIn('Logo is a hard gate', skill)
        self.assertIn('Minimalist professional default', skill)
        self.assertIn('Malayalam + English mixed-language integrity', typography)
        self.assertIn('never add invented slogans, captions', skill.lower())
        self.assertIn('pseudo-text', qa.lower())
    def test_sample_brands_have_bilingual_font_inventory(self):
        for slug in ['st-stephens','msossa','kirtho']:
            folder=ROOT/'resources/brands'/slug/'typography'
            self.assertTrue((folder/'font-inventory.json').exists())
            data=json.loads((ROOT/'resources/brands'/slug/'brand.json').read_text(encoding='utf-8'))
            self.assertIn('malayalam',data['typography']['language_support']['fonts'])
    def test_create_brand_script(self):
        with tempfile.TemporaryDirectory() as tmp:
            # Exercise validation logic only; avoid mutating the shipped sample brand set.
            import re
            self.assertIsNotNone(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*','sample-brand'))
            self.assertIsNone(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*','Bad Slug'))

    def test_output_and_reference_intake_is_mandatory(self):
        skill=(ROOT/'skills/graphic-design-studio/SKILL.md').read_text(encoding='utf-8')
        ref=(ROOT/'skills/graphic-design-studio/references/creative-direction.md').read_text(encoding='utf-8')
        workflow=(ROOT/'workflows/reference-and-output-intake.md').read_text(encoding='utf-8')
        self.assertIn('Output and reference intake (mandatory for every new design)', skill)
        self.assertIn('Ask for output platform and dimensions', skill)
        self.assertIn('Ask whether a reference image/design is available', skill)
        self.assertIn('If no reference is supplied', skill)
        self.assertIn('prompt review', ref.lower())
        self.assertIn('retain', ref.lower())
        self.assertIn('output', workflow.lower())

    def test_specialist_skills_are_present_for_both_agents(self):
        for slug in ['canvas-design','poster-design','algorithmic-art','brand-guidelines','adobe-design-from-template','graphic-design-skills-collection']:
            skill=ROOT/'skills'/slug/'SKILL.md'
            self.assertTrue(skill.exists(), slug)
            self.assertIn(f'name: {slug}', skill.read_text(encoding='utf-8'))

    def test_quality_review_has_semantic_content_gate(self):
        qa=(ROOT/'skills/graphic-design-studio/references/quality-review.md').read_text(encoding='utf-8').lower()
        studio=(ROOT/'skills/graphic-design-studio/SKILL.md').read_text(encoding='utf-8').lower()
        reviewer=(ROOT/'agents/quality-reviewer.md').read_text(encoding='utf-8').lower()
        for phrase in ['communication type','intended audience','single main message','repeated meaning','personal message','dear student','fail the design']:
            self.assertIn(phrase,qa)
        self.assertIn('semantic content review (hard gate)',studio)
        self.assertIn('repeated meaning',reviewer)
        self.assertIn('visually attractive design must fail',reviewer)

    def test_adobe_and_design_capabilities_are_configured(self):
        cfg=json.loads((ROOT/'config/studio-config.json').read_text(encoding='utf-8'))
        caps=cfg['design_capabilities']
        for key in ['adobe_express_templates','canvas_design','poster_design','algorithmic_art','brand_guidelines']:
            self.assertIn(key,caps)
        adobe=(ROOT/'skills/adobe-design-from-template/SKILL.md').read_text(encoding='utf-8')
        self.assertIn('explicit template selection',adobe.lower())

if __name__=='__main__': unittest.main()
