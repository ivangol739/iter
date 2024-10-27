from time import sleep


class FlatIterator:
  def __init__(self, list_of_list):
    self.list_of_list = [a for b in list_of_list for a in b]

  def __iter__(self):
    self.cursor = -1
    return self

  def __next__(self):
    self.cursor += 1
    if self.cursor >= len(self.list_of_list):
      raise StopIteration
    return self.list_of_list[self.cursor]


# for iten in FlatIterator(list_of_lists_1):
#   print(iten)
#   sleep(1)


def test_1():
  list_of_lists_1 = [
      ['a', 'b', 'c'],
      ['d', 'e', 'f', 'h', False],
      [1, 2, None]
  ]

  for flat_iterator_item, check_item in zip(
          FlatIterator(list_of_lists_1),
          ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
  ):

      assert flat_iterator_item == check_item

  assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
  test_1()