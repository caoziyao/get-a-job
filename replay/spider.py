

from models.job import JobModel
from replay.lagouAPI import LagouAPI
import queue
import threading
import requests

# from lagouAPI import LagouAPI


def get_job():

    pass


def lagou_spider():
    try:
        jd = LagouAPI.search('Python',city='全国')  #深圳
        for j in jd:
            info = LagouAPI.geo_info(j)
            print(info) 
            job = JobModel(info)
            job.save()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    lagou_spider()    

