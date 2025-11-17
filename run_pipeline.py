#!/usr/bin/env python3
"""
Master script to run the complete data collection pipeline:
1. Download HTML from websites
2. Convert HTML to Markdown
3. Clean and summarize Markdown
"""

import subprocess
import sys
import os

def run_script(script_name, description):
    """Run a Python script and report results."""
    print("\n" + "=" * 70)
    print(f"STEP: {description}")
    print("=" * 70)
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            check=True
        )
        print(f"\n✓ {description} - COMPLETED")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ {description} - FAILED")
        return False

def main():
    print("=" * 70)
    print("HTML to Markdown Dataset Creation Pipeline")
    print("=" * 70)
    print("\nThis pipeline will:")
    print("  1. Download raw HTML from 25 diverse websites")
    print("  2. Convert HTML to raw Markdown")
    print("  3. Clean and summarize Markdown")
    print("\n" + "=" * 70)
    
    input("\nPress Enter to start the pipeline...")
    
    # Step 1: Download HTML
    if not run_script("1_download_html.py", "Downloading HTML from websites"):
        print("\n⚠️  HTML download failed. Please check errors above.")
        return
    
    # Step 2: Convert to Markdown
    if not run_script("2_convert_to_markdown.py", "Converting HTML to Markdown"):
        print("\n⚠️  Markdown conversion failed. Please check errors above.")
        return
    
    # Step 3: Clean Markdown
    if not run_script("3_clean_markdown.py", "Cleaning and summarizing Markdown"):
        print("\n⚠️  Markdown cleaning failed. Please check errors above.")
        return
    
    # Final summary
    print("\n" + "=" * 70)
    print("✓ PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print("\nYour dataset is ready in the following directories:")
    print("  • dataset/raw_html/          - Original HTML files")
    print("  • dataset/raw_markdown/      - Raw markdown conversions")
    print("  • dataset/cleaned_markdown/  - Cleaned markdown (training data)")
    print("\nNext steps:")
    print("  1. Review the cleaned markdown files manually")
    print("  2. Further refine them as needed for your RL model")
    print("  3. Use the HTML→cleaned_markdown pairs as training data")
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
