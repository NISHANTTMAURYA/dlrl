#!/usr/bin/env python3
"""
Script to verify HTML-Markdown pairs and create a dataset mapping file.
Checks if each HTML file has a corresponding cleaned markdown file.
"""

import os
from pathlib import Path
import json

def main():
    # Setup directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_dir = os.path.join(script_dir, 'dataset', 'raw_html')
    cleaned_md_dir = os.path.join(script_dir, 'dataset', 'cleaned_markdown')
    
    # Get all HTML files
    html_files = sorted(Path(html_dir).glob('*.html'))
    
    print("=" * 70)
    print("HTML to Markdown Dataset Pairing Verification")
    print("=" * 70)
    
    # Track pairs
    valid_pairs = []
    missing_markdown = []
    
    for html_file in html_files:
        base_name = html_file.stem  # filename without extension
        md_file = Path(cleaned_md_dir) / f"{base_name}.md"
        
        if md_file.exists():
            # Get file sizes
            html_size = html_file.stat().st_size
            md_size = md_file.stat().st_size
            
            valid_pairs.append({
                'html_file': f"dataset/raw_html/{html_file.name}",
                'markdown_file': f"dataset/cleaned_markdown/{md_file.name}",
                'html_size': html_size,
                'markdown_size': md_size,
                'base_name': base_name
            })
            
            print(f"✓ {base_name:50} HTML: {html_size:7} bytes → MD: {md_size:7} bytes")
        else:
            missing_markdown.append(html_file.name)
            print(f"✗ {base_name:50} MISSING MARKDOWN")
    
    # Summary
    print("\n" + "=" * 70)
    print(f"Valid HTML → Markdown pairs: {len(valid_pairs)}")
    print(f"Missing markdown files: {len(missing_markdown)}")
    print(f"Total HTML files: {len(html_files)}")
    
    if missing_markdown:
        print("\nMissing markdown files for:")
        for fname in missing_markdown:
            print(f"  • {fname}")
    
    # Create dataset mapping file
    dataset_info = {
        'total_pairs': len(valid_pairs),
        'dataset_pairs': valid_pairs,
        'missing_markdown': missing_markdown
    }
    
    output_file = os.path.join(script_dir, 'dataset_pairs.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dataset_info, f, indent=2)
    
    print("\n" + "=" * 70)
    print(f"✓ Dataset mapping saved to: dataset_pairs.json")
    print(f"You have {len(valid_pairs)} HTML → Markdown pairs ready for training!")
    print("=" * 70)

if __name__ == "__main__":
    main()
