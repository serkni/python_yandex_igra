class Player:
    def __init__(self, name):
        self.name = name
        self.usedwords = []

    def count_words(self):
        return len(self.usedwords)

    def add_word(self, word):
        self.usedwords.append(word)

    def has_uses(self, word):
        return word in self.usedwords

    def __repr__(self):
        return  f"Привет {self.name}"