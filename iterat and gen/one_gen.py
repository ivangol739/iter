import types
from time import sleep

def flat_generator(list_of_lists):
  for sublist in list_of_lists:
    for item in sublist:
      yield item

# for _ in flat_generator(list_of_lists_1):
#   print(_)
#   sleep(1)

def test_2():
  list_of_lists_1 = [
      ['a', 'b', 'c'],
      ['d', 'e', 'f', 'h', False],
      [1, 2, None]
  ]

  for flat_iterator_item, check_item in zip(
          flat_generator(list_of_lists_1),
          ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
  ):

      assert flat_iterator_item == check_item

  assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

  assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
  test_2()