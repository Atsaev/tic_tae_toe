class FileActions:
    """Класс, который записывает все результаты игры в файл"""

    def __init__(self):
        self.text = ''

    def write_to_file(self, filename, text):
        self.filename = filename
        self.text = text
        file = open(filename, 'r')
        content = file.read(12)
        print(content)
        file.close()
