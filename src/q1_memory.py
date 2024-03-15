import json
from memory_profiler import profile
from collections import defaultdict
from datetime import datetime

@profile
def q1_memory(file_path):
    # Crear un diccionario para almacenar el recuento de tweets por fecha
    tweet_counts_by_date = defaultdict(int)

    # Crear un diccionario para almacenar el usuario con más publicaciones por fecha
    top_users_by_date = defaultdict(lambda: defaultdict(int))

    # Leer el archivo JSON línea por línea
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            tweet_date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S+00:00').date()
            tweet_counts_by_date[tweet_date] += 1
            # Actualizar el usuario con más publicaciones para esta fecha si es necesario
            username = tweet['user']['username']
            top_users_by_date[tweet_date][username] += 1

    # Obtener las top 10 fechas y los usuarios con más publicaciones para cada una de ellas
    top_10_dates_with_users = []
    for date, _ in sorted(tweet_counts_by_date.items(), key=lambda x: x[1], reverse=True)[:10]:
        top_users = top_users_by_date[date]
        top_user = max(top_users, key=top_users.get)
        top_10_dates_with_users.append((date, top_user))

    return top_10_dates_with_users