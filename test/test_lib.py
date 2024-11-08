from main.lib import shaker_sort


def test_shaker_sort_positive():
    # Тест 1: Случайный порядок
    assert shaker_sort([5, 3, 8, 4, 2, 7, 1, 10]) == sorted([5, 3, 8, 4, 2, 7, 1, 10])
def test_shaker_sort_negative():
    # Тест 2: Уже отсортированный массив
    assert not shaker_sort([1, 2, 3, 4, 5]) == [1, 2, 4, 3, 5]

