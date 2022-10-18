import tkinter as tk


def create_root(width, height):
    root_func = tk.Tk()
    root_func.geometry(f"{width}x{height}")
    root_func.title("Shop")

    return root_func


def create_frame(width, height):
    frame_func = tk.Canvas(
        root,
        width=width,
        height=height,
        bg="black"
    )
    frame_func.pack(padx=0, pady=0, anchor="nw")
    return frame_func


def create_label(text):
    app_title = tk.Label(root, text=text, bg="#FFFF14", font=("Artifakt Element Heavy", 20), fg="black", width=700)
    app_title.pack(padx=0, pady=0)
    return app_title


root = create_root(700, 600)
label = create_label("Welcome to Miro's shop!")
frame = create_frame(700, 600)
