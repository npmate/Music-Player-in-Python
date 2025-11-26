import pygame

class Player:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0)
        self.is_paused = True

    def load(self, path):
        pygame.mixer.music.load(path)

    def play(self):
        if self.is_paused:
            print("sound playing")
            pygame.mixer.music.play()
            self.is_paused = False
        else:
            print("sound is already playing")

    def pause(self):
        if not self.is_paused:
            print("sound paused")
            pygame.mixer.music.pause()
            self.is_paused = True
        else:
            print("sound has already been paused")
    
    def resume(self):
        if self.is_paused:
            print("sound resumed")
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            print("sound is already playing")

        
    def stop(self):
        if not self.is_paused:
            print("sound stopped")
            pygame.mixer.music.stop()
            self.is_paused = True
        else:
            print("sound has already been stopped")

    def volume(self, value):
        pygame.mixer.music.set_volume(float(value/100))
        
if __name__ == "__main__":
    player = Player(file=None)
    player.play()
    player.stop()
    player.stop()
