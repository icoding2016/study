"""
A web crawler that can take descriptive instruction for the content matching.
Using Pretrained Language Model - Bert

"""

import requests
from bs4 import BeautifulSoup
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModelForSeq2SeqLM
import torch
from dotenv import dotenv_values


class SmartWebCrawler:
    def __init__(self, relevance_model_name='distilbert-base-uncased-finetuned-sst-2-english',
                 summarization_model_name='t5-small'):
        self.env = dotenv_values()
        # Load the relevance analysis model and tokenizer
        self.relevance_tokenizer = AutoTokenizer.from_pretrained(relevance_model_name)
        self.relevance_model = AutoModelForSequenceClassification.from_pretrained(relevance_model_name)

        # Load the summarization model and tokenizer
        print(f'Loading model & tokkenizer ({relevance_model_name}, {summarization_model_name})')
        self.summarization_tokenizer = AutoTokenizer.from_pretrained(summarization_model_name)
        self.summarization_model = AutoModelForSeq2SeqLM.from_pretrained(summarization_model_name)

    def get_page_content(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def extract_text(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()

    def analyze_relevance(self, text, query):
        inputs = self.relevance_tokenizer(f"{query} [SEP] {text}", return_tensors='pt', truncation=True, padding=True)
        outputs = self.relevance_model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
        relevant_prob = probabilities[0][1].item()
        rating = int(relevant_prob * 10)
        return rating

    def summarize_text(self, text):
        inputs = self.summarization_tokenizer("summarize: " + text, return_tensors='pt', truncation=True,
                                              padding='max_length', max_length=512)
        outputs = self.summarization_model.generate(inputs['input_ids'], max_length=150, min_length=30,
                                                    length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = self.summarization_tokenizer.decode(outputs[0], skip_special_tokens=True)
        return summary

    def get_start_urls_from_search(self, query):
        print(f"get start urls from https://www.googleapis.com/customsearch")
        API_KEY = self.env["GC_API_KEY_CSEARCH"]
        CX = self.env["GC_CX"]
        url = f'https://customsearch.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={query}'
        urls = []
        response = requests.get(url)
        if response.status_code == 200:
            results = response.json()
            urls = [item['link'] for item in results.get('items', [])]
            print(f"start urls: {urls}")
        else:
            print(f"Fail to get start urls by google customsearch. response.status_code: {response.status_code}")
        return urls

    def crawl(self, query, start_urls=None, depth=2):
        if start_urls is None:
            start_urls = self.get_start_urls_from_search(query)
        visited = set()
        queue = [(url, 0) for url in start_urls]

        while queue:
            url, current_depth = queue.pop(0)
            if url in visited or current_depth > depth:
                continue
            visited.add(url)

            content = self.get_page_content(url)
            if content:
                text = self.extract_text(content)
                rating = self.analyze_relevance(text, query)
                if rating > 0:
                    summary = self.summarize_text(text)
                    yield url, summary, rating

                soup = BeautifulSoup(content, 'html.parser')
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href and href.startswith('http'):
                        queue.append((href, current_depth + 1))


def launch_crawler(query, start_urls=None, depth=2,
                   relevance_model_name='distilbert-base-uncased-finetuned-sst-2-english',
                   summarization_model_name='t5-small'):
    crawler = SmartWebCrawler(relevance_model_name=relevance_model_name,
                                 summarization_model_name=summarization_model_name)
    # results = []
    for url, summary, rating in crawler.crawl(query, start_urls, depth):
        # results.append((url, rating, summary))
        print(f"URL: {url}, \nRelevance: {rating}, \nSummary: {summary}")
        print('-'*80)
    # return results



# Example usage
def example():
    query = 'How to leverage AI technology in the telecom service industry?'
    # Case 1: Provide start_urls
    # start_urls = ['https://techcrunch.com']
    # results = launch_crawler(query, start_urls)
    # for url, summary, rating in results:
    #     print(f"URL: {url}, Summary: {summary}, Relevance Rating: {rating}")

    # Case 2: Don't provide start_urls, rely on search engine
    launch_crawler(query)

        


if __name__ == '__main__':
    example()
