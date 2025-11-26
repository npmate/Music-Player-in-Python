import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Music Player")
        self.volume_var = tk.IntVar(value=100)
        self.volume_text = tk.StringVar(value=f'Volume: {self.volume_var.get()}%')

    def create_widgets(self, widget_name, window, **kwargs):
        match widget_name:
            case "button":
                return ttk.Button(master=window, **kwargs)
            case "label":
                return ttk.Label(master=window, **kwargs)
            case "frame":
                return ttk.Frame(master=window, **kwargs)
            case "scale":
                return ttk.Scale(master=window, **kwargs)

    
    def callbacks(self, dic):
        self.dic = dic
        self.dic["volume"](100)
    
    def open_file(self):
        self.file = filedialog.askopenfilename(
        title="Choose a file",
        filetypes=[
        ("Audio Files", "*.mp3 *.wav"),
        ("All Files", "*.*")
        ]
        )
        if self.file:
            self.dic["open"](self.file)
    
    def on_volume_change(self, value):
        print(self.volume_var.get())
        self.value = int(float(value))
        self.dic["volume"](self.value)
        self.volume_text.set(f'Volume: {self.value}%')


    def run(self):
        top_label =  self.create_widgets("frame", self.window)
        top_label.pack(pady=10)
        play_button = self.create_widgets("button", top_label, text='Play', command=self.dic["play"])
        play_button.pack(side="left",padx=10)
        pause_button = self.create_widgets("button", top_label, text='Pause', command=self.dic["pause"])
        pause_button.pack(side="left",padx=10)
        resume_button = self.create_widgets("button", top_label, text = 'Resume', command=self.dic["resume"])
        resume_button.pack(side = "left", padx=10)
        stop_button = self.create_widgets("button", top_label, text='Stop', command=self.dic["stop"])
        stop_button.pack(side="left",padx=10)
        bottom_label = self.create_widgets("frame", self.window)
        bottom_label.pack(pady=10)
        choose_file = self.create_widgets("button", bottom_label, text="Open File", command=self.open_file)
        choose_file.pack()
        volume_text = self.create_widgets("label", self.window, textvariable=self.volume_text)
        volume_text.pack()
        volume_label = self.create_widgets("label", self.window)
        volume_label.pack()
        volume_slider = self.create_widgets("scale", volume_label, orient="horizontal", from_=0, to=100, length=300, command=self.on_volume_change, variable=self.volume_var)
        volume_slider.pack()
        self.window.mainloop()
    
if __name__ == "__main__":
    gui = GUI()
    gui.run()