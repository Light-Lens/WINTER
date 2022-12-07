import numpy, os

# Play offline media
def PlayOfflineMedia(media):
    # List all the files in the given directory and play them randomly.
    def StartPlaying(Directory):
        Files = os.listdir(Directory)
        Media = os.path.join(Directory, numpy.random.choice(Files))
        os.startfile(Media)
        return Media

    if any(i in media for i in ["song", "music"]):
        Dir = "D:\\Srijan\\Music"
        Name = StartPlaying(Dir)

    elif any(i in media for i in ["video", "movie"]):
        Dir = "D:\\Srijan\\Videos"
        Name = StartPlaying(Dir)

    elif any(i in media for i in ["pic", "picture", "image", "photo"]):
        Dir = "D:\\Srijan\\Pictures"
        Name = StartPlaying(Dir)

    else: return None
    return ""
