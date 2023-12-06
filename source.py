import sqlite3
from math import radians, sin, cos, sqrt, atan2
from pathlib import Path
from tkintermapview import TkinterMapView
# Функція для підключення до бази даних
def connect_to_database():
    documents_path = Path('~').expanduser() / 'Documents'
    bicycle_data_path = documents_path / 'BDP'
    database_path = bicycle_data_path / 'database.db'
    return sqlite3.connect(str(database_path))
# Обрахування дистанції між 2 заданими точками
def calculate_distance(lat1, lon1, lat2, lon2):
    # Радіани широти та довготи для кожної точки
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    # Різниця між довготами та широтами точок
    delta_lon = lon2_rad - lon1_rad
    delta_lat = lat2_rad - lat1_rad

    # Формула гаверсинусів для обчислення відстані
    a = sin(delta_lat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(delta_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371.0 * c  # Радіус Землі у км

    return distance
# Створення посилання на точку в Google Maps
def generate_google_maps_link(latitude, longitude):
    google_maps_link = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
    return google_maps_link
# Пошук найближчих 10 точок в км
def process_user_coordinates(gmap_widget, data_type, latitude, longitude):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute(f"SELECT latitude, longitude FROM {data_type}")
    rows = cursor.fetchall()

    result = f"Введені координати користувача: Latitude = {latitude}, Longitude = {longitude}\n"

    distances = []
    for cords in rows:
        lat, lon = cords
        distance = calculate_distance(latitude, longitude, lat, lon)
        distances.append((lat, lon, distance))

    gmap_widget.delete_all_marker()
    distances.sort(key=lambda x: x[2])

    for idx, item in enumerate(distances[:10], start=1):
        lat, lon, distance = item
        google_maps_link = generate_google_maps_link(lat, lon)
        result += f"{idx}. Відстань між користувачем та точкою ({latitude}, {longitude}) - ({lat}, {lon}): {distance:.2f} км\n"
        result += f"Google Maps Link: {google_maps_link}\n"
        gmap_widget.set_position(lat, lon, marker=True, text=f"{idx}. Distance: {distance:.2f} km")

    conn.close()
    return result
# Вивід інформації про точки
def print_table_data(data_type):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = f"SELECT * FROM {data_type}"

    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()

    result = f"Data from the {data_type} table:\n"
    for row in data:
        result += f"{row}\n"

    return result
# Відсортований вивід від центру міста
def sorted_table_by_center(data_type):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute(f'SELECT latitude, longitude, streets FROM {data_type}')
    rows_with_coords = cursor.fetchall()
    user_lat = 49.8419
    user_lon = 24.0315

    distances = []
    for cords in rows_with_coords:
        latitude, longitude, streets = cords
        distance = calculate_distance(user_lat, user_lon, latitude, longitude)
        distances.append((latitude, longitude, streets, distance))

    distances.sort(key=lambda x: x[3])

    result = f"Bicycle {data_type} sorted by distance to Lviv center:\n"
    for item in distances:
        latitude, longitude, streets, distance = item
        result += f"Latitude: {latitude}, Longitude: {longitude}, Streets: {streets}\n"

    conn.close()
    return result
#математичі дії
def analyze_bicycle_data(data_type):
    conn = connect_to_database()
    cursor = conn.cursor()
    result = ""  # Змінна для зберігання результатів аналізу

    if data_type == 'bicycle_parking':
        cursor.execute('SELECT COUNT(*) FROM bicycle_parking WHERE places IS NULL')
        count_rows_with_none_places_data = cursor.fetchone()[0]
        result += f"Total rows with 'None' data: {count_rows_with_none_places_data}\n"

        cursor.execute('SELECT COUNT(*) FROM bicycle_parking')
        count_rows_data = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM bicycle_parking WHERE places IS NOT NULL')
        count_rows_with_datas = cursor.fetchone()[0]
        result += f"Total parking: {count_rows_data}\n"
        result += f"Total parking with places: {count_rows_with_datas}\n"

        cursor.execute('''SELECT additional_parking FROM bicycle_parking WHERE additional_parking IS NOT NULL''')
        rows = cursor.fetchall()
        total_additional_parking = sum(row[0] for row in rows)
        result += f"Total additional parking: {total_additional_parking}\n"

    elif data_type == 'bicycle_repair_shop':
        cursor.execute('SELECT COUNT(*) FROM bicycle_repair_shop')
        count_rows_data = cursor.fetchone()[0]
        result += f"Total repirs: {count_rows_data}\n"

        cursor.execute('SELECT COUNT(*) FROM bicycle_repair_shop WHERE site IS NOT NULL')
        count_site_data = cursor.fetchone()[0]
        result += f"Total rows with sites: {count_site_data}\n"


    elif data_type == 'bicycle_paths':
        cursor.execute('''SELECT approximate_length FROM bicycle_paths''')
        rows = cursor.fetchall()
        total_length = sum(row[0] for row in rows)
        total_length = round(total_length, 2)
        result += f"Total approximate length of paths: {total_length}\n"

        cursor.execute('SELECT COUNT(*) FROM bicycle_paths')
        count_path_data = cursor.fetchone()[0]
        result += f"Total paths: {count_path_data}\n"

    else:
        result = "Invalid data type provided"

    conn.close()
    return result
#Вигрузка даних з бази даних
def load_data_from_database(data_type):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = f"SELECT * FROM {data_type}"

    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()
    return data
