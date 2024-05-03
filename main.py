import argparse
import csv

from lyricsgenius import Genius


def get_lyrics(artists, output_file, token):

    headers = ["artist", "title", "lyrics", "album"]

    with open(output_file, "w", newline="") as file:

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
