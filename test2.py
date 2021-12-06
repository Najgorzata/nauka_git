
import unittest
import fun
class TestMyFunc(unittest.TestCase):
    def test_ma_kota(self):
        self.assertEqual(fun.ma_kota("Ala"), "Ala ma kota.")


if __name__ == "__main__":
    unittest.main()

