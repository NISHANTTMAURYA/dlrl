#!/usr/bin/env python3
"""
Script to download raw HTML content from websites.
Saves HTML files with proper naming in the dataset/raw_html directory.
"""

import requests
import os
import time
from urllib.parse import urlparse
import hashlib

def create_filename_from_url(url):
    """Create a safe filename from URL."""
    # Parse the URL
    parsed = urlparse(url)
    # Combine domain and path
    domain = parsed.netloc.replace('www.', '')
    path = parsed.path.strip('/').replace('/', '_')
    
    if path:
        filename = f"{domain}_{path}"
    else:
        filename = domain
    
    # Clean filename
    filename = filename.replace('.', '_')
    # Limit length and add hash to ensure uniqueness
    if len(filename) > 50:
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        filename = filename[:42] + '_' + url_hash
    
    return filename + '.html'

def download_html(url, output_dir):
    """Download HTML content from a URL and save it."""
    try:
        print(f"Downloading: {url}")
        
        # Set headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Make request with timeout
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Create filename
        filename = create_filename_from_url(url)
        filepath = os.path.join(output_dir, filename)
        
        # Save HTML content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f"✓ Saved: {filename}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to download {url}: {str(e)}")
        return False
    except Exception as e:
        print(f"✗ Error saving {url}: {str(e)}")
        return False

def main():
    # Setup directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, 'dataset', 'raw_html')
    websites_file = os.path.join(script_dir, 'websites.txt')
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Read websites from file
    urls = []
    with open(websites_file, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if line and not line.startswith('#'):
                urls.append(line)
    
    print(f"Found {len(urls)} URLs to download")
    print("=" * 60)
    
    # Download each URL
    successful = 0
    failed = 0
    
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}]")
        if download_html(url, output_dir):
            successful += 1
        else:
            failed += 1
        
        # Be polite - wait between requests
        if i < len(urls):
            time.sleep(2)
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Download complete!")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total: {len(urls)}")
    print(f"HTML files saved in: {output_dir}")

if __name__ == "__main__":
    main()
