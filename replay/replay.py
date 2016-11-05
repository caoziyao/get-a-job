
# from replay import *
# from replay.lagouAPI import LagouAPI

import queue
import threading
import requests
from lagouAPI import LagouAPI

def get_worker():
    pass


def main():
    try:
        jd = LagouAPI.search('Python',city='深圳')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()    

