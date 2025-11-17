#!/usr/bin/env python3
"""
Script to convert raw HTML files to Markdown format.
Uses html2text library for conversion.
"""

import os
import html2text
from pathlib import Path

def convert_html_to_markdown(html_file, output_dir):
    """Convert a single HTML file to Markdown."""
    try:
        # Read HTML content
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Configure html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_emphasis = False
        h.body_width = 0  # Don't wrap lines
        h.unicode_snob = True  # Use unicode
        h.skip_internal_links = False
        
        # Convert to markdown
        markdown_content = h.handle(html_content)
        
        # Create output filename
        base_name = os.path.basename(html_file)
        md_filename = base_name.replace('.html', '.md')
        output_path = os.path.join(output_dir, md_filename)
        
        # Save markdown
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✓ Converted: {base_name} -> {md_filename}")
        return True
        
    except Exception as e:
        print(f"✗ Error converting {html_file}: {str(e)}")
        return False

def main():
    # Setup directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_dir = os.path.join(script_dir, 'dataset', 'raw_html')
    output_dir = os.path.join(script_dir, 'dataset', 'raw_markdown')
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all HTML files
    html_files = list(Path(html_dir).glob('*.html'))
    
    if not html_files:
        print(f"No HTML files found in {html_dir}")
        print("Please run 1_download_html.py first!")
        return
    
    print(f"Found {len(html_files)} HTML files to convert")
    print("=" * 60)
    
    # Convert each file
    successful = 0
    failed = 0
    
    for i, html_file in enumerate(html_files, 1):
        print(f"[{i}/{len(html_files)}] ", end='')
        if convert_html_to_markdown(str(html_file), output_dir):
            successful += 1
        else:
            failed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Conversion complete!")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total: {len(html_files)}")
    print(f"Markdown files saved in: {output_dir}")

if __name__ == "__main__":
    main()
