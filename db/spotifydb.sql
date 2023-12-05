CREATE DATABASE IF NOT EXISTS Spotify;
USE Spotify;

DROP TABLE IF EXISTS Songs;
CREATE TABLE Songs (
	genre VARCHAR(255),
	artist_name VARCHAR(400),
	track_name VARCHAR(400),
    track_id VARCHAR(255),
    popularity INT,
    acousticness FLOAT,
    danceability FLOAT, 
    duration INT, 
    energy FLOAT, 
    instrumentalness FLOAT,
    _key VARCHAR(255),
    liveness FLOAT,
    loudness FLOAT,
    _mode VARCHAR(255),
    speechiness FLOAT,
    tempo FLOAT, 
    time_signature VARCHAR(255),
    valence FLOAT
    -- PRIMARY KEY (track_name, artist_name)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/spotify-chatbot/SpotifyFeatures.csv' 
INTO TABLE songs 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
