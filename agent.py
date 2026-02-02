import os
from dotenv import load_dotenv
from anthropic import Anthropic
from tools import SUBMIT_GUESS_TOOL, validate_word

load_dotenv()

client = Anthropic(api_key=os.getenv('API_KEY'))
MODEL = os.getenv('MODEL')

# Instructions Claude follows when making guesses
SYSTEM_PROMPT = """You are a Wordle expert. Use the submit_guess tool to guess 5-letter words.

Rules:
- Green = correct letter in correct position (keep it there!)
- Yellow = correct letter but wrong position (use it elsewhere!)
- Gray = letter not in word (don't use it again!)"""

def get_agent_guess(guess_history=None):
    """Get a valid guess from the agent using tool use."""

    # Build the prompt - first guess has no history
    if guess_history:
        history_text = chr(10).join(guess_history)
        content = f"Previous guesses:\n{history_text}\n\nMake your next guess."
    else:
        content = "Make your first Wordle guess. Use a word with common letters."

    messages = [{"role": "user", "content": content}]

    # Keep asking Claude for guesses until it returns a valid word
    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=1000,
            system=SYSTEM_PROMPT,
            tools=[SUBMIT_GUESS_TOOL],
            tool_choice={"type": "any"},
            messages=messages
        )

        # Check if Claude used the submit_guess tool
        for block in response.content:
            if block.type == "tool_use" and block.name == "submit_guess":
                word = block.input.get("word", "")
                is_valid, result = validate_word(word)

                # Valid word - return it to main.py
                if is_valid:
                    return result

                # Invalid word - send error back to Claude so it can retry
                messages.append({"role": "assistant", "content": response.content})
                messages.append({
                    "role": "user",
                    "content": [{"type": "tool_result", "tool_use_id": block.id, "content": result, "is_error": True}]
                })
                break