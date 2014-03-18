import unittest
import person


class PersonTests(unittest.TestCase):
    def setUp(self):
        self.p = person.Person("Testov User", "test@emaildomain.com")

    def test_get_name(self):
        self.assertEqual("Testov User", self.p.get_name())

    def test_get_email(self):
        self.assertEqual("test@emaildomain.com", self.p.get_email())

    def test_tostring(self):
        self.assertEqual("Testov User - test@emaildomain.com", print(self.p))

if __name__ == '__main__':
    unittest.main()
