"""One word, the first that comes to mind, for make.fun."""
import os

OUTPUT_PATH = "/output/entry.txt"

# Petrichor: the smell of rain on dry earth. Surprising, vivid enough to
# call up a whole summer storm in nine letters, with a soft sound that
# rewards a second look -- and no filler word.
WORD = "petrichor"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
