import unittest
class TestApp(unittest.TestCase):
    def test_app(self):
        self.assertEqual(1+2, 3)

if __name__ == '__main__':
    unittest.main()