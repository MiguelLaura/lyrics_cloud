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
usage: python -m lyrics_cloud.artists_lyrics [-h] --artists ARTISTS --output-file OUTPUT_FILE --token TOKEN

options:
  -h, --help            show this help message and exit
  --artists ARTISTS     list of artists
  --output-file OUTPUT_FILE
                        csv file to write the results
  --token TOKEN         token for the genius API (https://docs.genius.com/)
```

#### Recommender system

```bash
usage: python -m lyrics_cloud.content_based_recommender [-h] --artist ARTIST --csv-file CSV_FILE --title TITLE

options:
  -h, --help           show this help message and exit
  --artist ARTIST      artist singing the song to get recommendations from
  --csv-file CSV_FILE  csv file containing the lyrics
  --title TITLE        song title to get recommendations from
```

#### Word cloud

```bash
usage: python -m lyrics_cloud.word_cloud [-h] --artist ARTIST --csv-file CSV_FILE --title TITLE

options:
  -h, --help           show this help message and exit
  --artist ARTIST      artist singing the song to get recommendations from
  --csv-file CSV_FILE  csv file containing the lyrics
  --title TITLE        song title to get recommendations from
```

* [Scraper](#scraper)
  * [get_lyrics](#get_lyrics)
* [Recommender](#recommender)
  * [build_recommender_word2vec](#build_recommender_word2vec)
  * [create_avg_word2vec_embeddings](#create_avg_word2vec_embeddings)
  * [recommend_with_word2vec](#recommend_with_word2vec)
  * [visualize_embeddings](#visualize_embeddings)
* [Word cloud](#word-cloud)
  * [generate_word_cloud](#generate_word_cloud)
* [Utils](#utils)
  * [clean_lyrics](#clean_lyrics)
  * [prepare_text](#prepare_text)

---

### Scraper

#### get_lyrics

Function to write lyrics from a list of artists into a csv file.

*Arguments*

* **artists** *list[str]* - list of artists name.
* **output_file** *str* - name of the output image (csv format).
* **token** *str* - token for the genius API (https://docs.genius.com/).

---

### Recommender

#### build_recommender_word2vec

Function to load and train the word2vec model on the corpus.

*Arguments*

* **corpus** *list[list[str]* - corpus of songs.

*Returns*

*model* - trained word2vec model.

#### create_avg_word2vec_embeddings

Function to create the averaged word2vec embeddings.

*Arguments*

* **df_lyrics** *Series* - lyrics.
* **model** - trained word2vec model.

*Returns*

*list[float]* - lyrics averaged word2vec embeddings.

#### recommend_with_word2vec

Function to recommend a song based on a title and artist.

*Arguments*

* **idx** *int* - index of the item to get recommendations from.
* **embeddings** *list[float]* - averaged word2vec embeddings.
* **nb_reco** *int* - number of recommendations to return.

#### visualize_embeddings

Function to visualize the word2vec embeddings.

*Arguments*

* **w2v** - trained word2vec model.

*Returns*

*dataframe* - PCA dataframe.

---

### Word cloud

#### generate_word_cloud

Function to plot a text word cloud.

*Arguments*

* **text** *str* - text to output in the word cloud.

---

### Utils

#### clean_lyrics

Function to clean the lyrics.

*Arguments*

* **lyrics** *str* - lyrics of a song.

*Returns*

*str* - cleaned lyrics.

#### prepare_text

Function to prepare the text (remove stop words, punctuation, etc.).

*Arguments*

* **text** *str* - text to prepare.

*Returns*

*str* - cleaned and tokenized text.
