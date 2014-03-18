import unittest
import person
import maillist
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
        self.ml.export_to_json()

        file_.open("test_list.json", "r")
        contents = file_.read()
        file_.close()
        call("rm -r test_list.json", shell = True)

        self.assertEqual("[\n\t{\n\t\t\"second testeroff\" : "\
                + "\"testeroff@test.bug\"\n\t},\n]", contents)


if __name__ == '__main__':
    unittest.main()