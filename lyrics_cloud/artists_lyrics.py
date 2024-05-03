# =============================================================================
# Script to get lyrics from a list of artists
# =============================================================================
#

import argparse
import csv
import re

from lyricsgenius import Genius


NON_LYRICS_RE = re.compile(r"{0-9}* Contributors.*Lyrics")


def get_lyrics(artists, output_file, token):
    """
    Function to write lyrics from a list of artists into a csv file.

    Args:
        artists (list[str]): list of artists name.
        output_file (str): name of the output image (csv format).
        token (str): token for the genius API (https://docs.genius.com/).
    """

    headers = ["artist", "title", "lyrics"]

    with open(output_file, "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerow(headers)

        genius = Genius(token, verbose=False, skip_non_songs=True)

        for name in artists:
            artist = genius.search_artist(name, sort="title")

            for song in artist.songs:
                lyrics = NON_LYRICS_RE.sub(lyrics)
                row = [name, song.title, lyrics]
                writer.writerow(row)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--artists", required=True, help="List of artists")
    parser.add_argument(
        "--output-file", required=True, help="Csv file to write the results"
    )
    parser.add_argument(
        "--token",
        required=True,
        help="Token for the genius API (https://docs.genius.com/)",
    )
    args = parser.parse_args()

    artists = args.artists.split(",")
    output_file = args.output_file
    token = args.token

    get_lyrics(artists, output_file, token)
