# =============================================================================
# Script to get lyrics from a list of artists
# =============================================================================
#

import argparse
import csv

from lyricsgenius import Genius
from tqdm import tqdm

from lyrics_cloud.utils import clean_lyrics


def get_artists_from_file(file):
    """
    Function to get artists from a txt file.

    Args:
        file (str): name of the input file (txt format).
    Yields:
        str: artist's name.
    """
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            yield line


def get_lyrics(artists, output_file, token):
    """
    Function to write lyrics from a list of artists into a csv file.

    Args:
        artists (list[str]): list of artists name.
        output_file (str): name of the output file (csv format).
        token (str): token for the genius API (https://docs.genius.com/).
    """
    headers = ["artist", "title", "lyrics"]

    with open(output_file, "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerow(headers)

        genius = Genius(token, verbose=False, skip_non_songs=True, retries=3)

        for name in tqdm(
            artists,
            total=(len(artists) if type(artists) == list else None),
            desc="Number of artists",
            position=0,
        ):
            name = name.lower()
            artist_songs = genius.search_artist(name, sort="title").songs

            for song in tqdm(
                artist_songs,
                total=len(artist_songs),
                desc="Number of songs for the artist {}".format(name),
                position=1,
            ):
                lyrics = clean_lyrics(song.lyrics)
                title = song.title.lower()
                row = [name, title, lyrics]
                writer.writerow(row)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    action_choices = ["list", "file"]
    parser.add_argument("--method", choices=action_choices, default=action_choices[0])
    parser.add_argument(
        "--artists",
        required=True,
        help="list of artists or text file with one artist per line",
    )
    parser.add_argument(
        "--output-file", required=True, help="csv file to write the results"
    )
    parser.add_argument(
        "--token",
        required=True,
        help="token for the genius API (https://docs.genius.com/)",
    )
    args = parser.parse_args()

    method = args.method
    artists = (
        args.artists.split(",")
        if method == "list"
        else get_artists_from_file(args.artists)
    )
    output_file = args.output_file
    token = args.token

    get_lyrics(artists, output_file, token)
