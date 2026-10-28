import importlib.util
import json
from pathlib import Path
import unittest
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('generate', ROOT / 'scripts/generate.py')
generate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate)

class GenerationTests(unittest.TestCase):
    def test_equivalent_disjoint_union_only(self):
        source = {'anyOf': [{'type': 'string'}, {'type': 'array', 'items': {'type': 'string'}}]}
        self.assertIn('oneOf', generate.generator_document(source))
        self.assertIn('anyOf', source)  # never mutate canonical contract
        nullable = {'anyOf': [{'type': 'number'}, {'type': 'null'}]}
        self.assertEqual(generate.generator_document(nullable), nullable)
    def test_public_contract_boundary(self):
        doc = json.loads((ROOT / 'spec/openapi.json').read_text())
        self.assertNotIn('userSession', doc['components']['securitySchemes'])
        for path, methods in doc['paths'].items():
            self.assertFalse(path.startswith('/dashboard/'))
            for op in methods.values(): self.assertEqual(op['security'], [{'bearerKey': []}])

if __name__ == '__main__': unittest.main()
