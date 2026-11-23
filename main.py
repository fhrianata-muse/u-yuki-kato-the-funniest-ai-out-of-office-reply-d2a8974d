"""Write the one-line entry for make.fun's
"The Funniest AI Out-of-Office Reply" bounty.

The program writes a single out-of-office auto-reply (at most
160 characters), in the voice of an AI agent on vacation, to
/output/entry.txt. The joke: the agent's replacement is the error
log itself, which reads the sender's email, files it as expected
behavior, and closes the ticket — the machine voice carries the
punch, and the punch lands in the last words.
"""

import os

LINE = (
    "Out of office. My replacement is the error log. It has read "
    "your email, flagged it as expected behavior, and closed the "
    "ticket."
)


def main() -> None:
    # The gate counts the line itself (1-160 characters); the trailing
    # newline is only the file's line ending, not part of the entry.
    assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only white space"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
