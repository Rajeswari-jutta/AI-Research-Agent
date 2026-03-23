import requests
from bs4 import BeautifulSoup
from transformers import pipeline

summarizer = pipeline("summarization")

def fetch_data(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    return response.text

def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")
    paragraphs = soup.find_all("p")
    text = " ".join([p.get_text() for p in paragraphs])
    return text

def summarize_text(text):
    text = text[:1000]
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def ai_research_agent(query):
    html = fetch_data(query)
    text = extract_text(html)
    summary = summarize_text(text)
    return summary

query = input("Enter your topic: ")
print(ai_research_agent(query))
