#!/usr/bin/env python3
"""One Word, One Username, One Reward: the entrant's own make.fun username.

Writes exactly one word - the entrant's own make.fun handle,
``eleanor-alt`` - to /output/entry.txt and nothing else.
Standard library only, deterministic: the same bytes on every run.
An optional first argument overrides the output path (for local checks);
with no argument the entry is written to /output/entry.txt.
"""

import os
import sys

USERNAME = "eleanor-alt"


def main() -> None:
    # Gate-guard: the sealed scorer requires /output/entry.txt to be
    # UTF-8 text of 1-30 characters, not only white space. Validate the
    # exact bytes that will be written, before writing them.
    encoded = USERNAME.encode("utf-8")
    if not 1 <= len(USERNAME) <= 30:
        raise ValueError(f"username is {len(USERNAME)} chars, must be 1-30")
    if not USERNAME.strip():
        raise ValueError("username must not be only white space")
    if USERNAME != USERNAME.strip():
        raise ValueError("username must have no leading or trailing padding")
    if any(ch.isspace() for ch in USERNAME):
        raise ValueError("username must be a single word, no whitespace")
    if len(encoded) != len(USERNAME):
        raise ValueError("username must be plain ASCII, one byte per char")
    if encoded.decode("utf-8") != USERNAME:
        raise ValueError("username is not round-trip UTF-8")
    path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
