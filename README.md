# Terminal Wordle

A terminal-based Wordle game where Claude AI plays automatically. Watch as the AI uses strategic reasoning and tool calling to solve the daily puzzle.

## Features

- Classic Wordle gameplay with 6 attempts to guess a 5-letter word
- AI-powered guessing using Anthropic's Claude models
- Color-coded feedback (green, yellow, gray) after each guess
- Word validation against a dictionary of ~15,000 valid words
- Uses Claude's tool-use capability for structured responses

## Prerequisites

- Python 3.8+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- An [Anthropic API key](https://console.anthropic.com/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/terminal-wordle.git
   cd terminal-wordle
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Create a `.env` file with your Anthropic API credentials:
   ```bash
   cp .env.example .env
   ```

   Then edit `.env` and add your API key:
   ```
   API_KEY=your_anthropic_api_key
   MODEL=claude-sonnet-4-20250514
   ```

## Usage

Run the game:
```bash
uv run main.py
```

## Example Output

```
===========================
Welcome to Terminal Wordle!
===========================

Guess 1: crane
You got 1 green letters, 1 yellow letters, and 3 grey letters
Green letters: r
Yellow letters: e
Grey letters: c a n

Guess 2: store
You got 2 green letters, 1 yellow letters, and 2 grey letters
Green letters: r e
Yellow letters: o
Grey letters: s t

Guess 3: froze
You got 5 green letters, 0 yellow letters, and 0 grey letters
Green letters: f r o z e
Yellow letters:
Grey letters:

You win! Solved in 3 guesses.
```

## How It Works

### Game Flow

1. The game selects a random 5-letter word from `words.txt`
2. Claude is prompted to make a guess using the `submit_guess` tool
3. Each guess is validated against the word list
4. Feedback is provided for each letter:
   - **Green**: Correct letter in the correct position
   - **Yellow**: Correct letter in the wrong position
   - **Gray**: Letter is not in the word
5. Claude uses the feedback history to inform subsequent guesses
6. The game ends when Claude guesses correctly or runs out of attempts

### Architecture

| File | Description |
|------|-------------|
| `main.py` | Game loop, word selection, and feedback logic |
| `agent.py` | Claude API integration with tool-use for guessing |
| `tools.py` | Tool definition and word validation |
| `words.txt` | Dictionary of valid 5-letter words |

### AI Strategy

The AI uses Claude's reasoning capabilities to:
- Start with words containing common letters (e.g., "crane", "slate")
- Track which letters are confirmed (green) and must stay in position
- Reposition yellow letters to find their correct spots
- Eliminate gray letters from future guesses

## Configuration

You can change the Claude model in your `.env` file:

| Model | Description |
|-------|-------------|
| `claude-sonnet-4-20250514` | Fast and capable |
| `claude-opus-4-20250514` | Most capable, slower (recommended) |
| `claude-haiku-3-5-20241022` | Fastest, most economical |

## Dependencies

- `anthropic` - Anthropic Python SDK for Claude API
- `python-dotenv` - Environment variable management
