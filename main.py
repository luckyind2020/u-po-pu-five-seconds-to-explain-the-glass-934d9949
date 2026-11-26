"""Five seconds to explain the glass — the cat's defence, printed verbatim."""
from pathlib import Path


def load_line() -> str:
    return Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()


def gate_check(line: str) -> str:
    """Enforce the bounty gate: one sentence, 1-200 chars, no padding."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-empty text with no surrounding whitespace")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} chars, over the 200-char gate")
    if line.count(".") > 1:
        raise ValueError("entry must read as a single sentence")
    return line


def main() -> None:
    print(gate_check(load_line()))


if __name__ == "__main__":
    main()
