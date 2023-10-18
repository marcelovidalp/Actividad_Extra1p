from tkinter import *
from tkinter import messagebox
import time

sorted_list = None

def barras(arr, canvas):
    if not arr:
        return
    max_height = max(arr)
    canvas.delete("all")
    bar_width = 15

    for i, num in enumerate(arr):
        bar_height = (num / max_height) * 250
        x1 = i * (bar_width)
        y1 = 350 - bar_height
        x2 = x1 + bar_width
        y2 = 350

        canvas.create_rectangle(x1, y1, x2, y2, fill="black")
        canvas.create_text(x1 + bar_width/2, y2 + 10, text=str(num))

def mergeSort(arr, canvas):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left, canvas)
        mergeSort(right, canvas)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        barras(arr, canvas)
        canvas.update()
        time.sleep(1)

def binarySearch(arr, target, canvas):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        barras(arr, canvas)
        canvas.update()
        time.sleep(1)

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    
    return -1

def start_merge_sort(entry_arr, canvas):
    global sorted_list
    user_input = entry_arr.get()     

    if not user_input:
        messagebox.showinfo("Error", "Debe ingresar numeros separados por espacios.")
        return
    
    try:
        arr = [int(x) for x in user_input.split()]
    except ValueError:
        messagebox.showinfo("Error", "Debe ingresar numeros enteros separados por espacios.")
        return

    barras(arr, canvas)
    mergeSort(arr, canvas)
    sorted_list = arr

def start_binarySearch(entry_search, canvas):
    global sorted_list
    if sorted_list is None:
        messagebox.showinfo("Error", "Primero debe ordenar la lista.")
        return

    try:
        target = int(entry_search.get())
    except ValueError:
        messagebox.showinfo("Error", "Debe ingresar un numero entero para buscarlo.")
        return
        
    index = binarySearch(sorted_list, target, canvas)

    if index != -1:
        messagebox.showinfo("Resultado", f"El numero {target} fue encontrado en el indice {index}.")
    else :
        messagebox.showinfo("Resultado", f"El numero {target} no fue encontrado en la lista.")

def main():
    ventana = Tk()
    ventana.title("Interfaz de Ordenamiento y Busqueda de elementos.")
    ventana.geometry("1000x700")

    frame1 = Frame(ventana, 
                   width=180, 
                   height=700, 
                   bg="dark slate blue")
    frame1.pack_propagate(False)
    frame1.pack() 
    frame1.place(x=0, y=0)

    entry_sort = Entry(frame1, width=19)
    entry_sort.pack()
    entry_sort.place(x=53, y=100)

    entry_search = Entry(frame1, width=19)
    entry_search.pack()
    entry_search.place(x=53, y=160)

    canvas = Canvas(ventana, 
                    width=800, 
                    height=400)
    canvas.pack(side=RIGHT)

    button_sort = Button(frame1, 
                         text= "Ordenar",
                         command=lambda: start_merge_sort(entry_sort, canvas))
    button_sort.pack()
    button_sort.place(x=0, y=100)

    button_search = Button(frame1, 
                           text= "Buscar", 
                           command=lambda: start_binarySearch(entry_search, canvas))
    button_search.pack()
    button_search.place(x=0, y=160)

    sort_label = Label(frame1, 
                       text="ORDENAMIENTO POR MEZCLA",
                       bg="dark slate blue")
    sort_label.pack()
    sort_label.place(x=0, y=75)

    search_label = Label(frame1, 
                       text="BUSQUEDA BINARIA",
                       bg="dark slate blue")
    search_label.pack()
    search_label.place(x=0, y=135)

    ventana.resizable(False, True)
    ventana.resizable(True, False)

    ventana.mainloop()

main()
