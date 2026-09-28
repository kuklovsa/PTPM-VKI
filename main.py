import logging
import math
import sys




log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

# Базовая настройка корневого логгера
logging.basicConfig(
    level=logging.DEBUG, # Минимальный уровень логирования (аналог MinimumLevel.Debug)
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout),          # Настройка логирования в консоль
        logging.FileHandler("Logs/file_txt.log", encoding="utf-8") # Настройка логирования в файл
    ]
)

logging.info("Логгер успешно сконфигурирован")
logging.info("Приложение запущено")


def loglen (a):
    if type(a) != int:
        logging.critical('Сторона не число')
    elif a > 0:
        logging.info(f"Сторона: {a}")
    else:
        logging.warning(f"сторона меньше 0: {a}")


def get_triangle_vertices(a, b, c):

    if type(a) != int or type(b) != int or type(c) != int:
        return "не треугольник", (-2, -2), (-2, -2), (-2, -2)

    if a + b <= c or a + c <= b or b + c <= a:
        trty = ("не треугольник")
    if a == b == c:
        trty = ( "равносторонний")
    elif a == b or b == c or a == c:
        trty = ( "равнобедренный")
    else:
        trty = ("разносторонний")
    # Проверка неравенства треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        return (-1, -1), (-1, -1), (-1, -1)
    if a < 1 or b < 1 or c < 1:
        return (-1, -1), (-1, -1), (-1, -1)

    # Первая и вторая вершины
    x1, y1 = 0.0, 0.0
    x2, y2 = float(c), 0.0

    # Находим угол между сторонами c и b по теореме косинусов
    cos_A = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    sin_A = math.sqrt(1.0 - cos_A ** 2)

    # Третья вершина (x3, y3)
    x3 = b * cos_A
    y3 = b * sin_A

    return trty, (x1, y1), (x2, y2), (x3, y3)


def proga ():
    a = input('сторона а: ')
    loglen (a)
    b = input('сторона b: ')
    loglen(b)
    c = input('сторона c: ')
    loglen(c)

    trty, v1, v2, v3 = get_triangle_vertices (a, b, c)
    print (trty,' ', v1,' ', v2,' ', v3)



proga()