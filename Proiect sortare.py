import tkinter as tk
import random
import time

root = tk.Tk()
root.title("Vizualizare Sort")
canvas_width = 800
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

n = 100
data = [random.randint(5, 100) for _ in range(n)]
bar_width = canvas_width // n
sorting = False
algorithm = ""
speed = 50

def draw_bars(data, color="blue"):
    canvas.delete("all")
    for i, val in enumerate(data):
        x0 = i * bar_width
        y0 = canvas_height - val * 3
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    root.update_idletasks()

def bubble_sort(data, i, j):
    global sorting, speed
    if not sorting:
        return
    if data[j] > data[j + 1]:
        data[j], data[j + 1] = data[j + 1], data[j]
        draw_bars(data, color="blue")
    if j < len(data) - i - 2:
        root.after(speed, bubble_sort, data, i, j + 1)
    elif i < len(data) - 1:
        root.after(speed, bubble_sort, data, i + 1, 0)
    else:
        draw_bars(data, color="pink")
        sorting = False

def selection_sort(data, size, step=0):
    global sorting, speed
    if not sorting:
        return
    if step < size:
        min_idx = step
        for i in range(step + 1, size):
            if data[i] < data[min_idx]:
                min_idx = i
        (data[step], data[min_idx]) = (data[min_idx], data[step])
        draw_bars(data, color="purple")
        root.after(speed, selection_sort, data, size, step + 1)
    else:
        draw_bars(data, color="pink")
        sorting = False

def stupid_sort():
    global data, sorting, speed
    if is_sorted(data):
        sorting = False
        return
    draw_bars(data, color="green")
    i, j = random.sample(range(len(data)), 2)
    data[i], data[j] = data[j], data[i]
    draw_bars(data)
    if sorting:
        root.after(speed, stupid_sort)
    draw_bars(data, color="pink")

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def stalin_sort(data, index=1, removed_elements=[]):
    global sorting, speed
    if not sorting:
        return
    if index >= len(data):
        draw_bars(data, color="red")
        sorting = False
        return
    if data[index] >= data[index - 1]:
        draw_bars(data, color="yellow")
        root.after(speed, stalin_sort, data, index + 1, removed_elements)
    else:
        removed_elements.append(data.pop(index))  # Directly remove the element
        draw_bars(data, color="pink")
        root.after(speed, stalin_sort, data, index, removed_elements)



def insertion_sort(data, index=1):
    global sorting, speed
    if not sorting:
        return
    if index >= len(data):
        draw_bars(data, color="pink")
        sorting = False
        return
    current_value = data[index]
    position = index
    while position > 0 and data[position - 1] > current_value:
        data[position] = data[position - 1]
        position -= 1
    data[position] = current_value
    draw_bars(data, color="yellow")
    root.after(speed, insertion_sort, data, index + 1)


def start_sorting():
    global sorting, algorithm
    selected_algorithm = algorithm_var.get()
    if selected_algorithm == "Bubble Sort":
        start_bubble_sort()
    elif selected_algorithm == "Selection Sort":
        start_selection_sort()
    elif selected_algorithm == "Stupid Sort":
        start_stupid_sort()
    elif selected_algorithm == "Stalin Sort":
        start_stalin_sorting()
    elif selected_algorithm == "Insertion Sort":
        start_insertion_sort()

def start_bubble_sort():
    global sorting, algorithm
    sorting = True
    algorithm = "bubble"
    bubble_sort(data, 0, 0)

def start_selection_sort():
    global sorting, algorithm
    sorting = True
    algorithm = "selection"
    selection_sort(data, len(data))

def start_stupid_sort():
    global sorting
    algorithm = "stupid"
    if not sorting:
        sorting = True
        stupid_sort()

def start_stalin_sorting():
    global sorting
    sorting = True
    algorithm = "stalin"
    draw_bars(data)
    root.after(10, stalin_sort, data)

def start_insertion_sort():
    global sorting
    sorting = True
    algorithm = "insertion"
    draw_bars(data)
    root.after(10, insertion_sort, data)

def stop_sort():
    global sorting
    sorting = False

def reset_data():
    global data, sorting
    sorting = False
    data = [random.randint(5, 100) for _ in range(n)]
    draw_bars(data)

def update_num_elements(val):
    global n, data
    n = int(val)
    data = [random.randint(5, 100) for _ in range(n)]
    draw_bars(data)

def update_speed(val):
    global speed
    speed = int(val)

def generate_new_values():
    global data
    data = [random.randint(5, 100) for _ in range(n)]
    draw_bars(data)

def close_app():
    root.quit()

algorithm_var = tk.StringVar(root)
algorithm_var.set("Select Sorting Algorithm")
algorithm_menu = tk.OptionMenu(root, algorithm_var, "Bubble Sort", "Selection Sort", "Stupid Sort", "Stalin Sort", "Insertion Sort")
algorithm_menu.pack(side=tk.LEFT, padx=10)


start_button = tk.Button(root, text="Start Sorting", command=start_sorting)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(root, text="Stop Sorting", command=stop_sort)
stop_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(root, text="Reset", command=reset_data)
reset_button.pack(side=tk.LEFT, padx=10)

new_values_button = tk.Button(root, text="Generate New Values", command=generate_new_values)
new_values_button.pack(side=tk.LEFT, padx=10)

num_elements_label = tk.Label(root, text="Number of elements:")
num_elements_label.pack(side=tk.LEFT, padx=10)

num_elements_scale = tk.Scale(root, from_=5, to=100, orient="horizontal", command=update_num_elements)
num_elements_scale.set(n)  # Set the default value to 100
num_elements_scale.pack(side=tk.LEFT, padx=10)


speed_label = tk.Label(root, text="Sorting Speed:")
speed_label.pack(side=tk.LEFT, padx=10)

speed_scale = tk.Scale(root, from_=1, to_=100, orient="horizontal", command=update_speed)
speed_scale.set(speed)  # Set the default speed to 50
speed_scale.pack(side=tk.LEFT, padx=10)

close_button = tk.Button(root, text="Close", command=close_app)
close_button.pack(side=tk.LEFT, padx=10)

draw_bars(data)
root.mainloop()
