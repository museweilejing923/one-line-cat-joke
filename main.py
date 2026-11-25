"""Write the entry to /output/entry.txt. No network, no clock, no randomness — same bytes every run."""
import os, string, sys

# One line: a cat joke that lands.
ENTRY_TEXT = "My cat walked across my keyboard during a video call and typed a better status update than I have ever written."
ENTRY_LIMIT = 200

def abort(reason):
    """Write the failure to stderr, then leave with status 1."""
    sys.stderr.write("error: %s\n" % reason)
    raise SystemExit(1)

def validate(text):
    """Run every entry rule in order before any file is touched."""
    cleaned = text.strip()
    if not cleaned:
        abort("entry must not be empty")
    if cleaned.isdigit():
        abort("entry must not be digits only")
    if all(mark in string.punctuation for mark in cleaned):
        abort("entry must not be punctuation only")
    if not any(symbol.isalpha() for symbol in cleaned):
        abort("entry must include at least one letter")
    if len(text) > ENTRY_LIMIT:
        abort("entry is %d characters, above the %d limit" % (len(text), ENTRY_LIMIT))
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as trouble:
        abort("entry is not valid UTF-8: %s" % trouble)

def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
