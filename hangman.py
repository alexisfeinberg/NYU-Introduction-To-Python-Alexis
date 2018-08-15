class Hangman():

    def __init__(self, word, guesses=0, guessed_letters=[]):
        self.word = word
        self.guesses = guesses
        self.guessed_letters = guessed_letters
