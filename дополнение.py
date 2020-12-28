def Count():
    f = open(r'C:\Users\zay89\OneDrive\Рабочий стол\cus.txt', encoding='utf-8')
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
        whitespacea = 0
        signsa = 0  # количество знаков препинания в конце предложения
        othera = 0

        for line in f:
            for chars in line:
                if chars in ' \n':
                    whitespacea += 1
                elif chars in '.!?':
                    signsa += 1
                else:
                    othera += 1
        print('Символов', whitespacea + signsa + othera)
        f.close()

    def count_symbols_wspace(self):
        f = open(r'C:\Users\zay89\OneDrive\Рабочий стол\cus.txt', encoding='utf-8')
        whitespaceb = 0
        signsb = 0  # количество знаков препинания в конце предложения
        otherb = 0  # остальные знаки

        for line in f:
            for chars in line:
                if chars in ' \n':
                    whitespaceb += 1
                elif chars in '.!?':
                    signsb += 1
                else:
                    otherb += 1
        print('Символов без пробелов', otherb + signsb)
        f.close()

    def count_words(self):
        f = open(r'C:\Users\zay89\OneDrive\Рабочий стол\cus.txt', encoding='utf-8')
        whitespacec = 0
        for line in f:
            for chars in line:
                if chars in ' \n':
                    whitespacec += 1
        print('Слов в файле', whitespacec + 1)
        f.close()


    def count_sentence(self):
        f = open(r'C:\Users\zay89\OneDrive\Рабочий стол\cus.txt', encoding='utf-8')
        signs4 = 0
        for line in f:
            for chars in line:
                if chars in '.!?':
                    signs4 += 1
        print('Предложений', signs4)
        f.close()


symbol = Counter()
symbol.count_symbols()

word = Counter()
word.count_words()

symb = Counter()
symb.count_symbols_wspace()

sentence = Counter()
sentence.count_sentence()