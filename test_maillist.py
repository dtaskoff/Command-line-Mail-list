import unittest
import person
import maillist
import json
from subprocess import call


class TestMailList(unittest.TestCase):
    def setUp(self):
        self.ml = maillist.MailList("test_list")

    def test_maillist(self):
        self.assertEqual("test_list", self.ml.list_name)
        self.assertEqual([], self.ml.people)

    def test_to_string_method(self):
        p = person.Person("test personoff", "personoff@test.bug")
        self.ml.add_person(p)
        self.assertEqual("[1] test personoff - personoff@test.bug\n",
            str(self.ml))

    def test_add_person(self):
        p = person.Person("test personoff", "personoff@test.bug")
        self.ml.add_person(p)
        self.assertEqual([p], self.ml.people)

    def test_remove_person(self):
        p = person.Person("test personoff", "personoff@test.bug")
        self.ml.add_person(p)
        self.ml.remove_person(1)
        self.assertEqual([], self.ml.people)

    def test_has_person_with_mail(self):
        p = person.Person("test personoff", "personoff@test.bug")
        self.ml.add_person(p)
        self.assertTrue(self.ml.has_person_with_mail("personoff@test.bug"))

    def test_merge_with(self):
        p = person.Person("second testeroff", "testeroff@test.bug")
        ml2 = maillist.MailList("test2")
        ml2.add_person(p)
        self.ml.merge_with(ml2)
        self.assertEqual([p], self.ml.people)

    def test_export_to_json(self):
        p = person.Person("second testeroff", "testeroff@test.bug")
        self.ml.add_person(p)
        expected = self.ml.export_to_json()

        self.assertEqual(json.dumps([{"name" : "second testeroff",
                                    "email" : "testeroff@test.bug"}], indent = 4),
            expected)


if __name__ == '__main__':
    unittest.main()