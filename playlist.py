class PlayList:
    id=""
    name=""
    image=""
    folder=""
    videos = []

    def __init__(self, id, name, image, folder):
        self.id = id
        self.name = name
        self.image = image
        self.folder = folder
        self.videos = []

    def addVideo(self, video):
        self.videos.append(video)