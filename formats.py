import os
import chardet
import json
import chardet


def parsing():
    folder = os.listdir()
    for file in folder:
        if file.endswith('.json'):
            with open(file, 'rb') as f:
                fl = f.read()
                enc = chardet.detect(fl)
                dec = fl.decode(enc['encoding'])
                news_dict = json.loads(dec)
                words = []
                for post in news_dict['rss']['channel']['items']:
                    words += post['description'].split(' ')
                words.sort(key=lambda val: len(val) >= 6)
                new_words = [word for word in words if len(word)>=6]
                unique_words=sorted(set(new_words), key=lambda val: new_words.count(val), reverse=True)
                print('Файл {} топ 10 слов: '.format(file), unique_words[:10])

parsing()
