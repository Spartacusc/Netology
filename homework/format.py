from collections import Counter
from pprint import pprint

import json

def length():
    with open("newsafr.json", encoding='utf8') as datafile:
        json_data = json.load(datafile)
        json_data = json_data["rss"]["channel"]["items"]
        # pprint(json_data)
        news_list = []
        for news in json_data:
            news_split = news["description"].split()
            # pprint(news_list)
            for new in news_split:
                if len(new) > 6:
                    news_list.append(new)
        counter = Counter(news_list)
        # pprint(counter)
        return counter

def popular():
    long = length()
    top = long.most_common(10)
    print('Топ 10 самых часто встречающихся слов:')
    for tip in top:
        print('\t', tip[0], '-', tip[1], 'раз')

popular()


import xml.etree.ElementTree as ET

def lenght_xml():
    tree = ET.parse("newsafr.xml")
    root = tree.getroot()
    xml_items = root.findall("channel/item/description")
    news_list = []
    for xmli in xml_items:
        news_split = xmli.text.split()
        for new in news_split:
            if len(new) > 6:
                news_list.append(new)
    counter = Counter(news_list)
    # pprint(counter)
    return counter

# lenght_xml()

def popular_xml():
    long = lenght_xml()
    top = long.most_common(10)
    print('Топ 10 самых часто встречающихся слов:')
    for tip in top:
        print('\t', tip[0], '-', tip[1], 'раз')

popular_xml()

