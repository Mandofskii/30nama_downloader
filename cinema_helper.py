from requests import post, get

class Subtitles:
    def __init__(self, episode):
        self.fa = episode["subtitle"]["fa"]
        self.en = episode["subtitle"]["en"]

class Qualities:
    def __init__(self, qualities):
        self.label = qualities["label"]
        self.link = qualities["src"]

class Downloads:
    def __init__(self, downloads):
        self.qualities = []
        for quality in downloads["file"]["source"][1:]:
            self.qualities.append(Qualities(quality))

class Episodes:
    def __init__(self, episode):
        self.downloads = Downloads(episode)
        self.episode_title = episode["data"]["episode"]
        self.subtitle = Subtitles(episode)

class Seasons:
    def __init__(self, season, episodes):
        self.episodes = []
        self.season = season
        for episode in episodes:
            self.episodes.append(Episodes(episode))

class Post:
    def __init__(self, result):
        print(result)
        self.id = result["data"]["post_id"]
        self.title = result["data"]["title"]
        if "list" in list(result.keys()):
            self.type = "series"
            self.seasons = []
            for season,episodes in result["list"].items():
                self.seasons.append(Seasons(season, episodes))
        else:
            self.type = "movie"
            self.downloads = Downloads(result)


class Cinema:
    def __init__(self, token):
        self.token = token
        self.api_key = "SOON"
        self.base_url = "SOON"
        self.headers = {
            "c-api-key": self.api_key,
            "c-useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
            "c-vpn": "false",
            "c-app-version": "0.9.7",
            "c-platform": "Desktop",
            "c-token": self.token,
        }

    def find_post_by_id(self, id):
        return Post(
            post(
                self.base_url + "stream/id/" + str(id),
                headers = self.headers
            ).json()["result"]
        )
