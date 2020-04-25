'''У вас есть список(list) IP адресов. Вам необходимо создать
класс который сможет:
1) Получить и изменить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13)'''


class IpHandler:
    """Handles a list of IPs, each IP must be a string"""

    def __init__(self, ipList):
        self._ipList = list

    @property
    def ipList(self):
        return self._ipList

    @ipList.setter
    def ipList(self, newList):
        self._ipList = newList

    def reverse_IP(self):
        """Return it's IPs reversed"""
        return self._ipList[::-1]

    def get_oct_1_3(self):
        """Returns a list of IPs without first octets (127.0.0.1 -> .0.0.1)"""
        return [f[3:] for f in self._ipList]

    def get_oct_3(self):
        """Returns a list of last octets of each IP (127.0.0.1 -> .1)"""
        return [l[-2:] for l in self._ipList]


'''У вас несколько JSON файлов. В каждом из этих файлов есть
произвольная структура данных. Вам необходимо написать
класс (без реализации конструктора) который будет описывать работу с
этими файлами, а именно:
1) Запись в файл
2) Чтение из файла
3) Получить путь относительный путь к файлу
4) Получить абсолютный путь к файлу'''

import os.path


class JSONhandler:
    """Handles .json files: read, write, get abs/rel path"""

    def read(self, file):
        """Reads json file"""
        with open(file, 'r') as f:
            f.read()

    def write(self, input_data, file):
        """Writes json-formatted data to provided file"""
        with open(file, 'w') as f:
            f.write(input_data)

    def get_absolute_path(self, file):
        """Returns absolute path to provided file"""
        return os.path.abspath(file)

    def get_relative_path(self, file):
        """Returns relative path to provided file"""
        return os.path.relpath(file)  # относительно текущей директории


'''Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и назначения этих атрибутов в классе.'''


class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, another_name):
        self._unit_name = another_name

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, another_mac):
        self._mac_address = another_mac

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, another_ip):
        self._ip_address = another_ip

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, another_login):
        self._login = another_login

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, another_password):
        self._password = another_password


'''Создать класс для представления информации о времени. Ваш класс должен иметь
возможности установки времени и изменения его отдельных полей (час, минута,
секунда) с проверкой допустимости вводимых значений. В случае недопустимых
значений полей нужно установить максимально допустимое значение.
Создать методы изменения времени на заданное количество часов, минут и секунд.'''


class Time:
	def __init__(self, h=0, m=0, s=0):
		# а нельзя ли написать сразу:
		# self.hours, self.minutes, self.seconds = h, m, s
		self.hours = h
		self.minutes = m
		self.seconds = s
		
	@property
	def hours(self):
		return self.hours

	@hours.setter
	def hours(self, new_hours):
		if new_hours <= 24:
			self.hours = new_hours
		else:
			print('The invalid value for hours!')

	@property
	def minutes(self):
		return self.minutes

	@minutes.setter
	def minutes(self, new_min):
		if new_min <= 60:
			self.minutes = new_min
		else:
			print('The invalid value for minutes!')

	@property
	def seconds(self):
		return self.seconds

	@minutes.setter
	def seconds(self, new_sec):
		if new_sec <= 60:
			self.seconds = new_sec
		else:
			print('The invalid value for seconds!')

	def __repr__(self):
		return f'{self.hours}, {self.minutes}, {self.seconds}'

	def __str__(self):
		return f'{self.hours}:{self.minutes}:{self.seconds}'


# САМАЯ ПОЛЕЗНАЯ ЗАДАЧА. С чётким, сразу понятным условием. Мозгоплавильная, но интересная!
'''Создайте класс Student, который содержит атрибуты: фамилия и инициалы, номер
группы, успеваемость (массив из пяти элементов).
Создайте список студентов из десяти элементов (10 экземпляров вашего класса).
Напиши функции:
1. Упорядочить массив по возрастанию среднего балла.
2. Вывести фамилии и номера групп студентов, имеющих оценки, равные
только 4 или 5.'''


class Student(object):
	def __init__(self, name, num, perf):  # perf - performance, not perforator
		self.name = name
		self.num = num
		self.perf = perf


# успеваемость указал по 5-балльной шкале, хотя единицы, вроде, не принято ставить
s_list = [
    Student('Petrov P.P.', 1, [1, 2, 2, 3, 2]),
    Student('Ivanov I.I', 3, [2, 3, 3, 4, 1]),
    Student('Sidorov S.S', 4, [3, 4, 2, 3, 3]),
    Student('Andreev A.A.', 2, [4, 4, 5, 4, 4]),
    Student('Fomin F.F.', 5, [2, 1, 2, 1, 2]),
    Student('Lukin L.L.', 1, [3, 2, 4, 2, 1]),
    Student('Churov C.C.', 2, [1, 1, 2, 1, 1]),
    Student('Nosov N.N.', 3, [3, 3, 1, 3, 3]),
    Student('Rocotov R.R.', 4, [2, 5, 3, 1, 4]),
    Student('Yurlov Y.Y.', 5, [4, 5, 5, 5, 5])
]


def sort_by_avg_mark(s_list):
    middle = [(m.name, m.num, sum(m.perf) / len(m.perf)) for m in s_list]
    return sorted(middle, key=lambda x: x[2])


def get_best_by_mark(s_list):
    best = [(b.name, b.num) for b in s_list if all([i > 3 for i in b.perf])]
    return best


print(sort_by_avg_mark(s_list))
print(get_best_by_mark(s_list))