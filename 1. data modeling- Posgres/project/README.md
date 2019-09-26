1. Discuss the purpose of this database: 

- Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Since the resides in a directory of JSON logs on user activity on the app, there' no way of doing queries or other ways to extract useful information. So we created star schema with fact table songplays with dimension tables users, songs, artists, and time to break into the database to create more organization, data cohesiveness, and possibly more insight into their data. 

- We created a star schema optimized for queries on song play analysis

- We have created the following tables with the respective attributes: 
  1) songplays (ts BIGINT, userId int , level varchar,sessionId int, location varchar, userAgent text,song_id varchar, artist_id varchar,     PRIMARY KEY (song_id, artist_id)   )

  2) users ( userId int PRIMARY KEY, firstName varchar, lastName varchar, gender char,  level varchar)

  3) songs (song_id varchar PRIMARY KEY, title varchar NOT NULL, artist_id varchar,year int, duration numeric(5) )

  4) artists ( artist_id varchar PRIMARY KEY, artist_name varchar NOT NULL,artist_location varchar, artist_latitude varchar, artist_longitude varchar )

  5) time ( timestamp bigint, hour int, day int, week_of_year int,  month int, year int, weekday int)

- to run the script, simply type create_tables.py from your command prompt

2. State and justify your database schema design and ETL pipeline.

- We tried to simplify the data extraction process as much as possible by doing a separate extraction process on log and songs file. Also we tried to avoid JOIN statement as much as possible since this become a hindrance for large dataset. By doing so, we defined the fact and dimension tables for a star schema for a particular analytic focus, and wrote an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL

3. Docstrings description: 

 1) process_log_file(cur, filepath): This function can be used to read the file in the filepath (data/log_data) to get the user and time info and used to populate the users and time dim tables.
    Arguments:
    cur: the cursor object. 
    filepath: log data file path. 
    Returns:
    None
 2) def get_files(filepath):This function can be used to get the file in the filepath (data) to get the log and songs json files and used to populate the tables derived from there.
    filepath: all the data file path.
    return all files

 3) def process_song_file(cur, filepath):  This function can be used to read the song file in the filepath (data/song_data) to get the song and artist info and used to populate the song and artist dim tables
    Arguments:
    cur: the cursor object. 
    filepath: data file path.      
        

3. [Optional] Provide example queries and results for song play analysis: Here are the important changes I have made: 
   a. On line 66, I have used dropna() function to drop all the missing values from user_df dataframe.
   b. On line 72, I have used dropna() function to drop all the missing values from df dataframe.
   c. On line 88, 89 and 90, I have added songid and artistid values to the row value of selected columns, namely 'ts', 'userId', 'level', 'sessionId', 'location', 'userAgent'
        
