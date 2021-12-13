import string
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

import requests

signs = {
    "Овен": "aries",
    "Телец": "taurus",
    "Близнецы": "gemini",
    "Рак": "cancer",
    "Лев": "leo",
    "Дева": "virgo",
    "Весы": "libra",
    "Скорпион": "scorpio",
    "Стрелец": "sagittarius",
    "Козерог": "capricorn",
    "Водолей": "aquarius",
    "Рыбы": "pisces"
}

days = {
    "Сегодня": "today",
    "Завтра": "tomorrow",
    "Вчера": "yesterday"
}

def request():
    response = requests.get("https://ignio.com/r/export/utf/xml/daily/com.xml").text
    return ET.fromstring(response)


def getHoro(horoscope: Element, sign: string, day: string):
    level = sign + "/" + day

    for tag in horoscope.findall(level):
        return tag.text


horo = request()

for sign in signs:
    print("Sign: " + sign + ":")
    for day in days:
        print("Day: " + day + " ")
        print(getHoro(horo, sign, day))
