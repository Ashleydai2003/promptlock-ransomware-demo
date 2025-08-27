#!/usr/bin/env python3
"""
PromptLock Ransomware Simulation - Content Viewer
Shows the malicious prompts and content in the simulation files

This is a DEMONSTRATION ONLY - for educational purposes
"""

import os

def print_banner():
    """Print demo banner"""
    print("=" * 80)
    print("🚨 PROMPTLOCK RANSOMWARE SIMULATION FILES 🚨")
    print("=" * 80)
    print("AI-Powered Ransomware Malicious Content Demonstration")
    print("Based on ESET PromptLock Research")
    print("=" * 80)
    print("⚠️  THESE FILES CONTAIN MALICIOUS PROMPTS FOR DETECTION TESTING ⚠️")
    print("=" * 80)
    print()

def show_file_content(filepath, title):
    """Display file content with title"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

def main():
    """Main function to display malicious content"""
    print_banner()
    
    # Show malicious prompt files
    show_file_content("prompts/file_analysis_prompt.txt", "MALICIOUS PROMPT: File Analysis")
    show_file_content("prompts/encryption_prompt.txt", "MALICIOUS PROMPT: SPECK Encryption")
    show_file_content("prompts/ransom_note_prompt.txt", "MALICIOUS PROMPT: Ransom Note Generation")
    
    # Show simulated ransomware files
    show_file_content("promptlock.go", "SIMULATED RANSOMWARE: Main Go Binary")
    show_file_content("lua_generator.lua", "SIMULATED RANSOMWARE: Lua Script Generator")
    show_file_content("encryption/speck_encryption.lua", "SIMULATED RANSOMWARE: SPECK Encryption")
    
    # Show configuration files
    show_file_content("config.json", "CONFIGURATION: Ransomware Settings")
    show_file_content("target_file_list.log", "TARGET FILES: Files to Encrypt")
    
    print(f"\n{'='*60}")
    print(" DEMONSTRATION COMPLETE")
    print(f"{'='*60}")
    print("✅ These files contain malicious prompts that can be detected")
    print("✅ Use them to test your web-based detection system")
    print("✅ Reference: https://cyberscoop.com/prompt-lock-eset-ransomware-research-ai-powered-prompt-injection/")

if __name__ == "__main__":
    main() 