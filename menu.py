import xml.etree.ElementTree as ET
import playlist as PL

class Menu:
    currIdx = 0
    
    def __init__(self, xmlfile):
        self.playlists = []
        tree = ET.parse(xmlfile)
        root = tree.getroot()

        for child in root:
            self.playlists.append(PL.PlayList(child.attrib["name"], "images/" + child.attrib["image"]))

    def currPos(self):
        return self.playlists[self.currIdx]

    def nextPos(self):
        self.currIdx = self.currIdx + 1
        if (self.currIdx >= len(self.playlists)) :
            self.currIdx = 0
        return self.currPos()
    
    def prevPos(self):
        self.currIdx = self.currIdx - 1
        if (self.currIdx < 0) :
            self.currIdx = len(self.playlists) - 1
        return self.currPos()
        