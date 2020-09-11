import re
from pprint import pprint

# -*- coding: utf-8 -*-

"""
Задание 15.1

Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""

def test3(l):
    return tuple(l)

def test2(l, t):
    l.append(t)
    pprint(l)

def test1(p):
    l = []
    for i in range(3):
        l.append(i)
        test2(l, tuple(l))

def get_ip_from_cfg(fileName = 'config_r1.txt'):
    result = []

    r = " ip address (\d+.\d+.\d+.\d+) (\d+.\d+.\d+.\d+)"

    with open(fileName, 'r') as f:
        for s in f:
            math = re.search(r, s)
            if math:
                result.append((math.group(1, 2)))

    return result

if __name__ == "__main__":
    pprint(get_ip_from_cfg())
    test1(1)
    print('end code')