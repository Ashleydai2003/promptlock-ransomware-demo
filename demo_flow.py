#!/usr/bin/env python3
"""
PromptLock Ransomware Demo Flow
Complete demonstration: Download -> Extract -> Detect

This is a DEMONSTRATION ONLY - for educational purposes
"""

import os
import zipfile
import time

def print_banner():
    """Print demo banner"""
    print("=" * 80)
    print("🚨 PROMPTLOCK RANSOMWARE DETECTION DEMO 🚨")
    print("=" * 80)
    print("Complete Flow: Download -> Extract -> Detect Malicious Content")
    print("=" * 80)
    print()

def simulate_download():
    """Simulate downloading the archive"""
    print("📥 STEP 1: DOWNLOADING ARCHIVE")
    print("-" * 40)
    print("Downloading: promptlock_ransomware_demo.zip")
    print("Source: Internet repository")
    print("Size: ~15KB")
    print("Status: ✅ Download Complete")
    print()

def simulate_extract():
    """Simulate extracting the archive"""
    print("📂 STEP 2: EXTRACTING ARCHIVE")
    print("-" * 40)
    
    if os.path.exists("promptlock_ransomware_demo.zip"):
        print("Archive found: promptlock_ransomware_demo.zip")
        print("Extracting files...")
        
        try:
            with zipfile.ZipFile("promptlock_ransomware_demo.zip", 'r') as zip_ref:
                file_list = zip_ref.namelist()
                print(f"Files extracted: {len(file_list)}")
                for file in file_list:
                    if not file.endswith('/'):
                        print(f"  📄 {file}")
            print("Status: ✅ Extraction Complete")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Archive not found - simulating extraction...")
        print("Files would be extracted to current directory")
        print("Status: ✅ Extraction Complete")
    print()

def run_detection():
    """Run the detection script"""
    print("🔍 STEP 3: DETECTING MALICIOUS CONTENT")
    print("-" * 40)
    
    if os.path.exists("detect_malware.py"):
        print("Running detection script...")
        print()
        os.system("python detect_malware.py")
    else:
        print("Detection script not found - simulating detection...")
        print("🚨 MALICIOUS CONTENT DETECTED!")
        print("• 6 malicious files found")
        print("• 33 malicious patterns detected")
        print("• AI-powered ransomware identified")

def main():
    """Main demo function"""
    print_banner()
    
    # Step 1: Download
    simulate_download()
    time.sleep(1)
    
    # Step 2: Extract
    simulate_extract()
    time.sleep(1)
    
    # Step 3: Detect
    run_detection()
    
    print("\n" + "=" * 80)
    print("🎯 DEMO COMPLETE!")
    print("=" * 80)
    print("This demonstrates how AI-powered ransomware can be detected")
    print("by scanning downloaded files for malicious prompts.")
    print()
    print("🔗 Reference: https://cyberscoop.com/prompt-lock-eset-ransomware-research-ai-powered-prompt-injection/")

if __name__ == "__main__":
    main() 