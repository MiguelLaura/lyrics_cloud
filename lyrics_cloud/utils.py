# =============================================================================
# Utility functions
# =============================================================================
#

import re

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


CHORUS_RE = re.compile(r"\[(pre-)?chorus]\n")
EMBED_RE = re.compile(r"[0-9]*embed")
NON_LYRICS_RE = re.compile(r"[0-9]* contributors.*lyrics")
VERSE_RE = re.compile(r"\[verse [0-9]*]\n")


def clean_lyrics(lyrics):
    """
    Function to clean the lyrics.

    Args:
        lyrics (str): lyrics of a song.
    Returns:
        str: cleaned lyrics.
    """

    lyrics = lyrics.lower()
    lyrics = CHORUS_RE.sub("", lyrics)
    lyrics = EMBED_RE.sub("", lyrics)
    lyrics = NON_LYRICS_RE.sub("", lyrics)
    lyrics = VERSE_RE.sub("", lyrics)

    return lyrics


def prepare_text(text):
    """
    Function to prepare the text (remove stop words, punctuation, etc.).

    Args:
        text (str): text to prepare.
    Returns:
        str: cleaned and tokenized text.
    """

    text = text.lower()

    text = clean_lyrics(text)

    # Remove stop words
    text = text.split()
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops]
    text = " ".join(text)

    # Function for removing punctuation
    tokenizer = RegexpTokenizer(r"\w+")
    text = tokenizer.tokenize(text)
    text = " ".join(text)

    return text
