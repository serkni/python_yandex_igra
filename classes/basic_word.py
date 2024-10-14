class BasicWord:

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def has_subword(self, canditate):
        return canditate.lower() in self.subwords

    def count_subwords(self):
        return len(self.subwords)

    def __repr__(self):
        return f"{self.word} содержит {len(self.subwords)} слов"

