# -*- coding: utf-8 -*-

import unittest

from thaianalysisrule import generate_sent

class TestGenerateSent(unittest.TestCase):
    def test_generate_sent(self):
        self.assertIsNotNone(generate_sent())