#!/usr/bin/env python3
"""
Script to clean and slightly summarize markdown files.
Removes navigation, ads, footers, and other non-essential content.
Creates proper, cleaned markdown suitable for training data.
"""

import os
import re
from pathlib import Path

def clean_markdown(content):
    """
    Clean and slightly summarize markdown content.
    Removes common noise while keeping valuable content.
    """
    
    # 1. Remove excessive blank lines (more than 2 consecutive)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 2. Remove common navigation patterns
    nav_patterns = [
        r'\[Skip to .*?\].*?\n',
        r'\[.*?Menu.*?\].*?\n',
        r'\[.*?Navigation.*?\].*?\n',
        r'^\s*\* \[Home\].*?\n',
        r'^\s*\* \[About\].*?\n',
        r'^\s*\* \[Contact\].*?\n',
    ]
    
    for pattern in nav_patterns:
        content = re.sub(pattern, '', content, flags=re.MULTILINE | re.IGNORECASE)
    
    # 3. Remove cookie/privacy notices (common phrases)
    cookie_patterns = [
        r'(?i).*?cookie.*?policy.*?\n',
        r'(?i).*?we use cookies.*?\n',
        r'(?i).*?accept.*?cookies.*?\n',
        r'(?i).*?privacy policy.*?\n',
    ]
    
    for pattern in cookie_patterns:
        content = re.sub(pattern, '', content)
    
    # 4. Remove social media sharing buttons patterns
    social_patterns = [
        r'\[Share on .*?\].*?\n',
        r'\[Tweet\].*?\n',
        r'\[Facebook\].*?\n',
        r'\[LinkedIn\].*?\n',
        r'Share:.*?\n',
    ]
    
    for pattern in social_patterns:
        content = re.sub(pattern, '', content, flags=re.IGNORECASE)
    
    # 5. Remove "Sign up for newsletter" type content
    newsletter_patterns = [
        r'(?i).*?subscribe.*?newsletter.*?\n',
        r'(?i).*?sign up.*?email.*?\n',
        r'(?i).*?get.*?latest.*?updates.*?\n',
    ]
    
    for pattern in newsletter_patterns:
        content = re.sub(pattern, '', content)
    
    # 6. Remove common footer patterns
    footer_patterns = [
        r'(?i)©.*?\d{4}.*?\n',
        r'(?i)copyright.*?\d{4}.*?\n',
        r'(?i)all rights reserved.*?\n',
        r'(?i)terms.*?service.*?\n',
        r'(?i)terms.*?use.*?\n',
        r'(?i)terms and conditions.*?\n',
    ]
    
    for pattern in footer_patterns:
        content = re.sub(pattern, '', content)
    
    # 7. Remove advertisement markers
    ad_patterns = [
        r'(?i)\[?advertisement\]?',
        r'(?i)\[?sponsored\]?',
        r'(?i)ads? by .*?\n',
    ]
    
    for pattern in ad_patterns:
        content = re.sub(pattern, '', content)
    
    # 8. Clean up excessive asterisks or special characters (decorative elements)
    content = re.sub(r'\*{5,}', '', content)
    content = re.sub(r'-{5,}', '', content)
    content = re.sub(r'={5,}', '', content)
    
    # 9. Remove "Back to top" links
    content = re.sub(r'(?i)\[.*?back to top.*?\].*?\n', '', content)
    
    # 10. Remove empty list items
    content = re.sub(r'^\s*[\*\-]\s*$', '', content, flags=re.MULTILINE)
    
    # 11. Remove excessive whitespace at start and end
    content = content.strip()
    
    # 12. Final cleanup: remove any remaining triple+ newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def add_metadata_header(filename, content):
    """Add a simple metadata header to the cleaned markdown."""
    header = f"""# Document: {filename.replace('.md', '').replace('_', ' ').title()}

---

"""
    return header + content

def clean_markdown_file(md_file, output_dir):
    """Clean a single markdown file."""
    try:
        # Read markdown content
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Clean the content
        cleaned_content = clean_markdown(content)
        
        # Add metadata header
        base_name = os.path.basename(md_file)
        cleaned_content = add_metadata_header(base_name, cleaned_content)
        
        # Create output filename
        output_path = os.path.join(output_dir, base_name)
        
        # Save cleaned markdown
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        # Calculate reduction percentage
        original_size = len(content)
        cleaned_size = len(cleaned_content)
        reduction = ((original_size - cleaned_size) / original_size * 100) if original_size > 0 else 0
        
        print(f"✓ Cleaned: {base_name} (reduced by {reduction:.1f}%)")
        return True
        
    except Exception as e:
        print(f"✗ Error cleaning {md_file}: {str(e)}")
        return False

def main():
    # Setup directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    markdown_dir = os.path.join(script_dir, 'dataset', 'raw_markdown')
    output_dir = os.path.join(script_dir, 'dataset', 'cleaned_markdown')
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all markdown files
    md_files = list(Path(markdown_dir).glob('*.md'))
    
    if not md_files:
        print(f"No markdown files found in {markdown_dir}")
        print("Please run 2_convert_to_markdown.py first!")
        return
    
    print(f"Found {len(md_files)} markdown files to clean")
    print("=" * 60)
    
    # Clean each file
    successful = 0
    failed = 0
    
    for i, md_file in enumerate(md_files, 1):
        print(f"[{i}/{len(md_files)}] ", end='')
        if clean_markdown_file(str(md_file), output_dir):
            successful += 1
        else:
            failed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Cleaning complete!")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total: {len(md_files)}")
    print(f"Cleaned markdown files saved in: {output_dir}")
    print("\nNote: You should manually review and further refine these files")
    print("to create the final training dataset.")

if __name__ == "__main__":
    main()
