from approveme import CMSC, NUM_FACULTY
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.cmsc = CMSC()

    def test_num_faculty(self):
        self.cmsc.num_faculty = NUM_FACULTY

    def test_all_unique(self):
        self.cmsc.check_all_unique

    def test_not_ok(self):
        status, ca, da = self.cmsc.check_committee("Lin", "Manocha")
        self.assertFalse(status)

        status, ca, da = self.cmsc.check_committee("Manocha", "Lin")
        self.assertFalse(status)

        status, ca, da = self.cmsc.check_committee("Molloy", "Pop")
        self.assertFalse(status)

    def test_ok(self):
        # Jason Fan, June 2022
        status, ca, da = self.cmsc.check_committee("Patro", "Boyd-Graber")
        self.assertTrue(status)

        # Erica Blum, 2021
        status, ca, da = self.cmsc.check_committee("Katz", "Miers")
        self.assertTrue(status)


if __name__ == "__main__":
    unittest.main()
