"""
To experiment with this code freely you will have to run this code locally.
Take a look at the main() function for an example of how to use the code. We
have provided example json output in the other code editor tabs for you to look
at, but you will not be able to run any queries through our UI.
"""
import json
import requests

from Utils.PrintUtils import pretty_print
from Utils.RequestUtils import RequestUtils

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"


# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}

FIRST_AID_KIT = "First Aid Kit"

REQUEST_FACTORY = RequestUtils(BASE_URL)


def answerFirstAidKit():

    response_first_aid_kit =REQUEST_FACTORY.query_by_name(query_type["simple"], FIRST_AID_KIT, REQUEST_FACTORY.ARTIST_URL_APPEND)
    response_first_aid_kit_list = [band for band in response_first_aid_kit["artists"] if band["name"] == FIRST_AID_KIT]
    answer_first_question = len(response_first_aid_kit_list)
    pretty_print("There is {} with the name of {}".format(answer_first_question, FIRST_AID_KIT))


def AnswerQuestion():

    answerFirstAidKit()

def main():

    request = RequestUtils(ARTIST_URL)

    results = request.query_by_name(query_type["simple"], "Nirvana")
    pretty_print(results)


    print ("\nARTIST:")
    pretty_print(results["artists"][3])

    artist_id = results["artists"][3]["id"]
    artist_data = request.query_site(query_type["releases"], artist_id)
    releases = artist_data["releases"]


    print ("\nONE RELEASE:")
    pretty_print(releases[0], indent=2)

    release_titles = [r["title"] for r in releases]
    print("\nALL TITLES:")
    for t in release_titles:
        print(t)

if __name__ == '__main__':
    AnswerQuestion()