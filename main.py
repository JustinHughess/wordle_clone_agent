from random import choice
import agent

def feedback(green, yellow, gray):
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

    with open("words.txt") as f:
        words = [w.strip() for w in f.readlines()]
        word = choice(words)

    guess_history = []

    for attempt in range(6):
        guess = agent.get_agent_guess(guess_history if attempt > 0 else None)
        print(f"Guess {attempt + 1}: {guess}")

        remaining_word = list(word)
        colors = ['gray'] * 5
        green, yellow, gray = [], [], []

        for i, (word_letter, guess_letter) in enumerate(zip(word, guess)):
            if word_letter == guess_letter:
                colors[i] = 'green'
                green.append(guess_letter)
                remaining_word.remove(guess_letter)

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

        if guess == word:
            print(f"You win! Solved in {attempt + 1} guesses.")
            print()
            break

        guess_detail = f"Guess {attempt + 1}: {guess} - "
        for i, letter in enumerate(guess):
            guess_detail += f"{letter}({i + 1})-{colors[i]}, "
        guess_history.append(guess_detail)
    else:
        print(f"You are out of guesses. The word was {word}.")
        print()

if __name__ == "__main__":
    main()
