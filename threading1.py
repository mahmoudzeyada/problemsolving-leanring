import logging

import threading

import time

import concurrent.futures
import random

# x = threading.Lock()
# a = 0


# def thread_function1(name):
#     x.acquire()
#     print("hello")
#     a += 1
#     # x.release()


# def thread_function2(name):
#     x.acquire()
#     print(name)
#     x.release()


# x1 = threading.Thread(target=thread_function2, daemon=True, args=(0,))
# x2 = threading.Thread(target=thread_function2, daemon=True, args=(1,))
# x1.start()
# x2.start()


# class fakedb:
#     def __init__(self):
#         self.value = 0
#         self._Lock = threading.Lock()

#     def update(self, name):
#         logging.info("Thread %d stating updating", name)
#         logging.info("Thread %d about to lock", name)
#         with self._Lock:
#             logging.info("Thread %d locking", name)
#             local_value = self.value
#             local_value += 1
#         # making race condition
#             # time.sleep(20)
#             self.value = local_value
#             logging.info("Thread %s about to release", name)
#         logging.info("Thread %s: finishing realising", name)
#         logging.info("Thread %s: finishing update", name)


# def thread_function(name):

#     logging.info("Thread %s: starting", name)

#     time.sleep(2)

#     logging.info("Thread %s: finishing", name)


# if __name__ == "__main__":

#     format = "%(asctime)s: %(message)s"

#     logging.basicConfig(format=format, level=logging.INFO,

#                         datefmt="%H:%M:%S")
#     logging.getLogger().setLevel(logging.DEBUG)
#     db = fakedb()
#     logging.info("Testing update. Starting value is %d.", db.value)

#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#         for index in range(2):
#             executor.submit(db.update, index)
#     logging.info("Testing update. Ending value is %d.", db.value)

class Pipeline:
    """
    Class to allow a single element pipeline between producer and consumer.
    """

    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug("%s:about to acquire getlock", name)
        self.consumer_lock.acquire()
        logging.debug("%s:have getlock", name)
        message = self.message
        logging.debug("%s:about to release setlock", name)
        self.producer_lock.release()
        logging.debug("%s:setlock released", name)
        return message

    def set_message(self, message, name):
        logging.debug("%s:about to acquire setlock", name)
        self.producer_lock.acquire()
        logging.debug("%s:have setlock", name)
        self.message = message
        logging.debug("%s:about to release getlock", name)
        self.consumer_lock.release()
        logging.debug("%s:getlock released", name)


pipline = Pipeline()


SENTINEL = object()


def producer(pipeline):
    """Pretend we're getting a message from the network."""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    # Send a sentinel message to tell consumer we're done
    pipeline.set_message(SENTINEL, "Producer")


def consumer(pipeline):
    """Pretend we're saving a number in the database."""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(producer, pipline)
    executor.submit(consumer, pipline)
