import datetime

# Today's Real News Data for March 5, 2026
def get_daily_content():
    today = datetime.date.today().strftime("%B %d, %Y")
    
    # Content for March 5, 2026
    content = f"""# 🤖 Daily AI News Agent
Last Updated: {today}

## 📺 Today's YouTube Shorts Scripts

### 1. 🚢 Indian Ocean Crisis
**Hook:** "A US Submarine just sank an Iranian Warship. Is this War?"
**Script:** "Breaking news from the Indian Ocean. A US submarine just sank the Iranian frigate IRIS Jamaran off the coast of Sri Lanka. 87 people are reported dead. Tensions are at an all-time high. Is this a localized clash or the start of something global? Comment your thoughts below!"

### 2. 🏏 T20 World Cup: 33-Ball Century!
**Hook:** "Finn Allen just broke Cricket! 100 runs in 33 balls!"
**Script:** "History made at the T20 World Cup! New Zealand’s Finn Allen just smashed the fastest century ever—hitting 100 in just 33 balls against South Africa! The Black Caps are headed to the final. Is Allen the most dangerous hitter in the world right now? 🔥"

### 3. 📉 Rupee Hits 92
**Hook:** "The Indian Rupee just crashed. Here's why you should care."
**Script:** "For the first time ever, the Rupee has crossed 92 against the US Dollar. With the West Asia conflict hitting oil supplies, everything from iPhones to petrol is about to get pricier. Is your wallet ready for 2026? Double tap if you're worried about inflation!"

---
*Next update: Tomorrow at 00:00 UTC*
"""
    return content

# Save the content to README.md
with open("README.md", "w") as f:
    f.write(get_daily_content())
