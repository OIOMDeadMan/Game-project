from pygame import mixer



class Music:
    def __init__(self):
        self.main_music = mixer.music.load(r'Game\game_assets\Music\man-is-he-mega.wav')

    def music_player(self):
            mixer.init()
            mixer.music.play(-1)