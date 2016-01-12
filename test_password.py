# coding: utf-8 
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("abcd"), "abce")

    def test_getNextEndLine(self):
        self.assertEqual(pwd.getNext("abhz"), "abia")

    def test_getNextWrongPwd(self):
        self.assertRaises(ValueError, pwd.getNext, "zzzz")

    def test_getNextNoPwd(self):
        self.assertRaises(ValueError, pwd.getNext, "")

    def test_hasSeries(self):
        self.assertEqual(pwd.hasSeries("aaa"), True)
        self.assertEqual(pwd.hasSeries("aabbcc"), False)

    def test_hasTwoPairs(self):
        self.assertEqual(pwd.hasTwoPairs("abab"), False)
        self.assertEqual(pwd.hasTwoPairs("aabcc"), True)

    def test_hasNoBadCharFalse(self):
        self.assertEqual(pwd.hasNoBadChar("aai"), False)
        self.assertEqual(pwd.hasNoBadChar("aao"), False)
        self.assertEqual(pwd.hasNoBadChar("aal"), False)
        self.assertEqual(pwd.hasNoBadChar("aabcc"), True)

# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()