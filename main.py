"""make.fun entry: Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation to /output/entry.txt.
Line 1 explains one everyday thing (a queue) to a 10-year-old in a
single vivid sentence built on an analogy.
Line 2 says in one sentence why that analogy works: what it maps
and what it leaves out.

Gate (from RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 400 characters, not only white space.
"""

# The entry text: exactly two lines, each a single sentence.
ENTRY = (
    "A queue is a caterpillar made of people, each person a little segment "
    "shuffling forward one wiggle at a time until the head reaches the counter.\n"
    "The caterpillar fits because a queue really does creep forward in small "
    "steps from the back to the front, but it leaves out that people can step "
    "out, jump in, or grumble, which no caterpillar segment ever does.\n"
)


def verify(text):
    """Enforce the gate from RULES.txt: 1-400 chars, non-blank, two lines."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(text) <= 400:
        raise ValueError("entry must be 1 to 400 characters, got %d" % len(text))
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines, got %d" % len(lines))
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise ValueError("line %d must not be blank" % i)
        if line.rstrip(".").count(".") != 0:
            raise ValueError("line %d must be a single sentence" % i)
    return True


def main():
    verify(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars, 2 lines)" % len(ENTRY))


if __name__ == "__main__":
    main()
