import unittest, RBTree


class TestMap(unittest.TestCase):

    def setUp(self):
        self.Map = RBTree.RBTree()
        self.Map.insert(8, 'A')
        self.Map.insert(18, 'B')
        self.Map.insert(5, 'C')
        self.Map.insert(15, 'D')
        self.Map.insert(17, 'E')
        self.Map.insert(25, 'F')
        self.Map.insert(40, 'G')
        

    def test_init_root(self):
        self.assertIsNotNone(self.Map.root) # Root is set
        self.assertIsNone(self.Map.root.parent) # Parent of root is None

    def test_init_tree(self):
        # Check if tree is initialized correctly using dft
        result = []
        it = RBTree.DFT_Iterator(self.Map)
        while(it.has_next()):
            result.append(next(it).key)
        self.assertListEqual(result, [8, 5, 17, 15, 25, 18, 40])

    def test_init_colors(self):
        # Check colors of initialized tree
        # RED
        self.assertTrue(self.Map.root.right.red) # 17
        self.assertTrue(self.Map.root.right.right.left.red) # 18
        self.assertTrue(self.Map.root.right.right.right.red) # 40
        # Black
        self.assertFalse(self.Map.root.red) # 8
        self.assertFalse(self.Map.root.left.red) # 5
        self.assertFalse(self.Map.root.right.left.red) # 15
        self.assertFalse(self.Map.root.right.right.red) # 25

    def test_insert_case13_dft(self):
        # Check if cases 1 and 3 work correct in insert_balance() using dft
        self.Map.insert(80, 'H')
        it = RBTree.DFT_Iterator(self.Map)
        result = []
        while(it.has_next()):
            result.append(next(it).key)
        self.assertListEqual(result, [17, 8, 5, 15, 25, 18, 40, 80])

    def test_insert_case13_colors(self):
        # Check colors after cases 1 and 3 in insert_balance()
        self.Map.insert(80, 'H')

        # Old nodes
        # RED
        self.assertTrue(self.Map.root.left.red) # 8
        self.assertTrue(self.Map.root.right.red) # 25
        # BLACK
        self.assertFalse(self.Map.root.red) # 17
        self.assertFalse(self.Map.root.left.left.red) # 5
        self.assertFalse(self.Map.root.left.right.red) # 15
        self.assertFalse(self.Map.root.right.left.red) # 18
        self.assertFalse(self.Map.root.right.right.red) # 40

        # New node
        # RED
        self.assertTrue(self.Map.root.right.right.right.red) # 80

    def test_insert_case23_dft(self):
        # Check if cases 2 and 3 work correct in insert_balance() using dft
        self.Map.insert(13, 'H')
        self.Map.insert(14, 'I')
        it = RBTree.DFT_Iterator(self.Map)
        result = []
        while(it.has_next()):
            result.append(next(it).key)
        self.assertListEqual(result, [8, 5, 17, 14, 13, 15, 25, 18, 40])

    def test_insert_case23_colors(self):
        # Check colors after cases 2 and 3 in insert_balance()
        self.Map.insert(13, 'H')
        self.Map.insert(14, 'I')

        # Old nodes
        # RED
        self.assertTrue(self.Map.root.right.red) # 17
        self.assertTrue(self.Map.root.right.left.right.red) # 15
        self.assertTrue(self.Map.root.right.right.left.red) # 18
        self.assertTrue(self.Map.root.right.right.right.red) # 40
        # BLACK
        self.assertFalse(self.Map.root.red) # 8
        self.assertFalse(self.Map.root.left.red) # 5
        self.assertFalse(self.Map.root.right.right.red) # 25

        # New nodes
        # RED
        self.assertTrue(self.Map.root.right.left.left.red) # 13
        # BLACK
        self.assertFalse(self.Map.root.right.left.red) # 14

    def test_insert_without_balance_dft(self):
        # Insert node without changing black height of the tree. Check tree using dft
        self.Map.insert(3, 'H')
        it = RBTree.DFT_Iterator(self.Map)
        result = []
        while(it.has_next()):
            result.append(next(it).key)
        self.assertListEqual(result, [8, 5, 3, 17, 15, 25, 18, 40])

    def test_insert_without_balance_colors(self):
        # Insert node without changing black height of the tree. Check colors of nodes
        self.Map.insert(3, 'H')

        # Old nodes
        # RED
        self.assertTrue(self.Map.root.right.red) # 17
        self.assertTrue(self.Map.root.right.right.left.red) # 18
        self.assertTrue(self.Map.root.right.right.right.red) # 40
        # BLACK
        self.assertFalse(self.Map.root.red) # 8
        self.assertFalse(self.Map.root.left.red) # 5
        self.assertFalse(self.Map.root.right.left.red) # 15
        self.assertFalse(self.Map.root.right.right.red) # 25

        # New node
        # RED
        self.assertTrue(self.Map.root.left.left.red) # 3

    def test_insert_exception(self):
        # Insertion of pair with key that already in the tree causes exception
        try:
            self.Map.insert(8, 'B')
        except Exception as e:
            self.assertEqual(str(e), "Pair with key=8 already exists")


    def test_remove_case12_dft(self):
        # Check if cases 1 and 2 work correct in remove_balance() using dft
        self.Map.remove(5)
        it = RBTree.DFT_Iterator(self.Map)
        result = []
        while(it.has_next()):
            result.append(next(it).key)
        self.assertListEqual(result, [17, 8, 15, 25, 18, 40])

    def test_remove_case12_colors(self):
        # Check colors after cases 1 and 2 in remove_balance()
        self.Map.remove(5)

        # RED
        self.assertTrue(self.Map.root.left.right.red) # 15
        self.assertTrue(self.Map.root.right.left.red) # 18
        self.assertTrue(self.Map.root.right.right.red) # 40
        # BLACK
        self.assertFalse(self.Map.root.red) # 17
        self.assertFalse(self.Map.root.left.red) # 8
        self.assertFalse(self.Map.root.right.red) # 25

    def test_remove_case34_dft(self):
        # Check if cases 3 and 4 work correct in remove_balance() using dft
        self.Map.remove(40)
        self.Map.remove(15)
        it = RBTree.DFT_Iterator(self.Map)
        result = []
        while(it.has_next()):
            result.append(next(it).key)
        self.assertListEqual(result, [8, 5, 18, 17, 25])
        
    def test_remove_case34_colors(self):
        # Check colors after cases 3 and 4 in remove_balance()
        self.Map.remove(40)
        self.Map.remove(15)

        # RED
        self.assertTrue(self.Map.root.right.red) # 18
        # BLACK
        self.assertFalse(self.Map.root.red) # 8
        self.assertFalse(self.Map.root.left.red) # 5
        self.assertFalse(self.Map.root.right.left.red) # 17
        self.assertFalse(self.Map.root.right.right.red) # 25

    def test_remove_without_balance_dft(self):
        # Remove node without changing black height of the tree. Check tree using dft
        self.Map.remove(18)
        it = RBTree.DFT_Iterator(self.Map)
        result = []
        while(it.has_next()):
            result.append(next(it).key)
        self.assertListEqual(result, [8, 5, 17, 15, 25, 40])

    def test_remove_without_balance_colors(self):
        # Remove node without changing black height of the tree. Check colors of nodes
        # RED
        self.assertTrue(self.Map.root.right.red) # 17
        self.assertTrue(self.Map.root.right.right.right.red) # 40
        # BLACK
        self.assertFalse(self.Map.root.red) # 8
        self.assertFalse(self.Map.root.left.red) # 5
        self.assertFalse(self.Map.root.right.left.red) # 15
        self.assertFalse(self.Map.root.right.right.red) # 25

    def test_remove_from_empty_exception(self):
        # Deleting node from empty tree causes exception
        empty = RBTree.RBTree()
        try:
            empty.remove(2)
        except Exception as e:
            self.assertEqual(str(e), "Map is empty")

    def test_remove_wrong_key_exception(self):
        # Deleting element with key that is not in the tree causes exception
        try:
            self.Map.remove(16)
        except Exception as e:
            self.assertEqual(str(e), "Pair with key=16 doesn't exist")

    def test_find(self):
        # Test find function
        self.assertEqual(self.Map.find(25), 'F')

    def test_not_found(self):
        # Find() returns None if pair with key is not it tree
        self.assertIsNone(self.Map.find(100))

    def test_find_in_empty_exception(self):
        # Searching in empty tree causes exception
        empty = RBTree.RBTree()
        try:
            empty.find(1)
        except Exception as e:
            self.assertEqual(str(e), "Map is empty")

    def test_clear(self):
        # Test clear function
        self.Map.clear()
        self.assertEqual(self.Map.root, self.Map.nil)

    def test_get_keys(self):
        # Test get_keys function
        self.assertListEqual(self.Map.get_keys(), [8, 5, 17, 15, 25, 18, 40])

    def test_get_keys_in_empty_map(self):
        # get_keys in empty tree returns empty list
        self.Map.clear()
        self.assertListEqual(self.Map.get_keys(), [])

    def test_get_values(self):
        # Test get_values function
        self.assertListEqual(self.Map.get_values(), ['A', 'C', 'E', 'D', 'F', 'B', 'G'])

    def test_get_values_in_empty_map(self):
        # get_values in empty tree returns empty list
        self.Map.clear()
        self.assertListEqual(self.Map.get_values(), [])

    def test_print(self):
        # Test print function
        self.assertEqual(str(self.Map), str([[8, 'A'], [5, 'C'], [17, 'E'], [15, 'D'], [25, 'F'], [18, 'B'], [40, 'G']])) # str() equals to print() because print calls __str__ or __repr__(more complex representation) methods

    def test_print_empty_map(self):
        # print in empty tree returns '[]'
        self.Map.clear()
        self.assertEqual(str(self.Map), str([]))

    def test_get_item(self):
        # Test 'get element by key' function
        self.assertEqual(self.Map[15], 'D')

    def test_get_item_none(self):
        # Getting item that is not in tree returns None
        self.assertIsNone(self.Map[100])

    def test_set_item(self):
        # Test 'set element by key' function
        self.Map[15] = 'J'
        self.assertEqual(self.Map[15], 'J')

    def test_set_item_in_empty_tree(self):
        # Setting element in empty tree causes exception
        self.Map.clear()
        try:
            self.Map[1] = 'V'
        except Exception as e:
            self.assertEqual(str(e), "Map is empty")

    def test_set_item_by_wrong_key(self):
        # Setting element by wrong key causes exception
        try:
            self.Map[100] = 'Z'
        except Exception as e:
            self.assertEqual(str(e), "Map doesn't have a pair with key=100")