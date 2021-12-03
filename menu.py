import xml.etree.ElementTree as ET
import playlist as PL
import video as VD
import json
import uuid
from math import *

class Menu:
    currIdx = 0
    currList = []
    playlists = []
    currentPage = 0
    
    def __init__(self, xmlfile):
        self.playlists = []
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        id = 0
        for child in root:
            pl = PL.PlayList(str(uuid.uuid4()), child.attrib["name"], "images/" + child.attrib["image"], child.attrib["folder"])
            print(json.dumps(pl.__dict__))
            vId = 0
            for subchild in child:
                vd = VD.Video(str(uuid.uuid4()),  subchild.attrib["name"], "images/" + subchild.attrib["image"], child.attrib["folder"] +"/" + subchild.attrib["file"])
                pl.addVideo(vd)
                vId = vId + 1
                print(json.dumps(vd.__dict__))
            self.playlists.append(pl)
            id = id + 1
            
        self.currentPage = 0
        self.setCurrList()


    def currPos(self):
        return self.playlists[self.currIdx]

    def nextPos(self):
        self.currIdx = self.currIdx + 1
        if (self.currIdx >= len(self.playlists)) :
            self.currIdx = 0
        if self.currentPage != self.computePage():
            self.currentPage = self.computePage()
            self.setCurrList()
        return self.currPos()
    
    def prevPos(self):
        self.currIdx = self.currIdx - 1
        if (self.currIdx < 0) :
            self.currIdx = len(self.playlists) - 1
        if self.currentPage != self.computePage():
            self.currentPage = self.computePage()
            self.setCurrList()
        return self.currPos()
        
    def setCurrList(self):
        start = self.currentPage * 6
        self.currList.clear()
        while (start < len(self.playlists) and len(self.currList) < 6):
            self.currList.append(self.playlists[start])
            start = start + 1

    def computePage(self):
        return self.currIdx // 6

    def pageCount(self):
        return ceil(len(self.playlists) / 6.)