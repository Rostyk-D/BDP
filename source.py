
import sqlite3
from math import radians, sin, cos, sqrt, atan2

#Обрахування дистанції між 2 заданими точками.
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
#Створення силкі на точку в Google maps.
def generate_google_maps_link(latitude, longitude):
    # стандартна силка на google maps з заданами координатами
    return f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
#Пошук найблищих 10 дорожок в Км.
def process_user_coordinates(data_type, latitude, longitude):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT latitude, longitude FROM {data_type}")
    rows = cursor.fetchall()

    result = f"Введені координати користувача: Latitude = {latitude}, Longitude = {longitude}\n"

    distances = []
    for cords in rows:
        lat, lon = cords
        distance = calculate_distance(latitude, longitude, lat, lon)
        distances.append((lat, lon, distance))

    distances.sort(key=lambda x: x[2])

    for item in distances[:10]:
        lat, lon, distance = item
        google_maps_link = generate_google_maps_link(lat, lon)
        result += f"Distance between user and point ({latitude}, {longitude}) - ({lat}, {lon}): {distance:.2f} km\n"
        result += f"Google Maps Link: {google_maps_link}\n"

    conn.close()
    return result

def print_table_data(data_type):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM {data_type}"

    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()

    result = f"Data from the {data_type} table:\n"
    for row in data:
        result += f"{row}\n"

    return result

def sorted_table_by_center(data_type):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(f'SELECT latitude, longitude, streets FROM {data_type}')
    rows_with_cords = cursor.fetchall()
    user_lat = 49.8419
    user_lon = 24.0315

    distances = []
    for cords in rows_with_cords:
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

def load_data_from_database(data_type):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM {data_type}"

    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()
    return data

def analyze_bicycle_data(data_type):
    conn = sqlite3.connect('database.db')
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
        result += f"Total rows: {count_rows_data}\n"
        result += f"Total rows with data: {count_rows_with_datas}\n"

        cursor.execute('''SELECT additional_parking FROM bicycle_parking WHERE additional_parking IS NOT NULL''')
        rows = cursor.fetchall()
        total_additional_parking = sum(row[0] for row in rows)
        result += f"Total additional parking: {total_additional_parking}\n"

    elif data_type == 'bicycle_repair_shop':
        cursor.execute('SELECT COUNT(*) FROM bicycle_repair_shop')
        count_rows_data = cursor.fetchone()[0]
        result += f"Total rows: {count_rows_data}\n"

    elif data_type == 'bicycle_paths':
        cursor.execute('''SELECT approximate_length FROM bicycle_paths''')
        rows = cursor.fetchall()
        total_length = sum(row[0] for row in rows)
        total_length = round(total_length, 2)
        result += f"Total approximate length of paths: {total_length}\n"

    else:
        result = "Invalid data type provided"

    conn.close()
    return result