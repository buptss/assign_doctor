# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 09:59:51 2018

@author: shahongzhou
"""
import heapq

class worker:
    def __init__(self, id, endtime):
        self.id = id
        self.endtime = endtime
    def renew(self, endtime):
        self.endtime = endtime
    def __lt__(self,other):
        if self.endtime < other.endtime:
            return True
        else:
            return False
        

class Topkheap(object):
    def __init__(self, k):
        self.k = k
        self.data = []
    def Push(self,starttime,duringtime):
        if len(self.data) <self.k:
            endtime = starttime + duringtime
            doctorid = len(self.data)
            doctor = worker(doctorid, endtime)
            heapq.heappush(self.data, doctor)
            print("任务实际开始时间:",starttime,"分配给doctor id", doctorid,"完成时间:",endtime)
        else:
            topksmall = self.data[0].endtime

            if topksmall < starttime:
                endtime = starttime + duringtime
            else:
                endtime = topksmall + duringtime
            doctor = self.data[0]            
            doctor.renew(endtime)       
            heapq.heapreplace(self.data, doctor)
            print("任务实际开始时间:",endtime-duringtime,"分配给doctor id", doctor.id,"完成时间:",endtime)
            
            

def assign_doctor(m, startlist,duringlist):
    th = Topkheap(m)
    for i in range(len(startlist)):
        th.Push(startlist[i], duringlist[i])
        
assign_doctor(5,[2,3,4,5,8,10,15,30,55],[5,5,5,5,5,5,8,10,12])