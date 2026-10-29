import copy
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('prepare_release', Path(__file__).parents[1] / 'scripts/prepare-release.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)

class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.old = {'info': {'version': '0.1.0'}, 'paths': {'/emails': {}}}
    def test_noop_does_not_release(self):
        self.assertFalse(release.decide(self.old, copy.deepcopy(self.old), '0.1.0'))
    def test_changed_contract_requires_bump(self):
        new = copy.deepcopy(self.old); new['paths']['/inboxes'] = {}
        with self.assertRaisesRegex(ValueError, 'without a version bump'):
            release.decide(self.old, new, '0.1.0')
    def test_new_version_releases(self):
        new = copy.deepcopy(self.old); new['info']['version'] = '0.2.0'
        self.assertTrue(release.decide(self.old, new, '0.1.0'))
    def test_rollback_does_not_publish_old_code(self):
        with self.assertRaisesRegex(ValueError, 'older'):
            release.decide(self.old, self.old, '0.2.0')
    def test_rejects_prereleases_and_invalid_version(self):
        for value in ['1.2.3-rc.1', '01.2.3', 'v1.2.3', '1.2', '1.2.3; echo oops']:
            with self.assertRaises(ValueError): release.semver(value)
