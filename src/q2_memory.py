import re
import codecs
from collections import Counter
from typing import List, Tuple

@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Función para encontrar los top 10 emojis más utilizados con su respectivo conteo en los tweets.
    
    Args:
    file_path (str): Ruta del archivo JSON que contiene los tweets.
    
    Returns:
    List[Tuple[str, int]]: Lista de tuplas que contienen el emoji y su respectivo conteo.
    """
    # Inicializar un contador para almacenar la cantidad de emojis
    emoji_counts = Counter()

    # Leer el archivo JSON línea por línea
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Encontrar secuencias de escape Unicode de 4 dígitos (emojis)
            emojis = re.findall(r'\\u[\da-fA-F]{4}', line)
            # Decodificar las secuencias de escape Unicode y contar los emojis
            emojis = [codecs.decode(emoji.encode(), 'unicode_escape') for emoji in emojis]
            emoji_counts.update(emojis)

    # Obtener los top 10 emojis más utilizados
    top_10_emojis = emoji_counts.most_common(10)

    return top_10_emojis