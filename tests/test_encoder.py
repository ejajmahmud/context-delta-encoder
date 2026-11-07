"""Tests for context-delta-encoder."""
import unittest
from context_delta_encoder.encoder import ContextDeltaEncoder


class TestDeltaEncoder(unittest.TestCase):
    def test_create_and_verify_patch(self):
        v1 = "alpha\nbeta\ngamma\n"
        v2 = "alpha\nbeta_updated\ngamma\n"
        patch = ContextDeltaEncoder.create_patch(v1, v2)
        self.assertNotEqual(patch.base_hash, patch.target_hash)
        self.assertGreater(len(patch.diff_lines), 0)
