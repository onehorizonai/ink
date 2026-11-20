import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from social_batch import validate_audience_copy, visible_social_copy


class AudienceCopyTests(unittest.TestCase):
    def test_rejects_previous_public_disclaimers(self):
        for text in ['Actual catalog movement, not an injury treatment claim', 'Fictional contract note', 'Uitsnede van het echte werkdocument']:
            with self.assertRaises(ValueError):
                validate_audience_copy([text])

    def test_keeps_useful_instruction_and_private_evidence(self):
        validate_audience_copy(['Keep the heel down.', 'Example: retry the upload.', 'Anatomy: Z-Anatomy, CC BY-SA 4.0.'])
        validate_audience_copy(visible_social_copy({'headline': 'Control the return.', 'visual': {'images': [{'source': 'Actual catalog capture'}]}}))

    def test_rejects_unfinished_public_placeholders(self):
        for text in ['Nog niet bevestigd', 'Lorem ipsum', 'TBD', 'Vul [onderwerp] hier in']:
            with self.assertRaises(ValueError):
                validate_audience_copy([text])
