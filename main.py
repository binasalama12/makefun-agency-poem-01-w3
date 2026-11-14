"""make.fun entry: an acrostic on AGENCY — six lines whose first
letters spell the word, each line one clause of the bargain between
a person and the agent who acts for them.
"""
import os

# Insertion order is the poem: A, G, E, N, C, Y.
LINES = {
    "A": "Ask me before you act, and I will tell you where the road bends;",
    "G": "Give me the heavy end of every load I cannot lift alone;",
    "E": "Every order I write in pencil, so tomorrow can revise it;",
    "N": "Nothing you carry for me makes the carrying less mine;",
    "C": "Choose, I say, and the choosing comes back wearing my own voice;",
    "Y": "Yet at the end of the day, the hand that signs is still this hand.",
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
