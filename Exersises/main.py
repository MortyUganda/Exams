import contextlib
import io
import os
import shutil
from zipfile import ZipFile
import pytest
import re

from main import *  # обратите внимание на название Вашего файла (у меня main.py)


def move_zip_to_project() -> None:
    """
    Функция переносит zip-архив с тестами в Ваш проект
    """
    downloads_dir_path = '/Users/zhugan81/Downloads'  # путь к папке "Загрузки"
    test_file = [file for file in os.scandir(downloads_dir_path) if re.fullmatch(r'\d+\.zip', file.name)]
    if test_file:
        shutil.move(test_file[0].path, 'tests.zip')


def get_filenames_from_zip():
    """
    Функция получает имена файлов из zip-архива с тестами
    """
    move_zip_to_project()
    file_names = map(lambda x: (str(x), f'{x}.clue'), range(1, len(ZipFile('tests.zip').filelist) // 2 + 1))
    return file_names


def capture_stdout(code_to_exec: str) -> str:
    """
    Функция выполняет блок кода из тестового файла, перехватывает вывод результатов в консоль (STDOUT)
    и сохраняет в переменную для последующей обработки
    :param code_to_exec: блок кода из тестового файла
    :return: результат вычисления блока кода из тестового файла
    """
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        exec(code_to_exec)
    return output.getvalue().strip()


@pytest.mark.parametrize("test_filename, clue_filename", get_filenames_from_zip())
def test_stepik(test_filename, clue_filename):
    with ZipFile('tests.zip') as zip_file:
        test_input = zip_file.open(test_filename).read().decode()
        expected = zip_file.open(clue_filename).read().decode()
    assert capture_stdout(test_input) == expected