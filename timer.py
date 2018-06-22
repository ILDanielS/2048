from time import time


class Timer:
    def __init__(self, end_time):
        self.__end_time = end_time
        self.__start_time = 0

    def is_over(self):
        return (time() - self.__start_time > self.__end_time)

    def start_timer(self):
        self.__start_time = time()
