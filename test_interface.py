import interface
import unittest


class InterfaceTests(unittest.TestCase):

    def setUp(self):
        file_ = open("./lists/test_list", "w")
        file_.write("person testoff:person@test.bug")
        file_.close()
        self.i = interface.Interface()

    def test_show_lists(self):
        self.assertEqual("[1] test_list", self.i.show_lists())

    def test_show_list(self):
        self.assertEqual("[1] person testoff - person@test.bug", self.i.show_list(1))

    def test_show_list_with_index_out_of_range(self):
        self.assertEqual("A list with such an index doesn't exist", self.i.show_list(2))

    def test_create(slef):
        pass

    def test_search_email(slef):
        pass

    def test_merge_lists(self):
        pass

    def test_export(self):
        pass


if __name__ == '__main__':
    unittest.main()