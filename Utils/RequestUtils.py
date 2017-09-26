import requests

class RequestUtils:
    ARTIST_URL_APPEND = "artist/"

    def __init__(self, urlBase, api_key=[]):
        self.urlBase = urlBase
        self.api_key =  api_key

    def query_by_name(self, params, name, typeQuery = ""):

        params["query"] = "artist:" + name
        return self.query_site(typeQuery, params)

    def query_site(self, urlAppend = "", params=[], uid="", fmt="json"):

        params["fmt"] = fmt
        r = requests.get("{0}{1}".format(self.urlBase, urlAppend) + uid, params=params)
        print("requesting", r.url)

        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            r.raise_for_status()

    def query_site_authentication(self,target, offset, urlAppend = ""):

        params = {"api-key": self.api_key[target], "offset": offset}
        self.query_site(urlAppend, params)