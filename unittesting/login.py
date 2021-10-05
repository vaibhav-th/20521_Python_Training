import unittest
from check import validate


class Validtest(unittest.TestCase):
    def testval1(self):
        self.assertEqual(validate('Vaibhav', 'Vaibhav@123'), True)

    def testval2(self):
        self.assertEqual(validate(21, 'Vaibhav@123'), False)

    def testval4(self):
        self.assertEqual(validate('vvv', 'V'), False)

    def testval3(self):
        self.assertEqual(validate('VaibhavA', 'Vai12'), False)


    def testval6(self):
        self.assertEqual(validate('Vai', 12345), False)

    def setUp(self):
        print("Setup")


    @classmethod
    def setUpClass(self):
        print("setup class")

    @classmethod
    def tearDownClass(self):
        print("teardown")

    if __name__ == '__main__':
        unittest.main()