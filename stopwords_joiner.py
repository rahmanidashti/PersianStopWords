from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
    PATH = 'stopwords/'
    stopwords_files = [stopword_file for stopword_file in listdir(PATH) if isfile(join(PATH, stopword_file))]

    stopwords_list = []
    stopwords_all = open(join(PATH, 'stopwords_all.txt'), 'w')

    for stopword_file in stopwords_files:
        stopwords = open(join(PATH, stopword_file), 'r', encoding='utf-8').readlines()
        for word in stopwords:
            if word.strip() not in stopwords_list:
                stopwords_list.append(word.strip())
                stopwords_all.write(word.strip() + '\n')
