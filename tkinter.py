
import tkinter as tk

root = tk.Tk()
root.title("Simple GUI")
root.geometry("400x300")

label = tk.Label(root, text="Welcome to Python GUI")
label.pack(pady=10)

name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

def greet():
    name = name_entry.get()
    result.config(text="Hello, " + name + "!")

button = tk.Button(root, text="Submit", command=greet)
button.pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()
