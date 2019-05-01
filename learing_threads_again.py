import random
import concurrent.futures
import logging
import time
import threading
import queue

format = "%(asctime)s: %(message)s"

logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        with self._lock:
            logging.info('Thread %s:starting update', name)
            local_copy = self.value
            local_copy += 1

            time.sleep(5)

            self.value = local_copy
        logging.info('Thread %s :finishing update', name)


db = FakeDatabase()

x = 5


def function1(index):
    logging.info('Thread function %s', index)
    lock = threading.Lock()
    with lock:
        global x
        logging.info('Thread function running %s', index)
        time.sleep(10)
        x += 1
        logging.info('Thread function finished %s', index)


def function2(index):
    logging.info('Thread function %s', index)
    lock = threading.Lock()
    with lock:
        global x
        logging.info('Thread function running %s', index)
        x += 1
        logging.info('Thread function finished %s', index)


# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     executor.submit(function1, 1)
#     executor.submit(function2, 2)
# logging.info("value x %d.", x)


# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     executor.map(db.update, range(2))
# logging.info("Testing update. Ending value is %d.", db.value)


class PipLine():
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        self.consumer_lock.acquire()
        message = self.message
        self.producer_lock.release()
        return message

    def send_message(self, name, message):
        self.producer_lock.acquire()
        self.message = message
        self.consumer_lock.release()


pipline = PipLine()


def producer(pipline):
    for index in range(10):
        message = random.randint(1, 200)
        logging.info("Producer got message :%s", message)
        logging.info("Creating Producer Thread %d", index)
        pipline.send_message("Producer", message)

    pipline.send_message("finished")


def consumer(pipline):
    message = 0
    count = 0
    while message != "finished":
        logging.info("Creating Consumer Thread %d", count)
        message = pipline.get_message("Consumer")
        logging.info("Consumer storing message: %s", message)
        count += 1


# with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
#     executor.submit(producer, pipline)
#     executor.submit(consumer, pipline)


def producerq(queue, event):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        queue.put(message)

    logging.info("Producer received event. Exiting")


def consumerq(queue, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(
            "Consumer storing message: %s (size=%d)", message, queue.qsize()
        )

    logging.info("Consumer received event. Exiting")


custom_queue = queue.Queue(maxsize=1)
event = threading.Event()

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(consumerq, custom_queue, event)
    executor.submit(producerq, custom_queue, event)

    time.sleep(0.1)
    logging.info('Main:about to set event')
    event.set()
