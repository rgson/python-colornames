#!/usr/bin/env python3

import unittest

import colornames


class ColornamesTest(unittest.TestCase):
    def test_find(self):
        colors = [
            # Exact
            ("Amaranth", (229,  43,  80)),
            ("Bamboo"  , (218,  99,   4)),
            ("Camelot" , (137,  52,  86)),
            ("Denim"   , ( 21,  96, 189)),
            ("Elephant", ( 18,  52,  71)),
            # Approximate
            ("Black"   , (  1,   3,   2)),
            ("White"   , (254, 255, 255)),
        ]
        for name, color in colors:
            with self.subTest(name=name, color=color):
                result = colornames.find(color)
                self.assertEqual(result, name)


if __name__ == "__main__":
    unittest.main()
