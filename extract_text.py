from bs4 import BeautifulSoup
import sys

def extract_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all text nodes
    text_nodes = []
    for element in soup.find_all(string=True):
        if element.parent.name not in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            text = element.strip()
            if text:
                text_nodes.append(text)

    # Print unique text nodes to avoid duplicates
    seen = set()
    for text in text_nodes:
        if text not in seen:
            print(f"TEXT: {text}")
            seen.add(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        extract_text(sys.argv[1])
    else:
        print("Usage: python extract_text.py <file_path>")
