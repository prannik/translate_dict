def write_dict(original_file, file_with_russian_words, file_with_english_words):
    with open(original_file, 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            line = line.split('\t')
            line_eng = line[0].split(' ; ')
            line_ru = line[1].split(' ; ')
            translate_dict = dict()
            for key in line_ru:
                translate_dict[key] = line_eng
            with open(file_with_english_words, 'a') as eng_file, open(file_with_russian_words, 'a') as ru_file:
                for ru_word in translate_dict:
                    for eng_word in translate_dict[ru_word]:
                        ru_file.write(ru_word + '\n')
                        eng_file.write(eng_word + '\n')


if __name__ == '__main__':
    original_file = 'dict.txt'
    file_with_russian_words = 'ru.txt'
    file_with_english_words = 'eng.txt'
    write_dict(original_file, file_with_russian_words, file_with_english_words)

