import requests
from pprint import pprint

API_KEY = 'trnsl.1.1.20190210T101020Z.da8831fcfb249567.b6641f9a89686edbea4ceb60c784b9b510a99fa0'
URL = 'https://translate.yandex.net/api/v1/tr.json/translate?id=07b70d9d.5c5ff8d2.55592c23-1-0&srv=tr-text&lang=ru-en&reason=auto'

def translate_it(text, text_translations, lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    with open(text, encoding='utf8') as f:
        for line in f:
            text = line.strip()
            empty_line = f.readline()
    print(text)

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(lang, to_lang),
    }

    response = requests.get(URL, params=params)

    print(response.status_code)
    json_ = response.json()

    with open(text_translations, 'w', encoding='utf8') as f:
        print('Запись в', text_translations)
        f.write(''.join(json_['text']))

    return ''.join(json_['text'])

translate_it('DE.txt', 'DE2.txt', 'de')
# translate_it('ES.txt', 'ES2.txt', 'es')
translate_it('FR.txt', 'FR2.txt', 'fr')

# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'ru', 'de'))


# requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))


