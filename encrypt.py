import cv2
import os
from tkinter import filedialog, simpledialog, messagebox

def encrypt():
    file_path = filedialog.askopenfilename(title="Select an Image")
    if not file_path:
        return

    img = cv2.imread(file_path)
    if img is None:
        messagebox.showerror("Error", "Invalid Image File")
        return

    msg = simpledialog.askstring("Input", "Enter secret message:")
    password = simpledialog.askstring("Input", "Enter a passcode:", show='*')

    if not msg or not password:
        messagebox.showerror("Error", "Message and passcode cannot be empty")
        return

    msg += "###"  # Unique delimiter to mark end of message
    msg_ascii = [ord(ch) for ch in msg]

    n, m, z = 0, 0, 0

    for value in msg_ascii:
        img[n, m, z] = value  # Store ASCII value directly
        z += 1
        if z == 3:
            z = 0
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1

    encrypted_path = "encryptedImage.png"  # PNG avoids compression artifacts
    cv2.imwrite(encrypted_path, img)
    os.system(f"start {encrypted_path}")
    messagebox.showinfo("Success", "Image encrypted and saved as encryptedImage.png")