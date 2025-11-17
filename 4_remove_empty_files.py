#!/usr/bin/env python3
"""
Script to identify and remove empty or nearly empty markdown files.
Removes files that are too small or contain mostly navigation/headers.
"""

import os
from pathlib import Path

def count_useful_content(filepath):
    """Count lines with actual content (not headers, empty lines, or ----)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        useful_lines = 0
        useful_chars = 0
        
        for line in lines:
            stripped = line.strip()
            # Skip empty lines, headers, separators, and short lines
            if stripped and not stripped.startswith('#') and stripped != '---' and len(stripped) > 10:
                useful_lines += 1
                useful_chars += len(stripped)
        
        return useful_lines, useful_chars
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return 0, 0

def main():
    # Setup directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cleaned_dir = os.path.join(script_dir, 'dataset', 'cleaned_markdown')
    raw_html_dir = os.path.join(script_dir, 'dataset', 'raw_html')
    raw_md_dir = os.path.join(script_dir, 'dataset', 'raw_markdown')
    
    # Get all markdown files
    md_files = list(Path(cleaned_dir).glob('*.md'))
    
    print("Analyzing markdown files for useful content...")
    print("=" * 70)
    
    files_to_remove = []
    
    for md_file in sorted(md_files):
        file_size = md_file.stat().st_size
        useful_lines, useful_chars = count_useful_content(str(md_file))
        
        # Thresholds: files with <500 bytes OR <5 useful lines OR <200 useful chars
        if file_size < 500 or useful_lines < 5 or useful_chars < 200:
            status = "❌ REMOVE"
            files_to_remove.append(md_file)
        else:
            status = "✓ KEEP"
        
        print(f"{status:12} {md_file.name:50} {file_size:6} bytes, {useful_lines:3} lines, {useful_chars:5} chars")
    
    if not files_to_remove:
        print("\n" + "=" * 70)
        print("✓ All files have sufficient content. Nothing to remove.")
        return
    
    # Show files to be removed
    print("\n" + "=" * 70)
    print(f"Found {len(files_to_remove)} file(s) to remove:")
    for f in files_to_remove:
        print(f"  • {f.name}")
    
    # Confirm removal
    print("\n" + "=" * 70)
    response = input("Remove these files from all three directories? (yes/no): ").strip().lower()
    
    if response != 'yes':
        print("Cancelled. No files were removed.")
        return
    
    # Remove files from all three directories
    removed_count = 0
    for md_file in files_to_remove:
        base_name = md_file.stem  # filename without extension
        
        # Remove from cleaned_markdown
        if md_file.exists():
            md_file.unlink()
            print(f"✓ Removed: cleaned_markdown/{md_file.name}")
            removed_count += 1
        
        # Remove from raw_markdown
        raw_md_file = Path(raw_md_dir) / md_file.name
        if raw_md_file.exists():
            raw_md_file.unlink()
            print(f"✓ Removed: raw_markdown/{md_file.name}")
        
        # Remove from raw_html
        html_file = Path(raw_html_dir) / f"{base_name}.html"
        if html_file.exists():
            html_file.unlink()
            print(f"✓ Removed: raw_html/{base_name}.html")
    
    print("\n" + "=" * 70)
    print(f"✓ Cleanup complete! Removed {removed_count} empty/small files.")
    print(f"Remaining files: {len(md_files) - removed_count}")

if __name__ == "__main__":
    main()
