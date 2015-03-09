import interface
import unittest
import person
import sqlite3
from subprocess import call


class InterfaceTests(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect("test_interface.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("create table test_interface(name, email)")
        self.cursor.execute('''insert into test_interface(name, email)
                                values('my name', 'mymail@abv.bg')''')
        self.i = interface.Interface(self.cursor)

    def test_interface_init(self):
        self.assertEqual("test_interface", self.i.mail_lists[0].list_name)
        self.assertEqual([person.Person("my name", "mymail@abv.bg")],
            self.i.mail_lists[0].people)

    def test_show_lists(self):
        result = self.i.show_lists()
        self.assertEqual("[1] test_interface", result)

    def test_show_list(self):
        result = self.i.show_list(1)
        self.assertEqual("[1] my name - mymail@abv.bg", result)

    def test_show_unexisting_list(self):
        result = self.i.show_list(2)
        self.assertEqual("A list with such an index doesn't exist", result)

    def tearDown(self):
        self.cursor.execute("drop table 'test_interface'")
        self.conn.close()
        call("rm -r test_interface.db", shell=True)


if __name__ == '__main__':
    unittest.main()
