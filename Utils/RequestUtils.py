import requests

class RequestUtils:
    def __init__(self, urlBase):
        self.urlBase = urlBase

    def query_by_name(self, params, name):
        """
        This adds an artist name to the query parameters before making an API call
        to the function above.
        """
        params["query"] = "artist:" + name
        return self.query_site(params)

    def query_site(self, params, uid="", fmt="json"):
        """
        This is the main function for making queries to the musicbrainz API. The
        query should return a json document.
        """
        params["fmt"] = fmt
        r = requests.get(self.urlBase + uid, params=params)
        print("requesting", r.url)

        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            r.raise_for_status()