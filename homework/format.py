
from pprint import pprint

import json
with open("newsafr.json" , encoding = 'utf8') as datafile:
    json_data = json.load(datafile)

with open("newsafr2.json",  "w" , encoding = 'utf8') as datafile:
    json.dump(json_data["rss"]["channel"]["items"],
    datafile, ensure_ascii=False, indent=2)
    # pprint(json_data)

def length():
    with open("newsafr2.json", encoding = 'utf8') as datafile:
        json_data = json.load(datafile)
        # pprint(json_data)
        news_list = []
        for news in json_data:
            news_split = news["description"].split()
            # pprint(news_list)
            for new in news_split:
                if len(new) > 6:
                    news_list.append(new)
        # pprint(sorted(news_list))
        return sorted(news_list)

# length()

def popular():
    long = length()
    pop_dict = {}
    counter = 1
    for name in long:
        pop_dict[name] = counter
        if name in pop_dict.keys():
            counter += 1
        else:
            counter = 0
    pprint(pop_dict)
    return pop_dict

popular()

# def sorted_key(pop_dict):
#     pop = popular()
#     return pop[name]
#
# pprint(sorted(pop_dict, key = sorted_key))



# import xml.etree.ElementTree as ET
# tree = ET.parse("newsafr.xml" , encoding = 'utf8')
# root = tree.getroot()
# print(root.tag)
# print(root.attrib)
# xml_tetle = root.find("channel/title")
# print(xml_title)
