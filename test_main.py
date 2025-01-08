import unittest
# Load this project's module explicitly, including when invoked from repository root.
import importlib.util as _import_util
from pathlib import Path as _Path
import sys as _sys
_spec = _import_util.spec_from_file_location(
    "sunil_agents_" + _Path(__file__).parent.name, _Path(__file__).with_name("main.py"))
_main = _import_util.module_from_spec(_spec)
_sys.modules[_spec.name] = _main
_spec.loader.exec_module(_main)
chunk_text = _main.chunk_text

class ChunkTests(unittest.TestCase):
    def test_offsets_exact_and_coverage_complete(self):
        text = "  one\n two   three four five six "
        chunks = chunk_text(text, "s", 3, 1)
        covered = set()
        for c in chunks:
            self.assertEqual(text[c["char_start"]:c["char_end"]], c["text"])
            covered.update(range(c["token_start"], c["token_end"]))
        self.assertEqual(covered, set(range(6)))
        self.assertEqual(chunks[1]["token_start"], 2)
    def test_stable_ids_and_empty(self):
        self.assertEqual(chunk_text("café voice", "s"), chunk_text("café voice", "s"))
        self.assertEqual(chunk_text("   ", "s"), [])
        self.assertNotEqual(chunk_text("voice", "a")[0]["id"], chunk_text("voice", "b")[0]["id"])
    def test_invalid_windows_fail(self):
        for size, overlap in [(0,0),(3,3),(3,-1),(True,0)]:
            with self.assertRaises(ValueError): chunk_text("text", "s", size, overlap)

