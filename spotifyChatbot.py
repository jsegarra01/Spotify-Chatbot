# This is a sample Python script.
import sqlite3
from flask import Flask, request, make_response, jsonify
import mysql.connector
from mysql.connector import Error, MySQLConnection

app = Flask(__name__)

# MYSQL DB Config
config = {
    'host': 'localhost',
    'database': 'Spotify',
    'user': 'root',
    'password': 'root'
}

# Create route for webhook
@app.route('/', methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        payload = request.json
        param_response = (payload['queryResult']['parameters'])
        query = "SELECT * FROM songs WHERE "

        counter = 0
        limiter = 3
        dialog_response = "Here are some songs I found: "

        print(param_response) # debug

        # Loop through JSON parameters to add query conditions
        for param in param_response:
          if param_response[param] != "" and param_response[param]:
            counter += 1
            if param == 'n_energy':
              aux = "energy < 0.4 AND "
            elif param == 'energy':
              aux = "energy > 0.75 AND "
            elif param == 'tempo':
                aux = "tempo > 130 AND "
            elif param == 'n_tempo':
                aux = "tempo < 90 AND "
            elif param == 'valence':
                aux = "valence > 0.75 AND "
            elif param == 'n_valence':
                aux = "valence < 0.4 AND "
            elif param == 'duration':
                aux = "duration > 360000 AND "
            elif param == 'n_duration':
                aux = "duration < 120000 AND "
            elif param == 'danceability':
                aux = "danceability > 0.75 AND "
            elif param == 'n_danceability':
                aux = "danceability < 0.4 AND "
            elif param == 'liveness':
                aux = "liveness > 0.8 AND "
            elif param == 'speechiness':
                aux = "speechiness > 0.33 AND speechiness < 0.66 AND "
            elif param == 'n_speechiness':
                aux = "speechiness < 0.4 AND "
            elif param == 'popularity':
                aux = "popularity > 70 AND "
            elif param == 'n_popularity':
                aux = "popularity < 45 AND "
            elif param == 'podcast':
                aux = "speechiness > 0.7 AND "
            elif param == 'genre':
              aux = "genre = '" + str(param_response[param]) + "' AND "
            elif param == 'music-artist':
              aux = "artist_name = '" + str(param_response[param]) + "' AND "
            elif param == 'number':
              limiter = int(param_response[param])
            query += aux
        query = query[:-4] + "ORDER BY RAND() LIMIT " + str(limiter) + ";" 
        
        print(query)

        if(counter == 0):
            return make_response(jsonify({'fulfillmentText': 'Please be a bit more specific.'}))

        try:
            print(query)
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(query)

            row = cursor.fetchone()
            if row is None:
              dialog_response = "I'm sorry I couldn't find anything in my database."
            else:
              while row is not None:
                print(row)
                dialog_response += row[2] + " - " + row[1] + " https://open.spotify.com/track/" + row[3] + "\n"
                row = cursor.fetchone() 

            cursor.close()
            conn.close()

            return make_response(jsonify({'fulfillmentText': dialog_response}))

        except Error as e:
            print(e)

if __name__ == '__main__':
    app.run(debug=True)