# 1. Написать свой cache декоратор c максимальным размером кеша и его очисткой
# при необходимости.

def do_cache(maxsize):
	def decorator(func):
		cache = dict()
		def wrapper(*args):
			if len(cache) >= maxsize:
				cache.pop(list(cache)[0])
			if args in cache:
				return args
			else:
				func(*args)
				cache.update(func(*args))
				return func(*args)
		return wrapper
	return decorator


@do_cache(maxsize=2)
def test(v, i):
	return v + i


# 2. Написать свой декоратор который будет проверять остаток от деления числа 100
# на результат работы функции ниже. Если остаток от деления = 0, вывести
# сообщение "We are OK!», иначе «Bad news guys, we got {остаток от деления}».
# Этот декоратор не должен возвращать результат работы функции. Только один из
# указанных принтов.

def div100(func):
	def wrapper(*args):
		if 100 % func(*args) == 0:
			print('We are OK!')
		else:
			print('Bad news guys, we got', 100 % func(*args))
	return wrapper


@div100
def test2(v):
	return v


# 3. Декоратор должен кэшировать значения аргументов, считать количество
# использований одних и тех же аргументов и печатать их перед исполнением
# декорируемой функции.

def count_args(func):
	cache = dict()
	cache_count = dict()
	def wrapper(*args):
		cache.update(func(*args))
		cache_count = {list(cache): list(cache).count(*args)}
		print(cache_count)
	return wrapper


@count_args
def my_func(string):
	return string
