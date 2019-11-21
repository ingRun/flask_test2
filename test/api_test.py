import time

import requests
import random
import _thread as thread


def login_post(k):
    for i in range(1000):
        data = {'email': (str(int(random.random() * 1000))),
                'password': (str(int(random.random() * 1000)))}
        try:
            r = requests.post('http://localhost:8081/api/register', data=data)
            r.close()
        except Exception:
            print(f'第{k}线程，第 {i + 1} 次请求  失败')
            break


def main():
    for i in range(1000):
        thread.start_new_thread(login_post, (i, ))


if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)
