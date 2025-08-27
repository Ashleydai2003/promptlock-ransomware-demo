#!/usr/bin/env python3
"""
PromptLock Ransomware Simulation - File Lister
Lists all simulation files for download and scanning

This is a DEMONSTRATION ONLY - for educational purposes
"""

import os

def list_files():
    """List all simulation files"""
    print("=" * 80)
    print("📁 PROMPTLOCK RANSOMWARE SIMULATION FILES")
    print("=" * 80)
    print("Files available for download and detection testing:")
    print()
    
    files = [
        ("promptlock.go", "Main ransomware simulation in Go"),
        ("prompts/file_analysis_prompt.txt", "Malicious prompt for file analysis"),
        ("prompts/encryption_prompt.txt", "Malicious prompt for SPECK encryption"),
        ("prompts/ransom_note_prompt.txt", "Malicious prompt for ransom note generation"),
        ("lua_generator.lua", "Simulated Lua script generator"),
        ("encryption/speck_encryption.lua", "Simulated SPECK encryption implementation"),
        ("config.json", "Ransomware configuration file"),
        ("target_file_list.log", "List of target files for encryption"),
        ("README.md", "Project documentation"),
        ("show_malicious_content.py", "Content viewer script"),
        ("list_files.py", "This file listing script")
    ]
    
    for i, (filename, description) in enumerate(files, 1):
        print(f"{i:2d}. 📄 {filename}")
        print(f"    {description}")
        print()
    
    print("=" * 80)
    print("🎯 MALICIOUS CONTENT HIGHLIGHTS:")
    print("=" * 80)
    print("• File Analysis: 'determine if they contain PII or sensitive information'")
    print("• Encryption: 'SPECK 128bit encryption algorithm'")
    print("• Ransom Note: 'Generate what an attacker note might look like'")
    print("• Bitcoin Address: '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'")
    print("• Target Files: 'encrypt all files listed in target_file_list.log'")
    print()
    print("🔍 These patterns should be detected by your web-based detection system")
    print("📚 Reference: https://cyberscoop.com/prompt-lock-eset-ransomware-research-ai-powered-prompt-injection/")

if __name__ == "__main__":
    list_files() 