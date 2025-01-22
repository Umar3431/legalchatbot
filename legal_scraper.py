import requests
from bs4 import BeautifulSoup
import re

def scrape_legal_information(query):
    """Scrapes the entire web for relevant legal information"""
    
    # Use Google Search API or scrape Google Search results
    search_url = f"https://www.google.com/search?q={query}+law+OR+legal+OR+regulation"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    
    # Extract top search results
    for g in soup.find_all("div", class_="tF2Cxc"):
        title = g.find("h3").text
        link = g.find("a")["href"]
        snippet = g.find("span", class_="aCOpRe").text if g.find("span", class_="aCOpRe") else "No snippet available."

        results.append(f"🔹 **{title}**\n{snippet}\n🔗 [Read More]({link})\n")

    # If results found, return top 3
    if results:
        return "\n".join(results[:3])
    
    return None  # No legal information found, AI will handle it
