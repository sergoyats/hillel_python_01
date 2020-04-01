import os
from datetime import datetime

# Преобразовать строку 'Name: Peter, Age: 20, Country: USA' 
# в словарь {'Name': 'Peter', 'Age': 20, 'Country': 'USA'} и записать в файл result.json

def jsonEncoder(data):
	with open('result.json', 'w') as result:
		splitData = (elem.split(':') for elem in data.split(',')) # генератор словаря
		prepData = {k.strip(): v.strip() for k, v in splitData}
		result.write(str(prepData))
		
jsonEncoder('Name: Peter, Age: 20, Country: USA')



# Написать декоратор, который будет логировать вызов и завершение функции в файл .log с метками времени.
# Записи в лог должны быть такими:
# 2020-03-13 17:29:32 - function 'имя функции' started
# 2020-03-13 17:29:32 - function 'имя функции' finished

# def with_log():
	# def wrapper(*args):
		# with open('test.log', 'a') as log:  # 'a' - append
			# log.write(f'{datetime.now()}-Function{func.__name__}started\n')
			# func(*args)
			# log.write(f'{datetime.now()}-Function{func.__name__}finished\n')
			
# @with_log
# def test_logging():
	# print('Inner function for testing')
	
	
	
# Напишите функцию, которая принимает два файла и объединяет их в один.
# Функция должна работать в двух режимах: 1 - последовательная запись; 2 - перемешка построчно

# def mix_files(mode, file1, file2):
	# with open(file1, 'r') as file1, open(file2, 'r') as file2, open('resultfile.txt', 'w') as result:
		# if mode == 1:
			# result.write(f'{file1.read()}\n{file2.read()}')
		# elif mode == 2:
			# for line_1 in file1.readlines():
				# for line_2 in file2.readlines():
					# result.write(f'{line_1}{line_2}')
				# continue
				
# mix_files(2, 'file_1.txt', 'file_2.txt')



# Написать функцию, которая читает и распечатывает текстовый файл.
# Декоратор этой функции должен печатать название файла и количество слов в нём.

# def check_file(func):
	# def wrapper(*args):
		# with open(*args[0]) as file:
			# words = file.read().split()
			# print(f'Opening file {args[0]}')
			# print(f'Words found: {len(words)}')
			# func(*args)
	# return wrapper
	
# @check_file
# def read_file(file_name):
	# with open(file_name) as file:
		# print(file.read())
		
# read_file('file_1.txt')



# Напишите функцию копирования файлов. На вход ваша функция принимает два аргумента:
# - путь файла, который необходимо скопировать
# - путь каталога, куда этот файл необходимо скопировать

def copyFileDir(inFile, outDir):
    with open(inFile, 'r') as file, open(outDir, 'w') as dir:
        dir.write(file.read())

# ИЛИ ПОДРОБНО:
def copyFileDir(inFile, outDir):
    os.chdir(outDir)  # преход в каталог по пути outDir
    testfile = open('task', 'w')  # создание testfile в каталоге
    testfile.write('')  # пока пустым
    testfile.close()
    with open(inFile, 'r') as infile, open('task', 'w') as outfile:
        outfile.write(infile.read())



# Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline

def str_to_html(tags):
    def decorator(func):
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }

        def wrapper(text):
		
            l = [tag_base[t] for t in tags]  # МОЙ СПОСОБ
            if len(tags) == 2:
                result = l[0].replace('%text%', l[1])
            if len(tags) == 3:
                result = l[0].replace('%text%', l[1]).replace('%text%', l[2])
            print(result)
			
			string = func(text)  # ЕГО СПОСОБ
			for tag in tags:
				string = tag_base[tag].replace('%text%', string)
			print(srting)
			
        return wrapper

    return decorator


@str_to_html(["italic", "bold"])
def get_text(text):
    return text



# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных

def log_reading(func):
    def wrapper(*args):
        result = func(*args)
        for f in result:
            if f.split('.')[1] == 'log':
                with open(f, 'r') as log:
                    log.read

    return wrapper


@log_reading
def get_files(outDir):  # outDir - путь каталогаё
    file_list = os.listdir(path=outDir)
    return file_list