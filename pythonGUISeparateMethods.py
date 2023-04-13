import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class DesktopApp:

    def __init__(self, master):
        self.master = master
        self.master.title("Photo Uploader")
        self.tall = 600
        self.stretched = 900

        self.create_widgets()

    # call defined methods inside create_widgets method(create_canvas, create_frame, create_label, create_button)
    def create_widgets(self):
        # tall = 600
        # stretched = 900
        # self.create_canvas(tall, stretched)
        self.create_canvas()
        self.create_frame()
        self.create_label()
        self.create_button()

    # Create a canvas
    # def create_canvas(self, tall, stretched):
    def create_canvas(self):
        # self.canvas = tk.Canvas(height=tall, width=stretched)
        self.canvas = tk.Canvas(height=self.tall, width=self.stretched)
        self.canvas.pack()

    # Create a frame
    def create_frame(self):
        self.frame = tk.Frame(self.master, height=150, bg="green", bd=5)
        self.frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    # Create a label
    def create_label(self):
        self.label = tk.Label(self.frame, text="Image to Text converter Desktop app", font=("Arial", 24))
        self.label.place(relx=0.5, rely=0.5, anchor="center")

    # Create the Upload Photo button
    def create_button(self):
        self.button = tk.Button(self.frame, text="Upload Photo", bg="gray", fg="red", height=2, width=20, command=self.upload_photo)
        self.button.pack(side="bottom")
    # When the "Upload Photo" button is clicked, open a file dialog box using the askopenfilename function
    # from the filedialog module of the tkinter library, which allows the user to select a file to upload

    # check image formats, show error pop up in case selecting non image format(f. e. PDF format)
    def upload_photo(self):
        file_path = filedialog.askopenfilename()

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
