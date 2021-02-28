# import datetime


print("It's project help you manage what you did, do and want to do.")


completed_arr = []
process_arr = []
desire_arr = []


class StatusObject:
    def __init__(self, arr):
        self.arr = arr
        arr.append(self)

    def delete(self):
        self.arr.remove(self)


class Completed(StatusObject):
    def __init__(self, data, status, arr):
        super(Completed, self).__init__(arr)
        #  self.data_time = datetime.datetime(*data)
        self.data_time = data
        self.status = status


class Process(StatusObject):
    def __init__(self, arr):
        super(Process, self).__init__(arr)

    def do_completed(self, data, status, arr):
        Completed(data, status, arr)


class Desire(StatusObject):
    def __init__(self, step, arr):
        super(Desire, self).__init__(arr)
        self.step = step

    def do_process(self, arr):
        Process(arr)


def test_me():
    Desire(1, desire_arr)
    Desire(3, desire_arr)
    print(desire_arr)
    for el in desire_arr:
        el.do_process(process_arr)
    print(process_arr)
    for el in process_arr:
        el.do_completed('today', 'fine', completed_arr)
    print(completed_arr)
    for el in completed_arr:
        print(el)
        print(el.data_time, el.status)


test_me()
