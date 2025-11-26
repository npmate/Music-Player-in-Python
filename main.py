from gui import GUI
from player import Player

class Main:
    def __init__(self):
        self.gui = GUI()
        self.player = Player()
    
    def play(self):
        self.player.play()
    
    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
    
    def load_player(self, path):
        self.player.load(path=path)
        print(f'Loading file: {path}') 

    def resume(self):
        self.player.resume()

    def volume(self, value):
        self.player.volume(value)
    
    def run(self):
        self.callbacks = {
            "play": self.play,
            "pause": self.pause,
            "stop": self.stop,
            "open": self.load_player,
            "resume": self.resume,
            "volume": self.volume
            
        }
        self.gui.callbacks(self.callbacks)
        self.gui.run()


if __name__ == "__main__":
    main = Main()
    main.run()