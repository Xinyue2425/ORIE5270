import unittest
from tree.tree import Tree
from tree.tree import Node


class test_tree(unittest.TestCase):
    def test_empty_tree(self):
        node = None
        self.tree = Tree(node)
        self.answer = "The tree is empty!"
        self.assertEqual(self.tree.print_tree(), self.answer)

    def test_case_1(self):
        node = Node(1, None, None)
        self.tree = Tree(node)
        self.answer = [[1]]
        assert self.tree.print_tree() == self.answer

    def test_case_2(self):
        node = Node(1, Node(2, Node(3, Node(4, None, None), None), None), None)
        self.tree = Tree(node)
        self.answer = [['|', '|', '|', '|', '|', '|', '|', 1, '|', '|', '|', '|', '|', '|', '|'],
                       ['|', '|', '|', 2, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                       ['|', 3, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                       [4, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
        assert self.tree.print_tree() == self.answer

    def test_case_3(self):
        node = Node(1, Node(2, Node(4, None, None), Node(5, None, None)),
                    Node(3, Node(6, None, None), Node(7, None, None)))
        self.tree = Tree(node)
        self.answer = [['|', '|', '|', 1, '|', '|', '|'],
                       ['|', 2, '|', '|', '|', 3, '|'],
                       [4, '|', 5, '|', 6, '|', 7]]
        assert self.tree.print_tree() == self.answer

    def test_case_4(self):
        left_node = Node(2, None, Node(4, None, None))
        right_node = Node(3, Node(5, None, Node(6, None, None)), None)
        node = Node(1, left_node, right_node)
        self.tree = Tree(node)
        self.answer = [['|', '|', '|', '|', '|', '|', '|', 1, '|', '|', '|', '|', '|', '|', '|'],
                       ['|', '|', '|', 2, '|', '|', '|', '|', '|', '|', '|', 3, '|', '|', '|'],
                       ['|', '|', '|', '|', '|', 4, '|', '|', '|', 5, '|', '|', '|', '|', '|'],
                       ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', 6, '|', '|', '|', '|']]
        assert self.tree.print_tree() == self.answer
