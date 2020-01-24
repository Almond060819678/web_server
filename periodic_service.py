import threading
import time
import signal
import uuid
from datetime import timedelta

from db import db_handler, News

WAIT_TIME_SECONDS = 20


class ProgramKilled(Exception):
    pass


def create_news_db_records():
    print(time.ctime(), 'next iteration!')
    news = News(
        name=str(uuid.uuid4())
    )
    news.save()


def signal_handler(signum, frame):
    raise ProgramKilled


class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

    def stop(self):
        self.stopped.set()
        self.join()

    def run(self):
        while not self.stopped.wait(self.interval.total_seconds()):
            self.execute(*self.args, **self.kwargs)


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    job = Job(interval=timedelta(seconds=WAIT_TIME_SECONDS), execute=create_news_db_records)
    job.start()
    db_handler.connect()
    News.create_table()

    while True:
        try:
            time.sleep(1)
        except ProgramKilled:
            print("Program killed: running cleanup code")
            job.stop()
            break
