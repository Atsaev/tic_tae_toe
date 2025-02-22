class FileActions:
    """Класс, который записывает все результаты игры в файл"""

    def __init__(self):
        self.text = ''

    def write_to_file(self, filename, text):
        self.filename = filename
        self.text = text
        with open(filename, 'a') as file:
            file.write(text + '\n')
            file.close()
