class FileActions:
    """Класс, который записывает все результаты игры в файл"""

    def __init__(self):
        self.text = ''

    def save_result(self, filename, text):
        with open(filename, 'a') as file:  # Open the file in append mode
            # Add a newline character for better readability
            file.write(text + '\n')
