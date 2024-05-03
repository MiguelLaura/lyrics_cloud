# lyrics_cloud

Trying things with music lyrics.

Scrape lyrics (either scrape of from json) and
+ create word cloud from them
+ color determined from the color palete of the song images
+ recommender system based on the lyrics

## How to install it

You need to set a python environment. Then, in your shell, type:

 ```bash
 git clone git@github.com:MiguelLaura/lyrics_cloud.git
 cd picross
 pip install .
 ```

## Contributing

To install the Git hooks:
```bash
pre-commit install
```

Before committing, `black` and [generate_readme.py](script/generate_readme.py) will automatically run.

## Usage

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
