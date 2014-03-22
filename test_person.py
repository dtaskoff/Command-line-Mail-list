import unittest
import person


class PersonTests(unittest.TestCase):
    def setUp(self):
        self.p = person.Person("User Testoff", "test@emaildomain.com")

    def test_person_init(self):
        self.assertEqual("User Testoff", self.p.name)
        self.assertEqual("test@emaildomain.com", self.p.email)

    def test_person_eq(self):
        p2 = person.Person("User Testoff", "test@emaildomain.com")
        self.assertTrue(self.p == p2)

    def test_tostring(self):
        self.assertEqual("User Testoff - test@emaildomain.com", str(self.p))

    def test_get_name(self):
        self.assertEqual("User Testoff", self.p.get_name())

    def test_get_email(self):
        self.assertEqual("test@emaildomain.com", self.p.get_email())


if __name__ == '__main__':
    unittest.main()
