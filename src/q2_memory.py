import re
import codecs
from collections import Counter
from typing import List, Tuple

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counts = Counter()
    unique_emojis = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            emojis = re.findall(r'\\u[\da-fA-F]{4}', line)  # Encuentra secuencias de escape Unicode de 4 dígitos
            emojis = [codecs.decode(emoji.encode(), 'unicode_escape') for emoji in emojis]  # Decodifica las secuencias de escape Unicode
            for emoji in emojis:
                emoji_counts[emoji] += 1
                unique_emojis.add(emoji)
    sorted_emojis = sorted(unique_emojis, key=lambda x: emoji_counts[x], reverse=True)
    return [(emoji, emoji_counts[emoji]) for emoji in sorted_emojis[:10]]