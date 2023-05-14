from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\guiproject\adhamcycle\loginadham\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x832")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1z.png"))
image_1 = canvas.create_image(
    640.0,
    416.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2z.png"))
image_2 = canvas.create_image(
    632.0,
    423.0,
    image=image_image_2
)

canvas.create_text(
    399.0,
    491.0,
    anchor="nw",
    text="Your password",
    fill="#666666",
    font=("Poppins Regular", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1z.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=398.1307373046875,
    y=642.454833984375,
    width=467.0735778808594,
    height=56.401336669921875
)

canvas.create_text(
    399.0,
    376.0,
    anchor="nw",
    text="Your email",
    fill="#666666",
    font=("Poppins Regular", 16 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3z.png"))
image_3 = canvas.create_image(
    629.0,
    112.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1z.png"))
entry_bg_1 = canvas.create_image(
    632.0,
    438.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=409.0,
    y=414.0,
    width=446.0,
    height=46.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2z.png"))
entry_bg_2 = canvas.create_image(
    634.5,
    553.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=411.0,
    y=528.0,
    width=447.0,
    height=48.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4z.png"))
image_4 = canvas.create_image(
    628.0,
    265.0,
    image=image_image_4
)
window.resizable(False, False)
window.mainloop()
