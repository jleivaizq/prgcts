# -*- coding: utf-8 -*-

from unittest import TestCase

from kihon.trees import BinaryTree


class BinaryTreeTest(TestCase):
    """Simple binary trees"""

    def test_binary_tree_insert(self):
        b = BinaryTree(key=5)
        b.insert(1)
        b.insert(8)
        self.assertEquals('(5, None) -> ((1, None) -> (-, -), (8, None) -> (-, -))', str(b))

    def test_binary_tree_extend(self):
        b = BinaryTree(key=5)
        b.extend([2, 4, 6, 8, 10])
        self.assertEquals(
            '(5, None) -> ((2, None) -> (-, (4, None) -> (-, -)), (6, None) -> (-, (8, None) -> '
            '(-, (10, None) -> (-, -))))',
            str(b)
        )

    def test_binary_tree_search(self):
        b = BinaryTree(key=5)
        b.extend([2, 4, 6, 8, 10])
        b.insert(7, 'Test')
        self.assertEquals('Test', b.search(7))

    def test_binary_tree_delete(self):
        b = BinaryTree(key=5)
        b.extend([2, 4, 6, 8, 10])
        b.delete(6)
        self.assertEquals(
            '(5, None) -> ((2, None) -> (-, (4, None) -> (-, -)), (8, None) -> (-, (10, None) -> (-, -)))',
            str(b)
        )

        b.delete(4)
        self.assertEquals(
            '(5, None) -> ((2, None) -> (-, -), (8, None) -> (-, (10, None) -> (-, -)))',
            str(b)
        )

        b.delete(5)
        self.assertEquals(
            '(2, None) -> (-, -), (8, None) -> (-, (10, None) -> (-, -))',
            str(b)
        )



