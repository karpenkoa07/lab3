import string
import tkinter as tk
import random
import pygame

alphabet = string.ascii_uppercase

pygame.mixer.init()
pygame.mixer.music.load("am.mp3")
pygame.mixer.music.play(-1)


def animate():
    for star in stars:
        canvas.move(star, 0, 2)
        x1, y1, x2, y2 = canvas.coords(star)
        if y1 > 500:
            new_x = random.randint(0, 1000)
            canvas.coords(star, new_x, 0, new_x + 2, 2)
    openwindow.after(30, animate)


openwindow = tk.Tk()
openwindow.title("Hello, User!")
openwindow.geometry(f"{1000}x{500}")
openwindow.resizable(False, False)

canvas = tk.Canvas(openwindow, width=1000, height=500, bg="black")
canvas.pack(fill="both", expand=True)

stars = []
for _ in range(100):
    x = random.randint(0, 1000)
    y = random.randint(0, 500)
    star = canvas.create_oval(x, y, x, y, fill="white", outline="")
    stars.append(star)

opentext = tk.Label(
    openwindow,
    text="Dear user, welcome to Among Us Key Generator!",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="black"
)
opentext.place(relx=0.5, rely=0.4, anchor="center")


def close_openwindow():
    openwindow.destroy()

    root = tk.Tk()
    root.geometry("1000x500")
    root.title("WELCOME TO AMONG US KEY ACTIVATOR!")
    root.resizable(False, False)

    def generate_key():
        number = entry_lbl.get()
        if len(number) != 6:
            key_lbl.config(text="YOU ARE AN IMPOSTOR!", bg="red")
            txt_lbl.config(text="Try again! :(", bg="white")
            return
        if not number.isdigit():
            key_lbl.config(text="YOU ARE A SHAPESHIFTER!", bg="red")
            txt_lbl.config(text="Try again! :(", bg="white")
            return

        s = "".join(random.sample(number[3:6], 3) + random.sample(alphabet, 2))
        t = "".join(random.sample(number[0:3], 3) + random.sample(alphabet, 2))
        num1 = int(s[0:3])
        num2 = int(t[0:3])
        block3 = num1 + num2
        key = f"{s}-{t}-{block3}"

        key_lbl.config(text=key, bg="white")
        txt_lbl.config(text="You are a crewmate, here is your key! ;) ")

    bck_picture = tk.PhotoImage(file="sus.png")
    canvas = tk.Canvas(root, width=1000, height=500)
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.create_image(0, 0, image=bck_picture, anchor=tk.NW)

    entry_lbl = tk.Entry(root, font="Times 20 bold")
    canvas.create_window(500, 50, window=entry_lbl)

    button = tk.Button(root, text="GENERATE KEY", command=generate_key)
    canvas.create_window(500, 300, window=button)

    key_lbl = tk.Label(root, text="", font=("Arial", 20))
    canvas.create_window(500, 350, window=key_lbl)

    txt_lbl = tk.Label(root, text="", font=("Arial", 20))
    canvas.create_window(500, 400, window=txt_lbl)

    root.mainloop()


btn = tk.Button(
    openwindow,
    text="Continue",
    command=close_openwindow,
    font=("Arial", 18),
    padx=10,
    pady=5
)
btn.place(relx=0.5, rely=0.6, anchor="center")

animate()
openwindow.mainloop()