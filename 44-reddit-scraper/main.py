import requests, bs4

print("Requesting page...\n")

response = requests.get("https://www.reddit.com/", headers = {'User-agent': 'r-scraper-demo'})
response.raise_for_status()
print("Response recieved\n")

page = bs4.BeautifulSoup(response.text, "html.parser")

print("[ TRENDING SUBREDDITS ]\n")

trending_subs = page.select(".trending-subreddits-content > ul > li > a")
for ix, sub in enumerate(trending_subs):
    print(str(ix+1) + ".) " + sub.getText())
    print("URL: " + sub.attrs['href'], "\n")

print("[ POPULAR POSTS ]\n")

popular_posts = page.select(".link")
for ix, post in enumerate(popular_posts):
    title = post.select(".title")[0].getText()
    rating = post.select(".score.unvoted")[0].getText()
    comments = post.select(".comments")[0].getText()
    author = post.select(".author")[0].getText()
    subr = post.select(".subreddit")[0].getText()
    url = post.select("a.title")[0].attrs['href']
    
    print("----------")
    print(str(ix+1) + ".) " + title)
    print("\tRating:", rating)
    print("\t" + comments)
    print("\tPosted in " + subr + " by " + author)
    print("\t(" + url + ")")
