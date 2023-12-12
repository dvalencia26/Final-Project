import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import metadata_extractor as meta_extrac
import os
from PIL import Image, ImageTk


def get_directory_and_folder_name(directory_path, folder_name):
    destination_path = os.path.join(directory_path, str(folder_name))
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    return destination_path


def ask_destination():
    destination_folder = filedialog.askdirectory(title="Select Destination Folder")
    if destination_folder:
        new_folder_name = tk.simpledialog.askstring("Folder Name", "Enter name of the new folder: ")
        if new_folder_name:
            path = get_directory_and_folder_name(destination_folder, new_folder_name)
            messagebox.showinfo("Organize Pictures", "Great! Now let's select the images you want to organize.")
            select_images(path)


def select_images(path):
    selected_files = filedialog.askopenfilenames(title="Select Images", filetypes=(("Image files", "*.jpg;*.jpeg"), ("All files", "*.*")))
    if selected_files:
        success = meta_extrac.extract_metadata(path, selected_files)  # Pass the directory for processing
        print("output: ", success)
        if success:
            messagebox.showinfo("Process Finished", "Photo organization was successful!")
        else:
            messagebox.showerror("Process Finished", "Photo organization failed.")


def main():
    root = tk.Tk()
    root.geometry("500x250")
    root.title("Photo Organizer")

    # Load the background image
    image_path = "../Final_Project/Pillow/hydrapapers-1024x727.jpg"
    background_image = Image.open(image_path)  # Replace with your image path
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label with the background image
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire window

    label_font = ("Arial", 20, "bold")
    label = tk.Label(root, text="Welcome to the Photo Organizer", font=label_font)
    label.pack(pady=50)

    instruction_label = tk.Label(root, text="Where would you like to store your organized pictures? ", font=("Arial", 12))
    instruction_label.pack(padx=30, pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack()

    destination_button = tk.Button(button_frame, text="Select Destination", command=ask_destination)
    destination_button.pack(padx=30, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
