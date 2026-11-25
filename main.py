"""Write the one-line horror entry to entry.txt in the output directory."""
import os

ENTRY = (
    "The grocery app started suggesting meals for two again. "
    "My wife passed in March. Last night it added her allergies back."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
