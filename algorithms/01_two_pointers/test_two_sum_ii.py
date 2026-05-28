from two_sum_ii import two_sum_indices


def test_two_sum_indices_basic_case():
    assert two_sum_indices([2, 7, 11, 15], 9) == [1, 2]


def test_two_sum_indices_with_duplicates():
    assert two_sum_indices([1, 2, 3, 4, 4, 9], 8) == [4, 5]


def test_two_sum_indices_with_negative_numbers():
    assert two_sum_indices([-5, -2, 0, 3, 9], 1) == [2, 4]
