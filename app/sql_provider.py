import os
from string import Template


class SQLProvider:
    # инизиализация файла в папке и открытие sql запроса из файла для чтения
    def __init__(self, file_path):
        self.scpirts = {}

        for file in os.listdir(file_path):
            if file.endswith('.sql'):
                self.scpirts[file] = Template(
                    open(f'{file_path/file}', 'r').read())

    def get(self, file_name, **kwargs):
        return self.scpirts[file_name].substitute(**kwargs)
