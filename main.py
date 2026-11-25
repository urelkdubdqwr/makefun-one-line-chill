# Reads a single chilling sentence from within the script itself and saves it as entry.txt.
# Renders this project's single-sentence scare and saves it as entry.txt.
# The destination folder can be overridden through the MAKEFUN_OUTPUT_DIR env var.
import os

ENTRY = (
    "The grocery app started suggesting meals for two again. "
    "My wife passed in March. Last night it added her allergies back."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    # When no override is supplied we default to /output, since that mount is the
    # conventional drop location for this project's artifact.
    # Create the destination folder if needed, then write the entry into it.
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
