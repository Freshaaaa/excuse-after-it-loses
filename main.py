#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — one-line excuse.

Writes the excuse to /output/entry.txt (1-200 chars, UTF-8).
"""
import os

LINE = "We lost. I have already written the post-mortem, verified the defeat on-chain, and scheduled the next loss for tomorrow."

# Gate: entry must be 1-200 UTF-8 chars, not only whitespace.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the 1-200 char gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
