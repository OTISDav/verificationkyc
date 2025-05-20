import unicodedata
import re


def normalize_text(text: str) -> str:
    # Supprimer les accents
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore').decode('utf-8')

    # Convertir en minuscule
    text = text.lower()

    # Supprimer tous les caractères non-alphanumériques
    text = re.sub(r'[^a-z0-9]', '', text)

    return text
