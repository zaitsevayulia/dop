def Count():
    f = open('file', encoding='utf-8')
    whitespace = 0  # количество пробелов
    signs = 0  # количество знаков препинания в конце предложения
    other = 0  # остальные знаки

    for line in f:
        for chars in line:
            if chars in ' \n':
                whitespace += 1
            elif chars in '.!?':
                signs += 1
            else:
                other += 1
    f.close()

class Counter:
    def __init__(self):
        self.name = 'Счетчик'

    def count_symbols(self):
        f = open(r'C:\Users\zay89\OneDrive\Рабочий стол\cus.txt', encoding='utf-8')
        whitespace = 0
        signs = 0  # количество знаков препинания в конце предложения
        other = 0

        for line in f:
            for chars in line:
                if chars in ' \n':
                    whitespace += 1
                elif chars in '.!?':
                    signs += 1
                else:
                    other += 1
        print('Символов', whitespace + signs + other)
        f.close()

    def count_symbols_wspace(self):
        f = open(r'C:\Users\zay89\OneDrive\Рабочий стол\cus.txt', encoding='utf-8')
        whitespace = 0
        signs = 0  # количество знаков препинания в конце предложения
        other = 0  # остальные знаки

        for line in f:
            for chars in line:
                if chars in ' \n':
                    whitespace += 1
                elif chars in '.!?':
                    signs += 1
                else:
                    other += 1
        print('Символов без пробелов', other + signs)
        f.close()

    def count_words(self):
        f = open(r'C:\Users\zay89\OneDrive\Рабочий стол\cus.txt', encoding='utf-8')
        whitespace = 0
        for line in f:
            for chars in line:
                if chars in ' \n':
                    whitespace += 1
        print('Слов в файле', whitespace + 1)
        f.close()


    def count_sentence(self):
        f = open(r'C:\Users\zay89\OneDrive\Рабочий стол\cus.txt', encoding='utf-8')
        signs = 0
        for line in f:
            for chars in line:
                if chars in '.!?':
                    signs += 1
        print('Предложений', signs)
        f.close()


symbol = Counter()
symbol.count_symbols()

word = Counter()
word.count_words()

symb = Counter()
symb.count_symbols_wspace()

sentence = Counter()
sentence.count_sentence()