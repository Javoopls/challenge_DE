import re
import codecs
from collections import Counter
from typing import List, Tuple

# Función para optimizar el tiempo de ejecución
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emoji_counts = Counter()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            emojis = re.findall(r'\\u[\da-fA-F]{4}', line)  # Encuentra secuencias de escape Unicode de 4 dígitos
            emojis = [codecs.decode(emoji.encode(), 'unicode_escape') for emoji in emojis]  # Decodifica las secuencias de escape Unicode
            emoji_counts.update(emojis)
    return emoji_counts.most_common(10)