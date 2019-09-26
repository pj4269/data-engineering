# DROP TABLES

songplay_table_drop = ("DROP TABLE  IF EXISTS songplays")
user_table_drop = ("DROP TABLE  IF EXISTS users")
song_table_drop = ("DROP TABLE  IF EXISTS songs")
artist_table_drop = ("DROP TABLE  IF EXISTS artists")
time_table_drop = ("DROP TABLE  IF EXISTS time")

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays (ts BIGINT, userId int , level varchar,\
                         sessionId int, location varchar, userAgent text,\
                         song_id varchar, artist_id varchar)")

user_table_create = ("CREATE TABLE IF NOT EXISTS users ( userId int, firstName varchar, lastName varchar, \
            gender char,  level varchar)")


song_table_create = ("CREATE TABLE IF NOT EXISTS songs (song_id varchar, title varchar, artist_id varchar,year int, duration numeric(5) )")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists ( artist_id varchar, artist_name varchar,artist_location varchar, artist_latitude varchar, 'artist_longitude varchar")

time_table_create = ("CREATE TABLE IF NOT EXISTS time ( timestamp bigint, hour int, day int, \
            week_of_year int,  month int, year int, weekday int)")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (ts, userId, level, sessionId, location, userAgent,song_id, artist_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")


user_table_insert = ("""INSERT INTO users( userId, firstName, lastName, gender,level) VALUES(%s, %s, %s, %s, %s ) """)

song_table_insert = ("""INSERT INTO songs (song_id, title,artist_id, year, duration ) VALUES (%s, %s, %s, %s, %s) """)

artist_table_insert = ("""INSERT INTO artists (artist_id, artist_name,artist_location, artist_latitude, artist_longitude ) VALUES (%s, %s, %s, %s, %s) """)


time_table_insert = ("""INSERT INTO time( timestamp, hour, day, week_of_year,  month, year, weekday) VALUES(%s, %s, %s, %s, %s, %s, %s) """)
# FIND SONGS

song_select = (""" select s.song_id, a.artist_id from songs s join artists a on s.artist_id = a.artist_id where s.title=%s and a.artist_name = %s and  s.duration=%s  """)



# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
