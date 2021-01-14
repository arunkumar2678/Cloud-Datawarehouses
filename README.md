# PostGresSQL - Python Project

## Some websites referred for help

[Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
[Converting Dictionary to List](https://stackoverflow.com/questions/1679384/converting-dictionary-to-list)
[w3 school](www.w3schools.com)

etl.py - has the ETL process to load all the fact and dimension tables

|Artist Table | Data type | Is Null | Description|
|-------------|-----------|----------|-----------|
|artist_id | varchar | not null | (Primary key (unique id) of the table (This is treated as a primary key since it will uniquely identify the artist)|
|artist_name | varchar | not null | Name of the artist|
|artist_location | varchar | null | Location of the artist|
|artist_latitude | float | null | Latitude of location of the artist|
|artist_longitude | float | null | Longitude of location of the artist|

|Songs Table | Data type | Is Null | Description|
|------------|-----------|---------|--------------
|song_id | varchar | not null | Primary key (unique id) of the table (This is treated as a primary |key since it will uniquely identify the song)|
|title | varchar | not null | Title of the song\
|artist_id | varchar | not null | Id of the artist(foreign key)|
|year | int | not null | Year of the song|
|duration | float | not null | Duration of the song|

| Time Table | Data type | Is Null | Description |
|------------|-----------|---------|-------------|
|starttime | date | not null | Primary key (unique id) of the table|
|hour | int | not null | Hour from timestamp|
|day | int | not null | Day from timestamp|
|week | int | not null | Week from timestamp|
|month | int | not null | Month from timestamp|
|year | int | not null | Year from timestamp|
|weekday | int | not null | Weekday from timestamp|

|Users | Data type | Is Null | Description|
|------|-----------|---------|------------|
userid | int | null | Primary key (unique id) of the table (This is treated as a primary key since it will uniquely identify the user)
firstname | varchar | null | First name of the user
lastname | varchar | null | Last name of the user
gender | varchar | null | Gender of the user
level | varchar | not null | Level of the user

|Songplays | Data type | Is Null | Description|
|----------|-----------|---------|------------|
|songplay_id | int | int | Primary key (unique id) of the table (This is treated as a primary key since it will uniquely identify the record with all the songplays information).|
|starttime | varchar | not null | Timestamp of the song|
|userid | varchar | null | ID of the user (Foreign key)|
|level | varchar | not null | The level of user app|
|song_id | varchar | null | ID of the song (Foreign key)|
|artist_id | varchar | null | ID of the artist (Foreign key)|
|sessionid | int | not null | The session id of the user on the app|
|location | varchar | null | Location of song played|
|useragent | varchar | null | User agent of the app|


|staging_events| Data type |
|------------|-----------|
|artist |TEXT|
|auth | TEXT|
|first_name |TEXT|
|gender | CHAR|
|item_session | INTEGER|
|last_name |TEXT|
|length |NUMERIC|
|level |TEXT|
|location |TEXT|
|method |TEXT|
|page |TEXT|
|registration |NUMERIC|
|session_id |INTEGER|
|song |TEXT|
|status |INTEGER|
|ts |BIGINT|
|user_agent |TEXT|
|user_id |INTEGER|


|staging_songs |Data type |
|------------|-----------|
|num_songs |INTEGER|
|artist_id |TEXT|
|artist_latitude |NUMERIC|
|artist_longitude |NUMERIC|
|artist_location |TEXT|
|artist_name |TEXT|
|song_id |TEXT|
|title |TEXT|
|duration |NUMERIC|
|year |INTEGER|


# Files

* etl.py- Final ETL file.
* create_tables.py - Python file creating database and tables.
* sql_queries.py - contains all the queries.
* etl_redshift - coding for rough draft to be used for the final ETL file (etl.py)

