# Data by Daylight
A project used to generate a database from Dead by Daylight data. This database file is used to power the [Database by Daylight](https://github.com/GeorgeNakhle/database_by_daylight) Android app, but can be used for other purposes too.

There is no documentation for the database file, instead use a graphical tool like [DB Browser for SQLite](http://sqlitebrowser.org/) to see its contents. All the data I built from is in the [source_data](https://github.com/GeorgeNakhle/data_by_daylight/tree/main/source_data) folder.

## Purpose & Goals
This project exists as a free and open collection of Dead by Daylight data for people to build cool things with. I use this data in the (also open source) [Database by Daylight](https://github.com/GeorgeNakhle/database_by_daylight) Android app.

There are very few open collections of Dead by Daylight data out there, and assembling this added a significant amount of time to the app's development process. Hopefully this database can spare you some of that trouble.

The data collected is limited to observable or computable data. Handwritten guides and editorial content are not collected in this repository.

## Data Structure
Most of the data is fetched from [Tricky's API](https://dbd.tricky.lol/apidocs/) and converted into spreadsheets found in the [source_data](https://github.com/GeorgeNakhle/data_by_daylight/tree/main/source_data) folder. All the spreadsheets are then used to build the final SQL file (`dbd.db`).

To edit the spreadsheets, I suggest using an office program like [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) or [LibreOffice](https://www.libreoffice.org/). Make sure to use UTF-8 text encoding and comma separators when opening files. You can also import it to Google Drive.

## How to Download
- Go to the [Releases](https://github.com/GeorgeNakhle/data_by_daylight/releases) section in this repository.
- Go to the newest version and install `dbd.db` under Assets.
- You're done!


## How to Build
- Make sure Python 3.7 or greater is installed on your system.
- Open a terminal in the project's root folder.
- Install the Requests module (`pip install requests`).
- Run `python build.py` in the terminal to generate the `dbd.db` file.
- You're done!

## How do I contribute?
This project sources most of its data from spreadsheets in the [source_data](https://github.com/GeorgeNakhle/data_by_daylight/tree/main/source_data) folder. If you want to contribute a code change, inspect [build.py](https://github.com/GeorgeNakhle/data_by_daylight/blob/main/build.py) in the root folder and follow the import trail.

If you can't work Git but have data corrections you'd like to contribute, you can create a Github Issue with the new file or share a link to a Google Drive spreadsheet.

## Data Sources
The data collected by this project is an accumulation of various sources.

- [Tricky's API](https://dbd.tricky.lol/apidocs/)
- [Dead By Daylight Icon Toolbox](http://dbdicontoolbox.com/)

## Special Credits
- [Tricky](https://twitter.com/trickyau) - For creating the API where 90% of this data comes from.
- [Gathering Hall Studios](https://github.com/gatheringhallstudios) - For inspiring me to do this project for DbD.

## License
The build code is licensed under the [MIT License](http://opensource.org/licenses/mit-license.php). Data and images are from Dead by Daylight, which is owned by [Behaviour Interactive](https://www.bhvr.com/).

You are free to use this database for any purpose.