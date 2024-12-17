import tkinter as tk
import random
import time

root = tk.Tk()
root.title("Vizualizare Bubble sort")
canvas_width = 800
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

n = 100
data = [random.randint(5, 100) for _ in range(n)]
bar_width= canvas_width//n

def draw_bars(data, color="blue"):
    canvas.delete("all")
    for i, val in enumerate(data):
        x0 = i * bar_width
        y0 = canvas_height - val * 3
        x1 = (i+1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    root.update_idletasks()

def selection_sort(data, size, step=0):
    if step < size:
        min_idx = step
        for i in range(step+1, size):
            if data[i] < data[min_idx]:
                min_idx = i
        (data[step], data[min_idx]) = (data[min_idx], data[step])
        print(data)
        draw_bars(data, color="pink")
        root.after(80, selection_sort, data, size, step + 1)
    else:
        draw_bars(data, color="purple")

draw_bars(data)
root.after(10, selection_sort, data, n)
root.mainloop()