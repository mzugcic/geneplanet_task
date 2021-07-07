## GenePlanet task

Here is a solution to a task which included:
- parsing a given _*.vcf_ file
- creating a small web app for filtering and viewing genome values

#### Used technologies
- [Python 3.7.9](https://www.python.org/downloads/release/python-379/)
- [PostgreSQL 12.6](https://www.postgresql.org/docs/12/index.html)
- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- [Django 3.2.5](https://docs.djangoproject.com/en/3.2/)

### Runing the project
To run the project you have to have _Python_, _PostgreSQL_ & _virtualenwrapper_ (you can use
 any tool for creating virtual environments for Python) installed on your machine. Please reference the
  documentation on the provided links for further information. _Django_ will be installed inside
   of the virtual environment with all the libraries needed for the project.
   
After you have everything of the above set up and working follow the next steps:
1. Create a virtual environment and call it whatever you want

2. Activate the same - if you used the same technologies as I did run:
    ```
    workon <env_name>
    ```
   
3. From the root of the project run:
    ```
    pip install -r requirements.txt
    ```
   This will also install Django.

4. Set up your environment variables as is shown in the _.env.example_ file & apply them by
 calling the next command from the project root folder:
    ```
   source .env
   ```

You should now be ready to run & test the project.

### Parsing gziped _*.vcf_ files

To fill the DB with data you can parse _*.vcf_ files.

To parse data from a file run the following command:
```
python manage.py parse_gziped_vcf_file <path_to_file>
```

By running this command all entries in the file will be parsed into `Genome` objects and will be
 available for viewing.
 
The command accepts 3 arguments, of which one is required:
 - `file` - **required** - path to file that should be parsed
   - this information is visible in the properties of the file accessible by right clicking on
    the file and selecting properties

 - `--bulk-limit` - integer that specifies how many objects should be processed at once in bulk
   - _does not  affect final count of processed objects_
   - this can have performance impacts since objects are parsed & later created in bulk - _use with
    caution_
    - defaults to `2000`
    
 - `--parse-count` - integer that specifies final count of processed objects
   - useful when parsing of the whole file is not needed, especially for testing purposes
    - when not set all file data is processed
    - defaults to `None`

### Search API

The home page is accessed on the next URL - http://127.0.0.1:8000/genomes/. For the app to work
 start the local server with the next command:
 ```
 python manage.py runserver
```

The page consists of a single text box which when filled searches the DB for the desired genome
 values.

The search bar handles searches by **RSID** & **CHR POS**.