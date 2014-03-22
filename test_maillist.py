import unittest
import person
import maillist
import json
from subprocess import call


class TestMailList(unittest.TestCase):
    def setUp(self):
        self.test_maillist = maillist.MailList("test_list")

    def test_maillist(self):
        self.assertEqual("test_list", self.test_maillist.list_name)
        self.assertEqual([], self.test_maillist.people)

    def test_to_string_method(self):
        p = person.Person("test personoff", "personoff@test.bug")
        self.test_maillist.add_person(p)
        self.assertEqual("[1] test personoff - personoff@test.bug",
            str(self.test_maillist))

    def test_add_person(self):
        p = person.Person("test personoff", "personoff@test.bug")
        result = self.test_maillist.add_person(p)
        self.assertEqual([p], self.test_maillist.people)
        self.assertTrue(result)

    def test_adding_the_same_person_again(self):
        p = person.Person("test personoff", "personoff@test.bug")
        self.test_maillist.add_person(p)
        result = self.test_maillist.add_person(p)
        self.assertFalse(result)

    def test_remove_person(self):
        p = person.Person("test personoff", "personoff@test.bug")
        self.test_maillist.add_person(p)
        self.test_maillist.remove_person(1)
        self.assertEqual([], self.test_maillist.people)

    def test_has_person_with_email(self):
        p = person.Person("test personoff", "personoff@test.bug")
        self.test_maillist.add_person(p)
        self.assertTrue(self.test_maillist.has_person_with_email("personoff@test.bug"))

    def test_merge_with(self):
        p = person.Person("second testeroff", "testeroff@test.bug")
        test_maillist2 = maillist.MailList("test2")
        test_maillist2.add_person(p)
        self.test_maillist.merge_with(test_maillist2)
        self.assertEqual([p], self.test_maillist.people)

    def test_export_to_json(self):
        p = person.Person("second testeroff", "testeroff@test.bug")
        self.test_maillist.add_person(p)
        result = self.test_maillist.export_to_json()

        self.assertEqual(json.dumps([{"name" : "second testeroff",
                                    "email" : "testeroff@test.bug"}], indent = 4),
            result)

    def test_import_from_json(self):
        json_object = json.dumps([{"name" : "second testeroff",
                                    "email" : "testeroff@test.bug"}], indent = 4)

        self.test_maillist.import_from_json(json_object)
        self.assertEqual([person.Person("second testeroff", "testeroff@test.bug")],
            self.test_maillist.people)


if __name__ == '__main__':
    unittest.main()