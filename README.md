# qpa_final_project

This is a final project for Quantory Python School.

## Starting the app

1. Clone this repository:<br>
```commandline
git clone https://github.com/q-liza/qpa_final_project.git
```
2. Build images and run containers from project root folder:<br>
```commandline
docker compose up -d
```
> :information_source: there are docker volume for database and mounted directories for application data 
> (e.g. logs, input and output files) in `docker-compose.yaml`

> :information_source: logs and output files are preserved in mounted directories

4. Initialize database (for the first run):<br>
```commandline
docker compose run --rm app python db/initialize_db.py
```
4. Start application:<br>
```commandline
docker compose run --rm app python main.py <args>
```
> :information_source: `app/main.py` is an entry point of the app

> :information_source: `<args>` must be replaced with arguments for `main.py`
<details>
  <summary>main.py cli-usage</summary>

  ```commandline
  main.py [-h] [--step STEP] [--plot_filename PLOT_FILENAME] [--file] INPUT
  ```
  ```
  positional arguments:
    INPUT                 the input DNA sequence: as a string itself or as a
                          filename. If filename is provided, must also provide '
                          --file' option
  
  optional arguments:
    -h, --help            show this help message and exit
    --step STEP           the step for gc-content calculating (default: 100)
    --plot_filename PLOT_FILENAME
                          the filename of a gc-content plot (default:
                          'gc_ratio_plot')
    --file                specifies that DNA sequence must be read from <input>
                          file
  ```
</details>

<details>
  <summary>example</summary>

  ```commandline
  docker compose run --rm app python main.py genomic.fna --plot_filename some_plot --file
  ```
</details>

5. Stop application:<br>
```commandline
docker compose down
```

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
