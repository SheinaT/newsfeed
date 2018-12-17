from bottle import route, run, static_file
import json, feedparser
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context



# rss_sources={
#     'jpost': "https://www.jpost.com/Rss/RssFeedsHeadlines.aspx"
# }


feed = feedparser.parse("https://www.fifa.com/rss/index.xml")


title = feed["entries"][0]["title"]
link = feed["entries"][0]["link"]

@route('/')
def html():
    return static_file("index.html", root='')


#
# def parseFeed(rss_link):
#     return feedparser.parse(rss_link)
@route('/get_articles')
def get_headlines():
    headlines_list = []
    headlines={
        "headlines":headlines_list
    }
    for headline in feed["entries"]:
        title = headline["title"]
        link = headline["link"]
        rss_dict={
            "title":title,
            "link": link
        }
        headlines_list.append(rss_dict)
    return json.dumps(headlines)

@route('/CSS/style.css')
def css():
    return static_file("style.css", root='CSS')

@route('/JS/star2.js')
def js():
    return static_file("star2.js", root='JS')



def main():
    run(host='localhost', port=7000)
if __name__ == '__main__':
    main()