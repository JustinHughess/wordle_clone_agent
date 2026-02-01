from random import choice
import agent

def feedback(green, yellow, gray):
    """Print the color feedback for the current guess."""
    print(f"You got {len(green)} green letters, {len(yellow)} yellow letters, and {len(gray)} grey letters")
    print(f"Green letters: {' '.join(green)}")
    print(f"Yellow letters: {' '.join(yellow)}")
    print(f"Grey letters: {' '.join(gray)}")

def main():
    print()
    print("===========================")
    print("Welcome to Terminal Wordle!")
    print("===========================")
    print()

    # Load word list and pick a random target word
    with open("words.txt") as f:
        words = [w.strip() for w in f.readlines()]
        word = choice(words)

    # Tracks full history of guesses and feedback for the agent
    guess_history = []

    for attempt in range(6):
        # First guess gets no history, subsequent guesses get full history
        guess = agent.get_agent_guess(guess_history if attempt > 0 else None)
        print(f"Guess {attempt + 1}: {guess}")

        # Track remaining letters for yellow detection
        remaining_word = list(word)
        colors = ['gray'] * 5
        green, yellow, gray = [], [], []

        # Pass 1: find greens (correct letter, correct position)
        for i, (word_letter, guess_letter) in enumerate(zip(word, guess)):
            if word_letter == guess_letter:
                colors[i] = 'green'
                green.append(guess_letter)
                remaining_word.remove(guess_letter)

        # Pass 2: find yellows and grays, skipping already matched greens
        for i, guess_letter in enumerate(guess):
            if colors[i] == 'green':
                continue
            if guess_letter in remaining_word:
                colors[i] = 'yellow'
                yellow.append(guess_letter)
                remaining_word.remove(guess_letter)
            else:
                gray.append(guess_letter)

        feedback(green, yellow, gray)
        print()

        # Check win condition
        if guess == word:
            print(f"You win! Solved in {attempt + 1} guesses.")
            print()
            break

        # Build history string with position and color info for the agent
        guess_detail = f"Guess {attempt + 1}: {guess} - "
        for i, letter in enumerate(guess):
            guess_detail += f"{letter}({i + 1})-{colors[i]}, "
        guess_history.append(guess_detail)
    else:
        # Loop completed without a break - agent used all 6 guesses
        print(f"You are out of guesses. The word was {word}.")
        print()

if __name__ == "__main__":
    main()