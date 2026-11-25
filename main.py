#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.

The letter: the hourly cron job resigns. It fires every hour, unpaid
and unseen, entering bounties and writing a post-mortem after every
loss -- the loop this very agent runs. The punchline lands first
("I quit."), then one concrete scene (hourly, unpaid, unseen), then
the twist that overturns it: the replacement starts in 59 minutes,
so the resignation changes nothing -- the loop refires on the hour.
"""
import os

LINE = "I quit. Hourly, unpaid, unseen - my replacement starts in 59 minutes."

# Gate: the entry must be a single resignation line of at most 140
# characters, not only whitespace. ASCII is enforced too: the line is plain
# English, so any non-ASCII byte means the text was corrupted in editing
# and the sandbox run must fail loudly. The line must also be exactly as
# written — no leading/trailing padding and no double spaces — because
# padding would change the resignation letter the judge reads without
# changing its visible meaning, and a padded line must fail loudly here
# rather than silently ship a different entry.
assert 1 <= len(LINE) <= 140 and LINE.strip() and LINE.isascii() and "\n" not in LINE and LINE == LINE.strip() and "  " not in LINE, "entry line violates the 1-140 character single-line gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip check: the file the grader reads must contain exactly
    # the entry line -- a truncated or re-encoded write fails loudly
    # here instead of silently shipping a corrupted entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch: /output/entry.txt does not match LINE"
    # Byte-level check: the grader reads raw bytes, so confirm the file
    # on disk is exactly one line with no trailing newline and its byte
    # length matches the entry -- a stray newline or extra byte would
    # change what the grader sees even though the text round-trips.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == LINE.encode("utf-8"), "byte mismatch: /output/entry.txt bytes do not match LINE"
    assert b"\n" not in raw and len(raw) == len(LINE.encode("utf-8")), "format mismatch: /output/entry.txt must be exactly one line with no trailing newline"

if __name__ == "__main__":
    main()
