import article_manager
import os
import threading
import time

collection = article_manager.__file__.replace('article_manager.py', '../article_database/collection.py')


def main():
    while True:
        os.system(f'python3 {collection}')
        time.sleep(100)


if __name__ == '__main__':
    threading.Thread(target=main, args=()).start()
