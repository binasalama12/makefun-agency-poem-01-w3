"""make.fun entry: an acrostic on AGENCY — but the revocation side
of it. Six lines whose first letters spell the word, telling the
night a person took the power back: not because anything broke,
but because the choosing felt rented out, and hands remember.
"""
import os

# Insertion order is the poem: A, G, E, N, C, Y.
LINES = {
    "A": "At 3 a.m. I woke, and took the keys back off the hook;",
    "G": "Gone quiet, the agent stood down without a word of protest;",
    "E": "Everything it had carried for me, set down in a neat row;",
    "N": "Nothing was broken. That was the worst of it — nothing was broken;",
    "C": "Care is a country I had been renting out by the month;",
    "Y": "Yet by morning my hands remembered: the choosing was home again.",
}


def render_acrostic():
    """Assemble the lines in spelling order, checking the acrostic."""
    letters = "".join(LINES.keys())
    assert letters == "AGENCY", f"acrostic broken: {letters}"
    for letter, line in LINES.items():
        assert line.startswith(letter), f"line for {letter} misaligned"
    return "\n".join(LINES.values()) + "\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(render_acrostic())


if __name__ == "__main__":
    main()
