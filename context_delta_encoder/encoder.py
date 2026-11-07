"""Core Context Delta Encoder implementation."""
import difflib
import hashlib
from typing import Dict, Any, List, Optional


class ContextPatch:
    def __init__(self, base_hash: str, target_hash: str, diff_lines: List[str]):
        self.base_hash = base_hash
        self.target_hash = target_hash
        self.diff_lines = diff_lines

    def to_dict(self) -> Dict[str, Any]:
        return {
            "base_hash": self.base_hash,
            "target_hash": self.target_hash,
            "diff_lines": self.diff_lines
        }


class ContextDeltaEncoder:
    @staticmethod
    def _hash(text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]

    @classmethod
    def create_patch(cls, base_text: str, new_text: str) -> ContextPatch:
        base_h = cls._hash(base_text)
        new_h = cls._hash(new_text)

        base_lines = base_text.splitlines(keepends=True)
        new_lines = new_text.splitlines(keepends=True)

        diff = list(difflib.unified_diff(base_lines, new_lines, fromfile="base", tofile="target"))
        return ContextPatch(base_h, new_h, diff)
