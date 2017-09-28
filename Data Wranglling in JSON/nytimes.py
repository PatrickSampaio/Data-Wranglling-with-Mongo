import json
import codecs
import requests

from Utils.RequestUtils import RequestUtils

URL_MAIN = "http://api.nytimes.com/svc/"
URL_POPULAR = URL_MAIN + "mostpopular/v2/"
API_KEY = {"popular": "",
           "article": "91fb265cb8f2410f9901ebbed631daf0"}
URL_FIELD = "url"
TITLE_FIELD = "title"
REQUEST_FACTORY = RequestUtils(URL_MAIN, API_KEY)

def get_from_file(kind, period):
    filename = "popular-{0}-{1}.json".format(kind, period)
    with open(filename, "r") as f:
        return json.loads(f.read())


def article_overview(kind, period):
    data = get_from_file(kind, period)
    all_news = [news for news in data]

    titles = []
    urls = []

    for news in data:
        titles.append({news["section"]:news[TITLE_FIELD]})
        for news_media in news["media"]:
            urls.append([url["url"] for url in news_media["media-metadata"] if "Standard Thumbnail" == url["format"]])

    return (titles, urls)


def get_popular(kind, days, section="all-sections", offset=0):


    if days not in [1, 7, 30]:

        print("Time period can be 1,7, 30 days only")
        return False

    if kind not in ["viewed", "shared", "emailed"]:

        print("kind can be only one of viewed/shared/emailed")
        return False

    url_append = "{}most{0}/{1}/{2}.json".format(URL_POPULAR, kind, section, days)
    data = REQUEST_FACTORY.query_site_authentication(url_append, "popular", offset)

    return data


def save_file(kind, period):


    data = get_popular(URL_POPULAR, "viewed", 1)
    num_results = data["num_results"]
    full_data = []

    with codecs.open("popular-{0}-{1}.json".format(kind, period), encoding='utf-8', mode='w') as v:

        for offset in range(0, num_results, 20):

            data = get_popular(URL_POPULAR, kind, period, offset=offset)
            full_data += data["results"]

        v.write(json.dumps(full_data, indent=2))


def test():

    titles, urls = article_overview("viewed", 1)
    assert len(titles) == 20
    assert len(urls) == 30
    assert titles[2] == {'Opinion': 'Professors, We Need You!'}
    assert urls[20] == 'http://graphics8.nytimes.com/images/2014/02/17/sports/ICEDANCE/ICEDANCE-thumbStandard.jpg'


if __name__ == "__main__":
    test()