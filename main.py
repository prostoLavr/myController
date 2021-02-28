import datetime as dt


print("It's project help you manage what you did, do and want to do.")


class StatusObject:
    def __init__(self):
        print(f'Add object {self}')


class Completed(StatusObject):
    def __init__(self, time_to_end, mood):
        super(Completed, self).__init__()
        self.time = time_to_end
        self.mood = mood


class Process(StatusObject):
    def __init__(self, time_to_start, process_progress=0):
        super(Process, self).__init__()
        self.time = time_to_start
        self.process_progress = process_progress


class Desire(StatusObject):
    def __init__(self, step, time_to_add_in_desire):
        super(Desire, self).__init__()
        self.time = time_to_add_in_desire
        self.step = step


class Category:
    def __init__(self, status):
        self.status = status


class Book(Category):
    def __init__(self, author, name, status):
        super().__init__(status)
        self.author = author
        self.name = name
        self.status = status


book = Book('Lawrence', 'python', Desire(10, dt.datetime.now()))
print(book.name, book.status.time)

