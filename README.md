# Offset-aware overlapping document chunker

> **Disclosed reconstruction prepared on 24 October 2026.** The recorded Git dates are synthetic, not dates of past development. See [HISTORY.md](HISTORY.md).

This is an incomplete stage in a tutorial reconstruction of an already-completed reference implementation. Source, fixtures, tests, command-line behavior and verification are introduced in later stages. Only the final branch tip contains the complete documented package.

## Intended scope of the final example

Splits text into overlapping whitespace-token windows while retaining exact character offsets and deterministic chunk IDs. Offsets refer to the original Unicode string, not UTF-8 bytes. Chunk size is measured in whitespace tokens, not a model tokenizer. No embedding model is used.

All examples are synthetic and educational. This reconstruction does not establish historical employment, deployment, usage, or production benchmarks.
