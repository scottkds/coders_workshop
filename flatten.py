import unittest

def flatten(list_to_flatten):
    """Creates a one-dimensional copy of the original list. Each atomic value is copied directly 
    into the returned list. Each list or tuple encountered in the original list has its elements
    fully expanded into the returned list.""" 
    flattened_list = []
    for item in list_to_flatten:
        if isinstance(item, list) or isinstance(item, tuple):
            flattened_list += flatten(item)
        else:
            flattened_list.append(item)
    return flattened_list


class TestFlatten(unittest.TestCase):

    def test_flatten(self):
        self.assertEqual(flatten([1, 2, 3, [1, 2, 3, [1, 2, 3]]]), [1, 2, 3, 1, 2, 3, 1, 2, 3])
        self.assertEqual(flatten([1, 2, 3, (1, 2, 3, (1, 2, 3))]), [1, 2, 3, 1, 2, 3, 1, 2, 3])

if __name__ == '__main__':

    unittest.main()
