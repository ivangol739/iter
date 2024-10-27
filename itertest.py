from time import sleep

#Итератор
words = ['Тысяча черетй!', 'Карамба', 'Пиастры', 'На абордаж!']
#
# # for word in words:
# # 	print(word)
#
# # iter_ = iter(words)
# iter_ = words.__iter__()
# while True:
# 	try:
# 		print(iter_.__next__())
# 		sleep(1)
# 	except StopIteration:
# 		break

# old
class Parrot:
	def __init__(self, words):
		self.words = words

	def __iter__(self):
		return VocabularyIterator(self.words)


class VocabularyIterator:
	def __init__(self, vocabulary):
		self.vocabulary = vocabulary
		self.cursor = -1

	def __next__(self):
		self.cursor += 1
		# self.cursor %= len(self.vocabulary)
		if self.cursor == len(self.vocabulary):
			raise StopIteration
		return self.vocabulary[self.cursor]


# pop = Parrot(words)
# for word in pop:
# 	print(word)


# new
class NewParrotWithLimit:
	def __init__(self, words, limit):
		self.vocabulary = words
		self.limit = limit

	def __iter__(self):
		self.cursor = -1
		self.total_cursor = -1
		return self

	def __next__(self):
		self.total_cursor += 1
		self.cursor += 1
		self.cursor %= len(self.vocabulary)
		if self.cursor == self.limit:
			raise StopIteration
		return self.vocabulary[self.cursor]

# pop = NewParrotWithLimit(words, 7)
# for word in pop:
# 	print(word)


class MyRange:
	def __init__(self, a, b=None, c=None):
		if c is not None:
			self.start = a
			self.end = b
			self.step = c
		elif b is not None:
			self.start = a
			self.end = b
			self.step = 1
		else:
			self.start = 0
			self.end = a
			self.step = 1

	def __iter__(self):
		self.cursor = self.start
		return self

	def __next__(self):
		if self.cursor >= self.end:
			raise StopIteration
		else:
			self.cursor += self.step
			return self.cursor - self.step


# for i in MyRange(3, 17, 2):
# 	print(i)



#Генератор
# def simple_generator(number):
# 	cursor = 0
# 	while True:
# 		yield number - cursor
# 		cursor += 1
#
#
# for num in simple_generator(4):
# 	print(num)
# 	sleep(1)


def parrot(words, limit):
	cursor = -1
	for _ in range(limit):
		cursor += 1
		cursor %= len(words)
		yield words[cursor]

# for word in parrot(words, 7):
# 	print(word)
# 	sleep(1)


def myrange(start, end):
	cursor = start
	while cursor < end:
		yield cursor
		cursor += 1


l_c = [i * i for i in range(20) if i % 2 != 0]
print(l_c)

generator_ = (i * i for i in range(20) if i % 2 != 0)
for num in generator_:
	print(num)

