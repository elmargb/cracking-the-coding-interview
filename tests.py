import unittest
from chapter_01_arrays_strings import problem_1_1_is_unique as p_1_1
from chapter_01_arrays_strings import problem_1_2_are_permuations as p_1_2
from chapter_01_arrays_strings import problem_1_3_URLify as p_1_3
from chapter_01_arrays_strings import problem_1_4_palindrome_permutation as p_1_4
from chapter_01_arrays_strings import problem_1_5_one_away as p_1_5
from chapter_01_arrays_strings import problem_1_6_string_compression as p_1_6
from chapter_01_arrays_strings import problem_1_7_rotate_matrix as p_1_7
from chapter_01_arrays_strings import problem_1_8_set_zero as p_1_8
from chapter_01_arrays_strings import problem_1_9_string_rotation as p_1_9
from chapter_02_linked_lists import LinkedList as ll
from chapter_02_linked_lists import problem_2_3_delete_middle as p_2_3
from chapter_02_linked_lists import problem_2_4_partition as p_2_4
from chapter_02_linked_lists import problem_2_5_sum_lists as p_2_5
from chapter_03_stacks_queues import Stack
from chapter_03_stacks_queues import Queue
from chapter_04_trees_and_graphs import problem_4_1_path_exists as p_4_1
from chapter_05_bit_manipulation import problem_5_0_convert_binary as p_5_0
from chapter_05_bit_manipulation import problem_5_1_insertion as p_5_1


class Tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_problem_1_1(self):
        s1 = "alex"
        s2 = "aalex"
        self.assertTrue(p_1_1.is_unique(s1))
        self.assertFalse(p_1_1.is_unique(s2))

    def test_problem_1_2(self):
        s1 = "alex"
        s2 = "aalex"
        s3 = "xela"
        self.assertFalse(p_1_2.are_permuations(s1, s2))
        self.assertTrue(p_1_2.are_permuations(s1, s3))

    def test_problem_1_3(self):
        # python strings are immutable, so we use a list of chars to do this "in place"
        # Expect 'Mr. John Smith' -> 'Mr.%20John%20Smith'
        self.assertEqual(['M', 'r', '.', '%', '2', '0', 'J', 'o', 'h', 'n', '%', '2', '0', 'S', 'm', 'i', 't', 'h'],
                         p_1_3.URLify(['M', 'r', '.', ' ', 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h']))

    def test_problem_1_4(self):
        # spaces don't matter
        self.assertEqual(True, p_1_4.palindrome_permuation('tact coa'))  # calitalization matters
        self.assertFalse(p_1_4.palindrome_permuation('Tact Coa'))  # capitalization matters
        self.assertFalse(p_1_4.palindrome_permuation('xyz'))

    def test_problem_1_5(self):
        self.assertTrue(p_1_5.one_away('pale', 'ple'))
        self.assertTrue(p_1_5.one_away('pale', 'pale'))
        self.assertTrue(p_1_5.one_away('pale', 'bale'))
        self.assertFalse(p_1_5.one_away('pale', 'bae'))
        self.assertFalse(p_1_5.one_away('alex', 'al'))

    def test_problem_1_6(self):
        self.assertEqual('a2b1c5a3', p_1_6.string_compression('aabcccccaaa'))
        self.assertEqual('alex', p_1_6.string_compression('alex'))  # strings that don't benefit from compression don't get compressed

    def test_problem_1_7(self):
        import numpy as np
        input_4x4 = np.array([[1, 2, 3, 4],
                              [1, 2, 3, 4],
                              [1, 2, 3, 4],
                              [1, 2, 3, 4]])
        input_5x5 = np.array([[1, 2, 3, 4, 5],
                              [1, 2, 3, 4, 5],
                              [1, 2, 3, 4, 5],
                              [1, 2, 3, 4, 5],
                              [1, 2, 3, 4, 5]])
        # assume rotations are clockwise
        output_4x4 = np.array([[1, 1, 1, 1],
                               [2, 2, 2, 2],
                               [3, 3, 3, 3],
                               [4, 4, 4, 4]])
        output_5x5 = np.array([[1, 1, 1, 1, 1],
                               [2, 2, 2, 2, 2],
                               [3, 3, 3, 3, 3],
                               [4, 4, 4, 4, 4],
                               [5, 5, 5, 5, 5]])
        self.assertTrue(np.array_equal(p_1_7.rotate_matrix(input_4x4), output_4x4))
        self.assertTrue(np.array_equal(p_1_7.rotate_matrix(input_5x5), output_5x5))

    def test_problem_1_8(self):
        import numpy as np
        input_4x4 = np.array([[1, 2, 3, 4],
                              [1, 2, 0, 4],
                              [1, 2, 3, 4],
                              [0, 2, 3, 4]])
        input_5x5 = np.array([[0, 2, 3, 4, 5],
                              [1, 2, 0, 4, 5],
                              [1, 2, 3, 4, 5],
                              [1, 2, 3, 4, 0],
                              [1, 2, 3, 4, 5]])
        # assume rotations are clockwise
        output_4x4 = np.array([[0, 2, 0, 4],
                               [0, 0, 0, 0],
                               [0, 2, 0, 4],
                               [0, 0, 0, 0]])
        output_5x5 = np.array([[0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0],
                               [0, 2, 0, 4, 0],
                               [0, 0, 0, 0, 0],
                               [0, 2, 0, 4, 0]])
        self.assertTrue(np.array_equal(p_1_8.set_zero(input_4x4), output_4x4))
        self.assertTrue(np.array_equal(p_1_8.set_zero(input_5x5), output_5x5))

    def test_problem_1_9(self):
        self.assertTrue(p_1_9.string_rotation('waterbottle', 'erbottlewat'))
        self.assertFalse(p_1_9.string_rotation('waterbottlex', 'erbottlewat'))

    def test_stack(self):
        my_stack = Stack.Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        my_stack.push(4)
        test_array = []
        for i in range(4):
            test_array += [my_stack.pop()]
        self.assertEqual(test_array, [4, 3, 2, 1])
        self.assertEqual(my_stack.is_empty(), True)

    def test_queue(self):
        my_q = Queue.Queue()
        my_q.add(1)
        my_q.add(2)
        my_q.add(3)
        my_q.add(4)
        test_array = []
        for i in range(4):
            test_array += [my_q.remove().value]
        self.assertEqual(test_array, [1, 2, 3, 4])
        self.assertTrue(my_q.is_empty())

    def test_problem_2_3(self):
        n1 = ll.Node(1, None)
        n2 = ll.Node(2, n1)
        n10 = ll.Node(10, n2)
        n5 = ll.Node(5, n10)
        string_representation = ''
        head = n5
        p_2_3.delete_middle(n10)
        while head is not None:
            string_representation += str(head.value)
            head = head.next_node
        self.assertEqual(string_representation, '521')

    def test_problem_2_4(self):
        n1 = ll.Node(1, None)
        n2 = ll.Node(2, n1)
        n10 = ll.Node(10, n2)
        n5_1 = ll.Node(5, n10)
        n8 = ll.Node(8, n5_1)
        n5_0 = ll.Node(5, n8)
        n3 = ll.Node(3, n5_0)
        new_head = p_2_4.partition(n3, 5)
        string_representation = ''
        while new_head is not None:
            string_representation += str(new_head.value)
            new_head = new_head.next_node
        self.assertEqual(string_representation, '12358510')

    def test_problem_2_5(self):
        """
        List1: 3 -> 2 -> 4 -> 9 -> NONE
        List2: 1 -> 5 -> 9 -> NONE

         9423
        + 951
        -----
        10374
        """
        # first list
        n14 = ll.Node(9, None)
        n13 = ll.Node(4, n14)
        n12 = ll.Node(2, n13)
        n11 = ll.Node(3, n12)
        # second list
        n23 = ll.Node(9, None)
        n22 = ll.Node(5, n23)
        n21 = ll.Node(1, n22)
        sum_head = p_2_5.sum_lists(n11, n21)
        list_num = ""
        while sum_head is not None:
            list_num = str(sum_head.value) + list_num  # careful to reverse order!
            sum_head = sum_head.next_node
        self.assertEqual(list_num, '10374')

    def test_problem_4_1(self):
        my_graph = p_4_1.Graph()
        p_4_1.reset(my_graph)
        self.assertEqual(p_4_1.path_exists(my_graph, my_graph.get_node(7), my_graph.get_node(5)), True)
        p_4_1.reset(my_graph)
        self.assertEqual(p_4_1.path_exists(my_graph, my_graph.get_node(3), my_graph.get_node(8)), False)
        p_4_1.reset(my_graph)
        self.assertEqual(p_4_1.path_exists(my_graph, my_graph.get_node(1), my_graph.get_node(8)), True)

    def test_problem_5_0(self):
        self.assertEqual(p_5_0.convert_to_base2(122), '1111010')
        self.assertEqual(p_5_0.convert_to_base(255, 10, 16), 'ff')
        self.assertEqual(p_5_0.convert_to_base('11110100', 2, 16), 'f4')

    def test_problem_5_1(self):
        self.assertEqual(p_5_1.insertion('10000000000', '10011', 2, 6), '10001001100')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
