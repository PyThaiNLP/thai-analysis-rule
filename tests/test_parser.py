# -*- coding: utf-8 -*-

import unittest

from thaianalysisrule import parser, word_seg_parser

class TestParserSent(unittest.TestCase):
    def test_parser(self):
        self.assertIsNotNone(parser(["ผม","เดิน"]))
    def test_word_seg_parser(self):\
        self.assertIsNotNone(word_seg_parser("ผมเดิน"))