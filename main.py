import argparse
import csv

from lyricsgenius import Genius


def get_lyrics(token, artists):

    headers = ["artist", "title", "lyrics", "album"]

    with open("lyrics.csv", "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerow(headers)

        genius = Genius(token, verbose=False, skip_non_songs=True)

        for name in artists:
            artist = genius.search_artist(name, sort="title")

            for song in artist.songs:
                row = [song.artist_names, song.title, song.lyrics, song.album.name]
                writer.writerow(row)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--token",
        required=True,
        help="Token for the genius API (https://docs.genius.com/)",
    )
    parser.add_argument("--artists", required=True, help="List of artists")
    args = parser.parse_args()

    token = args.token
    artists = args.artists.split(",")

    get_lyrics(token, artists)
