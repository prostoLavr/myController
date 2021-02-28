# import datetime as dt  # It can be needed

print("It's project help you manage what you did, do and want to do.")


class Status:
    def __init__(self):
        print(f'Add object {self}')

    class Completed:
        def __init__(self, time_to_end, mood):
            super().__init__()
            self.time = time_to_end
            self.mood = mood

    class Process:
        def __init__(self, time_to_start, process_progress=0):
            super().__init__()
            self.time = time_to_start
            self.process_progress = process_progress

    class Desire:
        def __init__(self, step, time_to_add_in_desire):
            super().__init__()
            self.time = time_to_add_in_desire
            self.step = step


class Category:
    def __init__(self, status: Status, text_description: str):
        self.status = status
        self.text = text_description


class Book(Category):
    def __init__(self, name: str, author: str, status: Status, text_description=''):
        super().__init__(status, text_description)
        self.author = author
        self.name = name
        self.status = status


class Film(Category):
    def __init__(self, name: str, year: int, status: Status, text_description=''):
        super().__init__(status, text_description)
        self.name = name
        self.year = year


class MyCategory(Category):
    def __init__(self, parameters: dict, status: Status, text_description=''):
        super().__init__(status, text_description)
        self.parameters = parameters
