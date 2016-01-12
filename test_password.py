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

# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()