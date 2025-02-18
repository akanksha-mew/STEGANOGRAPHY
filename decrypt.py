import cv2
from tkinter import filedialog, simpledialog, messagebox

def decrypt():
    file_path = filedialog.askopenfilename(title="Select an Encrypted Image")
    if not file_path:
        return

    img = cv2.imread(file_path)
    if img is None:
        messagebox.showerror("Error", "Invalid Image File")
        return

    pas = simpledialog.askstring("Input", "Enter passcode for Decryption:", show='*')
    original_password = simpledialog.askstring("Input", "Re-enter the original passcode:", show='*')

    if pas != original_password:
        messagebox.showerror("Error", "Incorrect passcode")
        return

    message = ""
    n, m, z = 0, 0, 0

    while True:
        char_value = img[n, m, z]
        message += chr(char_value)

        if message.endswith("###"):  # Stop reading when delimiter is reached
            message = message[:-3]  # Remove the delimiter
            break

        z += 1
        if z == 3:
            z = 0
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1

    messagebox.showinfo("Decrypted Message", f"Decryption Message: {message}")