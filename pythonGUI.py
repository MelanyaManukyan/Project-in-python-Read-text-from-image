import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class DesktopApp:

    def __init__(self, master):
        self.master = master
        self.master.title("Photo Uploader")

        tall = 600
        stretched = 900

        # Created a canvas
        canvas = tk.Canvas(height=tall, width=stretched)
        canvas.pack()

        # Created a frame
        frame = tk.Frame(master, height=150, bg="green", bd=5)
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        # frame.pack()

        label = tk.Label(frame, text="Image to Text converter Desktop app", font=("Arial", 24))
        label.place(relx=0.5, rely=0.5, anchor="center")

        # Created the Upload Photo button
        button = tk.Button(frame, text="Upload Photo", bg="gray", fg="red", height=2, width=20, command=self.upload_photo)
        button.pack(side="bottom")

    # When the "Upload Photo" button is clicked. It opens a file dialog box using the askopenfilename function
    # from the filedialog module of the tkinter library, which allows the user to select a file to upload
    def upload_photo(self):
        file_path = filedialog.askopenfilename()
        # if file_path.endswith("fdsa")
        if file_path.endswith(".png") or file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
            # process the selected file
            pass
        elif file_path.endswith(".gif") or file_path.endswith(".tiff"):
            # process the selected file
            pass
        elif file_path.endswith(".WebP") or file_path.endswith(".BMP"):
            # process the selected file
            pass
        elif file_path.endswith(".HEIF") or file_path.endswith(".SVG"):
            # process the selected file
            pass
        elif file_path.endswith(".CR") or file_path.endswith(".CRW") or file_path.endswith(".Avif"):
            # process the selected file
            pass
        else:
            error_msg = "Please select a correct image format, for example PNG or JPG format file."
            messagebox.showerror("Error", error_msg, parent=self.master)


root = tk.Tk()
app = DesktopApp(root)
root.mainloop()

# app = DesktopApp()
# app.master