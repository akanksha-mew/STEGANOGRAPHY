import tkinter as tk
from encrypt import encrypt
from decrypt import decrypt

# GUI Setup
root = tk.Tk()
root.title("Image Steganography")
root.geometry("300x200")

tk.Button(root, text="Encrypt Message", command=encrypt).pack(pady=10)
tk.Button(root, text="Decrypt Message", command=decrypt).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
