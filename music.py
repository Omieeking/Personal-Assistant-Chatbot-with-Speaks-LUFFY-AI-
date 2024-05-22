import pygame
import streamlit as st
import os
# os.environ['SDL_AUDIODRIVER'] = 'directsound'


# Load songs
songs = [os.path.join(r"C:\Users\Omkar Jadhav\OneDrive\Desktop\Music", f) for f in os.listdir(r"C:\Users\Omkar Jadhav\OneDrive\Desktop\Music") if f.endswith(".mp3")]

# Define a variable to store the index of the currently playing song
current_song = 0

# Play a song
def play_song():
    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()
    return ("playing song")

is_song_paused = False

# Pause a song
def pause_song():
    global is_song_paused
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        is_song_paused = True
        return "Song paused."
    else:
        return "No song is currently playing."

def resume_song():
    global is_song_paused
    if is_song_paused:
        pygame.mixer.music.unpause()
        is_song_paused = False
        return "Song resumed."
    else:
        return "Song is not paused."

def stop_song():
    pygame.mixer.music.stop()
    return ("Song stopped.")

# Stop a song and play the next one
def next_song():
    pygame.mixer.music.stop()
    global current_song
    current_song = (current_song + 1) % len(songs)
    play_song()
    return ("Playing next song")

# Stop a song and play the previous one
def previous_song():
    pygame.mixer.music.stop()
    global current_song
    current_song = (current_song - 1) % len(songs)
    play_song()
    return ("Playing previous song")

# Now you can call these functions from other Python files based on the user command

def user_control(self):
        while True:
            command = input("Enter a command (play, stop, next, prev, exit): ").lower()

            if command == "play":
                self.play_random_music()
            elif command == "stop":
                self.stop_music()
            elif command == "next":
                self.next_song()
            elif command == "prev":
                self.previous_song()
            elif command == "exit":
                self.stop_music()
                break
            else:
                st.subheader("Invalid command. Try again.")

