# Knowledge-Based Systems: Spotify-Chatbot
## About The Project

This project is a final project for the Knowledge Based Systems subject, it implements a webhook for a DialogFlow chatbot. 

### Authors
Eric Macià: eric.macia@students.salle.url.edu

Guillermo Sabaté: guillermo.sabate@students.salle.url.edu

Josep Segarra: josep.segarra@students.salle.url.edu

### Overview
* The chatbot suggests spotify music based on user demands, mapping the most basic requirements (Genre, Danceability, Tempo, Artist, ...)
* The chatbot is designed to implement the NLP functionalities provided by DIalogFlow, where work regarding the ontology of the project has been contemplated.


### Built With

The project has been built with some tools, frameworks and languages mentioned below.

* [DialogFlow](https://dialogflow.cloud.google.com/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [MySQL](https://www.mysql.com/)
* [ngrok](https://ngrok.com/)
* [Python](https://www.python.org/downloads/)


<!-- GETTING STARTED -->
## Getting Started

These are the instructions on setting up the project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

To run the program locally it is important to have installed the tools mentioned earlier.

* DialogFlow: To get access to the Chatbot, previous approval needs to have been done, for that contact the email on the Contact section to ask for developer permissions for the Chatbot configuration.
Alternatively, you can create a new agent in DialogFlow and import the data with the json files provided in the intents/ and entities/ directories.

* Python: We developed it in python 3.10.4, make sure to verify python version when using the project. 

* MySQL: 
```sh
pip install mysql-connector-python
```
* Flask: 
```sh
pip install flask
```
* Ngrok: Installed from link provided above.


### Installation

_Below is an example of how you can install and set up the project. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/ericmaciared/spotify-chatbot.git
   ```
2. Init MySQL and run the install .sql file to create the database.
   ```sh
   db/spotifydb.sql
   ```
   Make sure that the path to the csv file containing the information is in the right folder.
3. Run ngrok
   ```sh
   ngrok http 5000
   ```
4. Start the spotifyChatbot.py program
    ```sh
    pyhton3 spotifyChatbot.py
    ```
5. Copy https address provided by ngrok to the fulfillment section in DialogFlow.

5. Access the chatbot through Telegram or any other configured interface.
For telegram access this is the address:
    ```sh
    https://t.me/kbsspotifybot
    ```

<!-- USAGE EXAMPLES -->
## Usage

Type and talk with the chatbot through the interface, it can be asked small talk questions, and its main activity is to recommend songs, these can be asked through a set of parameters.
* Genres (Rock, Rap, Country, …)
* Popularity (Play number, popular, unknown, niche, …)
* Valence (happy-sad)
* Tempo (fast, slow)
* Artists by name (Eminem, Shakira,  Queen, …)
* Energy (energetic, weak, chill, …)
* Danceability (very danceable, not danceable, …)
* Duration of track (very long, short, by seconds, …)
* Key (A, B, G, …)
* Speechiness (very verbal, no voice, podcast, …)
* Liveness (live music, studio, …)


<!-- CONTACT -->
## Contact

Project Link: [https://github.com/ericmaciared/spotify-chatbot](https://github.com/ericmaciared/spotify-chatbot)
