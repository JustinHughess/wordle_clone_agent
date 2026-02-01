# Load word list once at startup into a set for fast lookups
with open("words.txt") as f:
    VALID_WORDS = set(w.strip().lower() for w in f.readlines())

# Tool definition that tells Claude how to submit a guess
SUBMIT_GUESS_TOOL = {
    "name": "submit_guess",
    "description": "Submit a 5-letter word as your Wordle guess. The system will tell you if it's invalid so you can try again.",
    "input_schema": {
        "type": "object",
        "properties": {
            "word": {
                "type": "string",
                "description": "The 5-letter word to guess"
            }
        },
        "required": ["word"]
    }
}

def validate_word(word):
    """Validate a guess - checks length and that it exists in the word list."""
    word = word.lower().strip()

    if len(word) != 5:
        return False, f"Invalid: '{word}' is {len(word)} letters, must be exactly 5. Try a different word."

    if word not in VALID_WORDS:
        return False, f"Invalid: '{word}' is not in the word list. Try a different common word."

    return True, word