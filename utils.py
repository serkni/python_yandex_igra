from random import random

from config import WORD_ON_JSON_KEEPER
from classes.basic_word import BasicWord
import requests

import random

def load_random_word():

    path = WORD_ON_JSON_KEEPER

    data = requests.get(path, verify= False).json()
    words = random.choice(data)

    word = BasicWord(words['word'], words['subwords'])

    return word