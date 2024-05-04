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

You must download Google's pre-trained word2vec vectors [here](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g).

* [Functions](#functions)
  * [get_lyrics](#get_lyrics)

---

### Functions

#### get_lyrics

Function to write lyrics from a list of artists into a csv file.

*Arguments*

* **artists** *list[str]* - list of artists name.
* **output_file** *str* - name of the output image (csv format).
* **token** *str* - token for the genius API (https://docs.genius.com/).
