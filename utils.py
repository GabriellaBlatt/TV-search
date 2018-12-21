from bottle import template
import json

JSON_FOLDER = './data'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143", "175", "216", "1371", "1871", "2993", "305"]


def getVersion():
    return "0.0.1"


def getJsonFromFile(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"


def find_relevant_shows(word):
    word = word.lower()
    all_of_shows = [json.loads(getJsonFromFile(AVAILABE_SHOWS[i])) for i in range(12)]
    relevant = []
    for show in all_of_shows:
        for episode in show["_embedded"]["episodes"]:
            if episode["summary"] and word in episode["summary"].lower():
                e = {
                    "showid": show["id"],
                    "episodeid": episode["id"],
                    "text": "{show}: {episode}".format(show=show["name"], episode=episode["name"])
                }
                relevant.append(e)
    return relevant
