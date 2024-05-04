# =============================================================================
# Utility functions
# =============================================================================
#

import re


CHORUS_RE = re.compile(r"\[(Pre-)?Chorus]\n")
NON_LYRICS_RE = re.compile(r"[0-9]* Contributors.*Lyrics")
VERSE_RE = re.compile(r"\[Verse [0-9]*]\n")


def clean_lyrics(lyrics):
    """
    Function to clean the lyrics.

    Args:
        lyrics (str): lyrics of a song.
    """

    lyrics = lyrics.lower()
    lyrics = CHORUS_RE.sub("", lyrics)
    lyrics = NON_LYRICS_RE.sub("", lyrics)
    lyrics = VERSE_RE.sub("", lyrics)

    return lyrics
