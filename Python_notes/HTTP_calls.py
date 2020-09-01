
import urllib.request,json

def main():
    url = "http://api.plos.org/search?q=title:DNA"
    data=urllib.request.urlopen(url).read()
    jsonData =json.loads(data.decode("utf-8"))
    print(jsonData["response"]["docs"][0]["abstract"])

if __name__ == '__main__':main()



















