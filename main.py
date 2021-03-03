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


if __name__ == '__main__':
    arr = []
    txt = None
    while txt not in ('', 'exit', 'exit'):
        txt = input('>>>').lower()
        if txt == 'add':
            ctg = input('Change the category: ').lower()
            if ctg == 'book':
                names = input('Print name: '), input('Print author: ')
                st = input('change the status: ').lower()
                if st == 'progress':
                    status = Status.Process(input('Print time to start: '))
                elif st == 'desire':
                    status = Status.Desire(int(input('Print step: ')), input('Print time to add in desire: '))
                elif st == 'completed':
                    status = Status.Completed(input('Print time to end: '), input('Print your mood: '))
                else:
                    status = Status.Desire(0, 'time')
                arr.append(Book(*names, status, input('Print some text: ')))
        if txt == 'list':
            print(arr)
            print(*list(map(lambda x: (x.name, x.author), arr)))

