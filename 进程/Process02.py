import multiprocessing
from  time import sleep, ctime


class ClockProcess(multiprocessing.Process):

    """
    两个函数
    1. init函数
    2. run函数
    """
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print("The time is %s" % ctime())
            sleep(self.interval)

if __name__ == '__main__':

    p = ClockProcess(3)
    p.start()

    while True:
        print('Sleeping...')
        sleep(1)