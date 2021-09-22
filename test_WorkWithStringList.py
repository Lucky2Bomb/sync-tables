from WorkWithStringList import check_one_type_items_in_list, delete_item_in_list, get_list_as_string, get_new_list_with, get_new_list_without_item, glue_two_string_lists
import unittest


class Test_WorkWithStringList(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_new_list_without_item(self):

        self.assertEqual(type(get_new_list_without_item(
            ['a', 'b', 'c', 'd'], 'd')), list)

        self.assertEqual(get_new_list_without_item(
            ['a', 'b', 'c', 'd'], 'd'), ['a', 'b', 'c'])

        # (it should be) call error TypeError('All items in the list must be type of str')
        # self.assertEqual(get_new_list_without_item(
        #     ['a', 'b', 1, 'd'], 'd'), ['a', 'b', 1])

        with self.assertRaises(ValueError):
            self.assertEqual(get_new_list_without_item(
                ['a', 'b', 'c', 'd'], 'e'), ['a', 'b', 'c', 'd'])

            self.assertEqual(get_new_list_without_item(
                ['a', 'b', 'c', 'd'], 1
            ))

    def test_check_one_type_items_in_list(self):

        self.assertIsNone(check_one_type_items_in_list(['a', 'b', 'c']))
        self.assertIsNone(check_one_type_items_in_list([1, 2, 3], int))

        with self.assertRaises(TypeError):
            self.assertEqual(check_one_type_items_in_list(['a', 'b', 1], str))

    def test_get_list_as_string(self):
        self.assertEqual(
            get_list_as_string(['a', 'b', 'c']), 'a, b, c')

        with self.assertRaises(TypeError):
            self.assertEqual(
                get_list_as_string(['a', 'b', 1]), 'a, b, 1')

    def test_get_new_list_with(self):

        self.assertEqual(get_new_list_with(['a', 'b', 'c'], 'r.', ',', True),
                         ['r.a,', 'r.b,', 'r.c']
                         )

        self.assertEqual(get_new_list_with(['a', 'b', 'c'], 'r.', ',', False),
                         ['r.a,', 'r.b,', 'r.c,']
                         )

    def test_glue_two_string_lists(self):

        self.assertEqual(glue_two_string_lists(['a', 'b', 'c'], ['d', 'e', 'f'], ' = '),
                         ['a = d', 'b = e', 'c = f']
                         )


unittest.main()
