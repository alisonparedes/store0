import unittest
from store0 import model


class TestCaseLoadModel(unittest.TestCase):
    def test_load(self):
        m = model.load()
        print(m.summary())
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
