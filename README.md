# qpa_final_project

This is a final project for Quantory Python School.

## Starting the app

1. Initialize Environment Variable:<br>
add `APP_DIR` environment variable with the path to the `app` folder on your machine, since other paths in config depend on it.
2. Initialize Data Base:<br>
separately run `app/db/init.py` script for initial db creation.
3. Start the App:<br>
use `app/main.py` as an entry point of the app.

## Project Structure
- `app`: the app root directory
  - `db`: database related logic
    - `init.py`: data and script for db creation, table creation and filling tables with data
    - `manager.py`: main objects for db interaction
    - `models.py`: data models for tables
    - `queries.py`: data retrieving queries
  - `gc_content_functions.py`: [gc-content metric](https://en.wikipedia.org/wiki/GC-content) related logic
  - `gene_expression_functions.py`: [gene expression](https://www.khanacademy.org/science/high-school-biology/hs-molecular-genetics/hs-rna-and-protein-synthesis/a/the-genetic-code) related logic
  - `main.py`: example of app usage, app entry point
  - `config.py`: configuration file
- `pic`: user saved plots as images

<br>

> **Warning** <br>
> contributors @q-liza and @lizaa-t are the same person :)
