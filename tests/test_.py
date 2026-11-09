import unittest
import sys
import os

from src.password_validator import validate_password

class Test_TragleCalc (unittest.TestCase):
    def test_truelat(self):
        inputpass ="SecurePass1!"
        res =True
        self.assertEqual(validate_password(inputpass), res)

    def test_truerus(self):
        inputpass ="ПарольТест9#"
        res =True
        self.assertEqual(validate_password(inputpass), res)

    def test_len7(self):
        inputpass ="Secur1!"
        res = False
        self.assertEqual(validate_password(inputpass), res)

    def test_len8(self):
        inputpass ="Secure1!"
        res =True
        self.assertEqual(validate_password(inputpass), res)

    def test_len20(self):
        inputpass ="12345678901234567Aa!"
        res = True
        self.assertEqual(validate_password(inputpass), res)

    def test_len21(self):
        inputpass ="123456789012345678Aa!"
        res = False
        self.assertEqual(validate_password(inputpass), res)

    def test_noupper(self):
        inputpass ="securepass1!"
        res = False
        self.assertEqual(validate_password(inputpass), res)

    def test_nolower(self):
        inputpass ="SECUREPASS1!"
        res = False
        self.assertEqual(validate_password(inputpass), res)

    def test_noNUMBER(self):
        inputpass ="SecurePass!!"
        res = False
        self.assertEqual(validate_password(inputpass), res)

    def test_nospec(self):
        inputpass ="SecurePass12"
        res = False
        self.assertEqual(validate_password(inputpass), res)

    def test_anotherspec(self):
        inputpass ="SecurePass1_"
        res =False
        self.assertEqual(validate_password(inputpass), res)




    def test_TyErrint(self):
        inputpass = 12345678
        self.assertRaises(TypeError, validate_password, inputpass)

    def test_TyErrNone(self):
        inputpass = None
        self.assertRaises(TypeError, validate_password, inputpass)

    def test_TyErrlist(self):
        inputpass = ['P', 'a', 's', 's', 'w', 'o', 'r', 'd']
        self.assertRaises(TypeError, validate_password, inputpass)

    def test_ValErrSp1(self):
        inputpass = " SecurePass1!"
        self.assertRaises(ValueError, validate_password, inputpass)

    def test_ValErrSpMid(self):
        inputpass = "Secure Pass1!"
        self.assertRaises(ValueError, validate_password, inputpass)

    def test_ValErrSpEnd(self):
        inputpass = "SecurePass1! "
        self.assertRaises(ValueError, validate_password, inputpass)




if __name__ == "__main__":
  unittest.main()