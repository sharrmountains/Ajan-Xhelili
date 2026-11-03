import tkinter as tk

window = tk.Tk()
window.title("Area Calculator")
window.geometry("400x450")

title = tk.Label(window, text="Area Calculator",
                 font=("Arial", 22))
title.pack(pady=15)

shape = tk.StringVar()
shape.set("Rectangle")


def calculate():
 
        gjatesia = float(length.get())
        gjeresi = float(width.get())

        if shape.get() == "Square":
            area = gjatesia * gjatesia  
            result.config(text=str(area) + " m²")

        elif shape.get() == "Rectangle":
            area = gjatesia * gjeresi
            result.config(text=str(area) + " m²")

        else:
            area = gjatesia * gjeresi / 2
            result.config(text=str(area) + " m²")



def square():
    shape.set("Square")

    square_button.config(bg="lightblue")
    rectangle_button.config(bg="SystemButtonFace")
    triangle_button.config(bg="SystemButtonFace")


def rectangle():
    shape.set("Rectangle")

    square_button.config(bg="SystemButtonFace")
    rectangle_button.config(bg="lightblue")
    triangle_button.config(bg="SystemButtonFace")


def triangle():
    shape.set("Triangle")

    square_button.config(bg="SystemButtonFace")
    rectangle_button.config(bg="SystemButtonFace")
    triangle_button.config(bg="lightblue")


tk.Label(window, text="Choose a shape:").pack()

square_button = tk.Button(
    window,
    text="Square",
    command=square
)
square_button.pack(pady=4)

rectangle_button = tk.Button(
    window,
    text="Rectangle",
    command=rectangle
)
rectangle_button.pack(pady=4)

triangle_button = tk.Button(
    window,
    text="Triangle",
    command=triangle
)
triangle_button.pack(pady=4)


tk.Label(
    window,
    text="Add the two values to calculate the area in m²"
).pack(pady=8)


tk.Label(window, text="Length:").pack(pady=5)

length = tk.Entry(window)
length.pack()


tk.Label(window, text="Width:").pack(pady=5)

width = tk.Entry(window)
width.pack()


tk.Button(
    window,
    text="Calculate",
    command=calculate
).pack(pady=10)


result = tk.Label(
    window,
    text="",
    font=("Arial", 20)
)
result.pack(pady=10)

#ajan xhelili

window.mainloop()