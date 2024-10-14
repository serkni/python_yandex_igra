
from utils import load_random_word
from classes.player import Player


def main():
    main_word = load_random_word()
    word = main_word.word
    word_count = main_word.count_subwords()

    name = input('Введите ваше имя: ')
    player = Player(name)
    print(player)

    print(f"Составьте из слова {word.upper()} {word_count} слов")
    print("Чтобы закончить игру, напишите 'stop'")

    answer = input("Напишите ваше первое слово: ")

    while player.count_words() != word_count and answer != 'stop':
        if len(answer) >= 3:

            if player.has_uses(answer):
                print("Это слово уже было")

            else:

                if main_word.has_subword(answer):
                    print("Вы угадали слово")
                    player.add_word(answer)

                else:
                    print("Неверное слово")
        else:
            print("Короткое слово")
        answer = input("Введите слово ")

    print(f"Игра завершена, вы отгадали {player.count_words()} слов")


main()