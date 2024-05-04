# lyrics_cloud

Trying things with music lyrics.

## Installation

You need to set a python environment (tested version: 3.10.5). Then, in your shell, type:

 ```bash
 git clone git@github.com:MiguelLaura/lyrics_cloud.git
 cd lyrics_cloud
 pip install .
 ```

## Contributing

To install the Git hooks:
```bash
pre-commit install
```

Before committing, `black` and [generate_readme.py](script/generate_readme.py) will automatically run.

To change the README file, change [README.template.md](README.template.md) first and generate the README after (or let the pre-commit do it). You'll need to add the new functions to [generate_readme.py](script/generate_readme.py) in `DOCS`.

## Usage

### Command line

#### Get the lyrics to artists' songs

```bash
usage: python lyrics_cloud/artists_lyrics.py [-h] --artists ARTISTS --output-file OUTPUT_FILE --token TOKEN

options:
  -h, --help            show this help message and exit
  --artists ARTISTS     list of artists
  --output-file OUTPUT_FILE
                        csv file to write the results
  --token TOKEN         token for the genius API (https://docs.genius.com/)
```

#### Recommender system

```bash
usage: python lyrics_cloud/content_based_recommender.py [-h] --artist ARTIST --csv-file CSV_FILE --title TITLE

options:
  -h, --help           show this help message and exit
  --artist ARTIST      artist singing the song to get recommendations from
  --csv-file CSV_FILE  csv file containing the lyrics
  --title TITLE        song title to get recommendations from
```

{toc}
{docs}