import tkinter as tk
from tkintermapview import TkinterMapView
from source import process_user_coordinates, print_table_data, sorted_table_by_center, Path, analyze_bicycle_data
import os

#Кнопкі...

def process_map_click(event):
    x, y = event.x, event.y
    lon, lat = gmap_widget.pixel_to_lonlat(x, y)  # Перетворення позиції курсора на координати на мапі

    # Оновлення значень глобальних змінних для Latitude та Longitude
    latitude_value.set(str(lat))
    longitude_value.set(str(lon))
def display_result(result):
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# Функція для обробки координат
def process_coordinates():
    selected_data = dropdown.get()
    latitude_str = latitude_value.get()
    longitude_str = longitude_value.get()

    if latitude_str and longitude_str:  # Перевірка наявності значень
        latitude = float(latitude_str)
        longitude = float(longitude_str)
        result = process_user_coordinates(gmap_widget, selected_data, latitude, longitude)
        display_result(result)
    else:
        display_result("Please enter Latitude and Longitude values.")

# Функція для виведення даних
def print_data():
    selected_data = dropdown.get()
    result = print_table_data(selected_data)
    display_result(result)

# Функція для аналізу даних
def analyze_data():
    selected_data = dropdown.get()
    result = analyze_bicycle_data(selected_data)  # Тут викликаємо відповідну функцію
    display_result(result)

# Функція для сортування даних
def sort_data():
    selected_data = dropdown.get()
    result = sorted_table_by_center(selected_data)
    display_result(result)


root = tk.Tk()  # Початок вікна
root.title("Bicycle Processing")  # Назва вікна

latitude_value = tk.StringVar()
longitude_value = tk.StringVar()

# Ініціалізація віджету для карт Google Maps
initial_latitude = 49.8397
initial_longitude = 24.0297

gmap_widget = TkinterMapView(root, height=300)
gmap_widget.pack(fill="both")
gmap_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=20)
gmap_widget.set_position(initial_latitude, initial_longitude)
gmap_widget.set_zoom(12)

# Додавання обробника кліку на мапі
gmap_widget.bind("<Button-1>", process_map_click)

# Шлях до вашої іконки
documents_path = Path(os.path.expanduser('~')) / 'Documents'
bicycle_data_path = documents_path / 'BDP'
icon_path = bicycle_data_path / 'bike-svgrepo-com.ico'
root.iconbitmap(default=icon_path)

# Ввід довжини...
label_lat = tk.Label(root, text="Latitude:")
label_lat.pack()
entry_lat = tk.Entry(root, textvariable=latitude_value)
entry_lat.pack()

# Ввід довжини...
label_lon = tk.Label(root, text="Longitude:")
label_lon.pack()
entry_lon = tk.Entry(root, textvariable=longitude_value)
entry_lon.pack()

# Кнопка для обробки координат
button_process = tk.Button(root, text="Process Coordinates", command=process_coordinates)
button_process.pack()

# Вибірка...
options = [
    "bicycle_paths",
    "bicycle_parking",
    "bicycle_repair_shop"
]
dropdown = tk.StringVar(root)
dropdown.set(options[0])
menu = tk.OptionMenu(root, dropdown, *options)
menu.pack()

# Кнопка для виведення даних
button_print = tk.Button(root, text="Print Data", command=print_data)
button_print.pack()

# Кнопка для аналізу даних
button_analyze = tk.Button(root, text="Analyze Data", command=analyze_data)
button_analyze.pack()

# Кнопка для сортування даних
button_sort = tk.Button(root, text="Sort Data", command=sort_data)
button_sort.pack()

# Поле для виведення результатів
result_text = tk.Text(root, height=8, width=150)
result_text.pack()

root.geometry("600x600")  # Розмір вікна
root.mainloop()  # Кінець роботи з вікном
