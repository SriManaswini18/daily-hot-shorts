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
        
        # Get the first 3 trending titles
        news_items = []
        for item in root.findall('./channel/item')[:3]:
            news_items.append(item.find('title').text)
        return news_items
    except:
        return ["Cricket World Cup Updates", "Global Tech Trends", "Market News"]

def create_shorts_scripts():
    topics = get_live_news()
    today = datetime.date.today().strftime("%B %d, %Y")
    
    content = f"# 🤖 Daily AI News Agent\n"
    content += f"Last Updated: {today}\n\n"
    content += f"## 📺 Today's YouTube Shorts Scripts\n\n"
    
    for i, topic in enumerate(topics, 1):
        content += f"### {i}. {topic}\n"
        content += f"**Hook:** \"You won't believe what's happening right now with {topic.split(' - ')[0]}!\"\n"
        content += f"**Script:** \"Huge news today! {topic}. This is changing everything we thought we knew. What do you think? Is this a win or a fail? Comment below!\"\n\n"
    
    content += "---\n*Generated automatically by your GitHub Agent.*"
    return content

# Save to README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(create_shorts_scripts())
