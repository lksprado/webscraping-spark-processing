import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bs4 import BeautifulSoup as bs

from app.extract import extract_html 

def test_extract_success(requests_mock):
    url = "http://example.com"
    html_content = "<html><body><h1>Test</h1></body></html>"
    requests_mock.get(url, text=html_content)
    
    soup = extract_html(url)
    assert isinstance(soup, bs)
    assert soup.find("h1").text == "Test"