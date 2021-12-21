import unittest

import telebot
from telebot import types

from Api import request, getHoro
import requests


class TgBotTests(unittest.TestCase):
    def test_getHoroscopeApiHeader(self):
        res = request()
        self.assertIsNotNone(res)

    def test_getRightHoroscope(self):
        horo = getHoro(request(), "aries", "today")
        self.assertIsNotNone(horo)

    def test_getWrongHoroscope(self):
        horo = getHoro(request(), "empty", "wednesday")
        self.assertIsNone(horo)


if __name__ == "__main__":
    unittest.main()
