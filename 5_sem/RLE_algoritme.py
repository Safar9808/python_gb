# Программа реализует RLE алгоритм для файла text.txt, и записывает результат в файл result.txt

string = open('text.txt').readline()

def rle_encode(string):
    encode = ''
    char = string[0]
    count = 1
    for i in range(1, len(string)):
        if string[i] == char:
            count += 1
        else:
            encode = encode + str(count) + char
            count = 1
            char = string[i]
    encode = encode+str(count)+char
    open('result.txt', 'w').write(encode)


def rle_decode(string):
    letter = string
    digit = string
    for i in '123456789':
        letter = letter.replace(i, ' ')
    for i in 'qwertyuiopasdfghjklzxcvbnm':
        digit = digit.replace(i, ' ')
    letter_list = letter.split()
    digit_list = list(map(int, digit.split()))
    decode = ''
    for i in range(len(digit_list)):
        decode = decode + digit_list[i] * letter_list[i]
    open('result.txt', 'w').write(decode)


rle_decode(string) if string[0] in '123456789' else rle_encode(string) 
