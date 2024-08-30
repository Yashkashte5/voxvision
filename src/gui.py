import tkinter as tk
from voice_recognition import recognize_speech
from text_to_speech import speak

def on_button_click():
    command = recognize_speech()
    if command:
        speak(f"You said: {command}")

root = tk.Tk()
root.title("VoxVision")

button = tk.Button(root, text="Start", command=on_button_click)
button.pack(pady=20)

root.mainloop()
