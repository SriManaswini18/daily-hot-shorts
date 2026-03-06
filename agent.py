import urllib.request
import xml.etree.ElementTree as ET
import datetime

def get_live_news():
    # Fetching Top Stories from Google News RSS
    url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    try:
        response = urllib.request.urlopen(url)
        tree = ET.parse(response)
        root = tree.getroot()
        news_items = []
        for item in root.findall('./channel/item')[:3]:
            news_items.append(item.find('title').text)
        return news_items
    except:
        return ["Cricket Updates", "Tech Trends", "World News"]

def create_shorts():
    topics = get_live_news()
    today = datetime.date.today().strftime("%B %d, %Y")
    content = f"# 🤖 Daily News Agent\nLast Updated: {today}\n\n"
    for i, t in enumerate(topics, 1):
        content += f"### {i}. {t}\n**Hook:** \"This is big! {t}\"\n**Script:** \"Breaking news for {today}! {t}. This is trending right now. What do you think?\"\n\n"
    return content

with open("README.md", "w", encoding="utf-8") as f:
    f.write(create_shorts())
    
