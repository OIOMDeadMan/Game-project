from pygame import mixer



class Music:
    def __init__(self):
        def main_music(self):
            mixer.init()
            mixer.music.load('man-is-he-mega.wav')
            mixer.music.play(-1)