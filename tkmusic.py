import tkinter as tk
from tkinter import filedialog
import pygame
import time
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("400x155")
        self.root.resizable(False, False)

        self.playing = False
        self.loop = False

        self.song_label = tk.Label(self.root, text="No file loaded")
        self.song_label.pack(anchor="w", padx=10, pady=10)

        self.select_button = tk.Button(self.root, text="Select Song", command=self.select_song)
        self.select_button.pack(anchor="w", padx=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(anchor="w", padx=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(anchor="w", padx=10)
        
        self.loopcheck = tk.Checkbutton(self.root, text="Loop", command=self.toggleloop)
        self.loopcheck.pack(anchor="w", padx=10)

        self.volume_label = tk.Label(self.root, text="Volume")
        self.volume_label.place(relx=1, anchor="ne")

        self.volume_slider = tk.Scale(self.root, from_=100, to=0, showvalue=True, orient=tk.VERTICAL, command=self.set_volume, cursor="tcross")
        self.volume_slider.place(relx=1, relheight=0.8, rely=0.2, anchor="ne")
        self.volume_slider.set(100)

    def select_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("Audio Files", ".mp3 .wav .ogg .xm .mod")])
        if song_path:
            self.song_label.config(text="Loaded: " + os.path.basename(song_path))
            self.song_path = song_path
            self.song_length = pygame.mixer.Sound(song_path).get_length()
            pygame.mixer.music.load(self.song_path)

    def play_music(self):
        if hasattr(self, 'song_path'):
            if not self.playing:
                if self.loop:
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.play(0)
                self.playing = True

    def stop_music(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume) / 100)
    
    def toggleloop(self):
        self.loop = not self.loop

pygame.mixer.init()
root = tk.Tk()
player = MusicPlayer(root)
root.mainloop()