# Import necessary libraries
from tkinter import *
from pytube import YouTube
from tkinter import messagebox
import validators


# Function to download a YouTube video
def download_video():
    """
    This function downloads a YouTube video based on the URL entered by the user and the selected resolution.
    """
    # Get the URL from the entry field
    video_url = url_entry.get()

    # Check if the entered URL is valid
    if validators.url(video_url):
        # Get the selected resolution from the dropdown menu
        selected_resolution = resolution_var.get()
        try:
            # Create a YouTube object
            yt = YouTube(video_url)

            # Filter available streams by resolution and get the first one
            stream = yt.streams.filter(res=selected_resolution).first()

            # Check if a stream is found for the selected resolution
            if stream:
                # Download the video
                stream.download()

                # Show success message
                messagebox.showinfo("Success", "Video Downloaded Successfully")
            else:
                # Show error message if no video is found for the selected resolution
                messagebox.showerror("Error", "No video found for the selected resolution")
        except Exception as e:
            # Show error message if an exception occurs during the download process
            messagebox.showerror("Error", f"An error occurred {e}")
    else:
        # Show error message for invalid URL
        messagebox.showerror("Error", "Please Enter a valid URL")


# Create the Tkinter application window
app = Tk()
app.geometry("500x300")
app.title("Youtube Downloader")

# Title label for the application
title_label = Label(app, text="Youtube Downloader", font=("Helvetica", 20))
title_label.pack(pady=10)

# Label prompting the user to enter the URL
url_label = Label(app, text="Please enter your URL: ", font=("Helvetica", 12))
url_label.pack(pady=10)

# Entry field for the URL
url_entry = Entry(app, width=40, borderwidth=3, relief=GROOVE)
url_entry.pack()

# Variable to store the selected resolution
resolution_var = StringVar(app)
resolutions = ["1080p", "720p", "480p", "360p", "240p", "144p"]  # Available resolutions
resolution_var.set("720p")  # Default resolution
resolution_menu = OptionMenu(app, resolution_var, *resolutions)
resolution_menu.pack(pady=20)

# Button to trigger the download process
download_button = Button(app, text="Download", font=("Helvetica", 12), borderwidth=2, relief=GROOVE,
                         command=download_video)
download_button.pack(pady=20)

# Label for developer info
developer_label = Label(app, text="Made by Ilia keshavarz", font=("arial", 10, "bold"), fg="#212121")
developer_label.pack()

# Run the Tkinter event loop
app.mainloop()
