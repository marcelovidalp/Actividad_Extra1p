from tkinter import *
import random
import time

def merge_sort(arr, canvas):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, canvas)
        merge_sort(right_half, canvas)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        draw_bars(arr, canvas)
        canvas.update()
        time.sleep(0.1)

def draw_bars(arr, canvas):
    max_height = max(arr)
    canvas.delete("all")
    bar_width = 20
    spacing = 10

    for i, num in enumerate(arr):
        bar_height = (num / max_height) * 300
        x1 = i * (bar_width + spacing)
        y1 = 300 - bar_height
        x2 = x1 + bar_width
        y2 = 300

        canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
        canvas.create_text(x1 + bar_width/2, y2 + 10, text=str(num))



def start_merge_sort(entry, canvas):
    user_input = entry.get()
    arr = [int(x) for x in user_input.split()]

    draw_bars(arr, canvas)
    merge_sort(arr, canvas)

def main():
    ventana = Tk()
    ventana.title("Interfaz de Ordenamiento y Busqueda de elementos.")

    frame1 = Frame(ventana, width=800, height=100)
    frame1.config(bg="red")
    frame1.pack

    entry_arr = Entry(frame1, width=60)
    entry_arr.pack(side= LEFT)

    canvas = Canvas(ventana, width=800, height=400)
    canvas.pack()

    button = Button(frame1, text= "Ordenar", command=lambda: start_merge_sort(entry_arr, canvas))
    button.pack(side=LEFT)

    ventana.mainloop()
    
main()
