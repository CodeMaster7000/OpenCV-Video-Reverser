import cv2
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Video Reverser")
title_label = Label(root, fg="black", text="Video Reverser", font=("Arial", 40))
title_label.pack()
blank_label = Label(root, text="")
blank_label.pack()
location_e = Entry(root, width=100, borderwidth=5)
location_e.pack()

def execute():
    video_path = location_e.get()
    try:
        vid = cv2.VideoCapture(video_path)

        if not vid.isOpened():
            raise FileNotFoundError("Could not open video file: please check path.")

        frame_list = []

        check, video = vid.read()

        if video is None:
            raise ValueError("Unable to read the video file: it may be empty or corrupted.")
          
        while check:
            frame_list.append(video)
            check, video = vid.read()

        if not frame_list:
            raise ValueError("No frames were extracted from the video. Video might be corrupted.")

        frame_list.pop()
        frame_list.reverse()

        for frame in frame_list:
            cv2.imshow("Reversed Video", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        vid.release()
        cv2.destroyAllWindows()

    except FileNotFoundError as fnf_error:
        messagebox.showerror("File Not Found", str(fnf_error))
    except ValueError as val_error:
        messagebox.showerror("Video Error", str(val_error))
    except Exception as e:
        messagebox.showerror("Unknown Error", f"An unexpected error occurred: {str(e)}")

location_e.insert(0, "Enter the video path you wish to reverse:")

location_button = Button(root, text="Enter", command=execute)
location_button.pack()

root.mainloop()
