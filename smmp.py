import tkinter as tk
from tkinter import filedialog
from tinytag import TinyTag as tnt
import eyed3 as e3
from PIL import Image, ImageTk
import pygame
import io
import os

#insert reference here

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Symmetrical Music Player")
        self.root.geometry("400x155")
        self.root.resizable(True, False)

        self.playing = False
        self.loop = False

        self.song_label = tk.Label(self.root, text="No file loaded")
        self.song_label.pack(anchor="w", padx=10, pady=10)

        self.select_button = tk.Button(self.root, text="Select Song", command=self.select_song)
        self.select_button.pack(anchor="w", padx=10)

        self.play_pause = tk.Button(self.root, text="⏵", command=self.play_music)
        self.play_pause.pack(anchor="w", padx=10)
        
        self.loopcheck = tk.Checkbutton(self.root, text="Loop", command=self.toggleloop)
        self.loopcheck.pack(anchor="w", padx=10)

        self.volume_label = tk.Label(self.root, text="Volume")
        self.volume_label.place(relx=1, anchor="ne")

        self.volume_slider = tk.Scale(self.root, from_=100, to=0, showvalue=True, orient=tk.VERTICAL, command=self.set_volume, cursor="tcross")
        self.volume_slider.place(relx=1, relheight=0.8, rely=0.2, anchor="ne")
        self.volume_slider.set(100)

    def select_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("Audio Files", ".mp3 .wav .ogg .xm .mod .it .s3m .flac")])
        if song_path in [None, ""]:
            return
        try:
            sng = tnt.get(song_path)
            if sng.album != None:
                song_name = f"{sng.album} - {sng.title}"
            else:
                song_name = sng.title
        except:
            song_name = os.path.basename(song_path)
        try:
            sngi = e3.load(song_path)
            print(sngi.tag.images[0].mime_type[6:])
            img = Image.open(io.BytesIO(sngi.tag.images[0].image_data)).resize((128, 128), Image.BOX)
            icon = ImageTk.PhotoImage(image=img, width=128, height=128)
            self.iconc = tk.Label(self.root, width=128, height=128, image=icon)
            self.iconc.image = icon
            self.iconc.place_forget()
            self.iconc.place(anchor="e", relx=1, rely=0.5, x=-56, width=128, height=128)
            self.iconc.lower(self.song_label)
        except:
            self.iconc = tk.Label(self.root, width=128, height=128)
            self.iconc.place_forget()
            self.iconc.place(anchor="e", relx=1, rely=0.5, x=-56, width=128, height=128)
        if song_name == None:
            song_name = os.path.basename(song_path)
        if song_path:
            self.song_label.config(text=song_name)
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
                self.play_pause.configure(text="⏹")
            else:
                pygame.mixer.music.stop()
                self.playing = False
                self.play_pause.configure(text="⏵")

    #def stop_music(self):
    #    if self.playing:
    #        pygame.mixer.music.stop()
    #        self.playing = False

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume) / 100)
    
    def toggleloop(self):
        self.loop = not self.loop

pygame.mixer.init()
root = tk.Tk()
player = MusicPlayer(root)
root.mainloop()