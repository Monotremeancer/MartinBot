from youtube_search import YoutubeSearch
def YT(search):
    results = YoutubeSearch(search, max_results = 10).to_json()
    return results
print(YT('Sad+but+true'))