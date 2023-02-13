# Data by Daylight
A project used to generate a database from Dead by Daylight data. This database file is used to power the Database by Daylight Android app, but can be used for other purposes as well.

Check the releases section for compiled SQLite db files. There is no documentation for the db file, instead use a graphical tool like [SQliteBrowser](http://sqlitebrowser.org/) or figure it out from the [mapping file](). The data I built from is in the [source_data](https://github.com/gatheringhallstudios/MHWorldData/tree/master/source_data) folder.

## Purpose & Goals
This project exists as a free and open collection of Dead by Daylight data for people to build cool things with. I use this data in the (also open source) [Dead by Database](https://github.com/GeorgeNakhle/database_by_daylight) Android app.

There are very few open collections of Dead by Daylight data out there, and assembling this added a significant amount of time to the app's development process. Hopefully this database can spare you some of that trouble.

The data collected is limited to observable or computable data. Handwritten guides and editorial content are not collected in this repository.

## How do I contribute?
This project sources most of its data from spreadsheets in the [source_data/](https://github.com/gatheringhallstudios/MHWorldData/tree/master/source_data) folder. If you want to contribute a code change, inspect build.py in the root folder and follow the import trail.

If you are unable to work Git but have data corrections or translations to contribute, you can create a Github Issue with the new file or share a link to a google drive spreadsheet.

## Data Structure
The data files in [source_data/](https://github.com/gatheringhallstudios/MHWorldData/tree/master/source_data) are used to build the final SQL file.

To edit the CSV files, I suggest using an office program like Excel or [LibreOffice](https://www.libreoffice.org/). Make sure to use UTF8 text encoding and comma separators when opening files. You can also import it to Google Drive.

Each subsystem (Survivor, Killer, Item, etc.) is stored in its own subdirectory. There are several types of data files:
- ***type*_base.csv**: A names and basic data registry containing the names of different objects of that type for each supported language, as well as any additional base data.
- ***type*_base_translations.csv**: An extension of a base file that adds translated names and potentially descriptions to the main base file.
- ***type*_*data*.csv**: Additional data key'd by the name of the owning type. These are used when the type can have many data, like a monster can have many hunting rewards.
- ***type*_ext.csv**: Extension data that adds additional data to the type. This is used when each type can be optionally extended, such as a weapon that may be a bowgun and has bowgun ammo.

## How to Build
Make sure Python 3.6 or greater is installed on your system, and pipenv is installed (`pip install pipenv`).
- Open a console window in the root project directory (shift+rightclick or `cd` to navigate to it)
- `pipenv --python 3.8` to setup the environment. Make sure its using python 3.6 or greater.
- `pipenv install` to install all dependencies. 
- `pipenv shell` to activate the environment

Afterwards, run `pipenv run python build.py` in a terminal to generate an `dbd.sql` file. You can run the tests by executing `pipenv run pytest tests`. 
You will need to use `pipenv shell` everytime you open a new console window.

## Data Sources
The data collected by this project is an accumulation of various sources, including manual entry from the game itself, official guidebooks, and other collections.

- [Tricky's API](https://dbd.tricky.lol/apidocs/)
- [Dead By Daylight Icon Toolbox](http://dbdicontoolbox.com/)

## Special Credits
- [Tricky](https://twitter.com/trickyau) - For creating the API where 90% of this data comes from.
- [Gathering Hall Studios](https://github.com/gatheringhallstudios) - For inspiring me to do this project for DbD.

## License
The build code is licensed under the [MIT License](http://opensource.org/licenses/mit-license.php). Data and images are from Dead by Daylight, which is owned by Behaviour Interactive.

You are free to use this database for any purpose.