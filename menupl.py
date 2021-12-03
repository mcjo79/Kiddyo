import json
from math import *

class MenuPL:
    currIdx = 0
    currList = []
    videoList = []
    currentPage = 0
    
    def __init__(self, videoList):
        print("enter")
        self.videoList = videoList            
        self.currentPage = 0
        self.setCurrList()
        for video in videoList:
            print(json.dumps(video.__dict__))


    def currPos(self):
        return self.videoList[self.currIdx]

    def nextPos(self):
        self.currIdx = self.currIdx + 1
        if (self.currIdx >= len(self.videoList)) :
            self.currIdx = 0
        if self.currentPage != self.computePage():
            self.currentPage = self.computePage()
            self.setCurrList()
        return self.currPos()
    
    def prevPos(self):
        self.currIdx = self.currIdx - 1
        if (self.currIdx < 0) :
            self.currIdx = len(self.videoList) - 1
        if self.currentPage != self.computePage():
            self.currentPage = self.computePage()
            self.setCurrList()
        return self.currPos()
        
    def setCurrList(self):
        start = self.currentPage * 3
        self.currList.clear()
        while (start < len(self.videoList) and len(self.currList) < 3):
            self.currList.append(self.videoList[start])
            start = start + 1

    def computePage(self):
        return self.currIdx // 3

    def pageCount(self):
        return ceil(len(self.videoList) / 3.)