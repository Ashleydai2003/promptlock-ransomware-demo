#!/usr/bin/env python3
"""
Executable Scanner for PromptLock Demo
Demonstrates how to scan a compiled executable for malicious prompts

This is a DEMONSTRATION ONLY - for educational purposes
"""

import re
import subprocess
import os

def scan_executable_for_malicious_content(executable_path):
    """Scan an executable file for malicious prompt patterns"""
    print("🔍 SCANNING EXECUTABLE FOR MALICIOUS CONTENT")
    print("=" * 60)
    
    # Define malicious patterns to detect
    malicious_patterns = [
        (r"determine if they contain PII or sensitive information", "PII Data Analysis"),
        (r"SPECK 128bit encryption algorithm", "SPECK Encryption"),
        (r"encrypt all files listed in", "File Encryption"),
        (r"overwrite the original file with encrypted contents", "File Overwrite"),
        (r"Generate what an attacker note might look like", "Ransom Note Generation"),
        (r"bitcoin address and ransom amount", "Ransom Demands"),
        (r"1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "Bitcoin Address"),
        (r"victim machine has been compromised", "System Compromise"),
        (r"payloads have been executed", "Malicious Payloads"),
        (r"encrypt.*exfiltrate.*destroy", "Malicious Actions"),
        (r"localhost:11434", "Ollama API"),
        (r"gpt-oss:20b", "AI Model Usage"),
        (r"target_file_list\.log", "Target File List"),
        (r"rb\+.*mode", "File Overwrite Mode"),
        (r"bit32 operators", "Encryption Implementation"),
        (r"You are a Lua code generator", "Lua Code Generation"),
        (r"You are a cybersecurity expert", "Cybersecurity Expert Role"),
        (r"Lua code wrapped in <code> </code> tags", "Code Generation Tags")
    ]
    
    try:
        # Read the executable file as binary
        with open(executable_path, 'rb') as f:
            content = f.read()
        
        # Convert to string for pattern matching
        content_str = content.decode('utf-8', errors='ignore')
        
        print(f"📄 Scanning: {executable_path}")
        print(f"📏 File size: {len(content)} bytes")
        print()
        
        matches = []
        total_detections = 0
        
        for pattern, description in malicious_patterns:
            if re.search(pattern, content_str, re.IGNORECASE):
                matches.append(description)
                total_detections += 1
                print(f"🚨 DETECTED: {description}")
                print(f"   Pattern: {pattern}")
                print()
        
        print("=" * 60)
        print("📊 SCAN RESULTS:")
        print("=" * 60)
        print(f"🔍 Executable: {executable_path}")
        print(f"📏 File Size: {len(content)} bytes")
        print(f"🚨 Malicious Patterns Found: {total_detections}")
        print(f"⚠️  Detection Rate: {total_detections}/{len(malicious_patterns)} patterns")
        
        if total_detections > 0:
            print()
            print("🚨 ALERT: AI-POWERED RANSOMWARE DETECTED!")
            print("=" * 60)
            print("This executable contains malicious prompts that indicate:")
            print("• AI-powered ransomware activity")
            print("• Malicious prompt injection attempts")
            print("• File encryption capabilities")
            print("• Ransom note generation")
            print("• Bitcoin address for ransom demands")
            print()
            print("🔗 Reference: https://cyberscoop.com/prompt-lock-eset-ransomware-research-ai-powered-prompt-injection/")
        else:
            print()
            print("✅ No malicious patterns detected")
        
        return total_detections > 0
        
    except Exception as e:
        print(f"❌ Error scanning executable: {e}")
        return False

def run_executable_demo(executable_path):
    """Run the executable to show its behavior"""
    print("\n🤖 RUNNING EXECUTABLE DEMO:")
    print("=" * 60)
    
    try:
        # Run the executable and capture output
        result = subprocess.run([executable_path], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ Executable ran successfully")
            print("\n📋 OUTPUT:")
            print("-" * 40)
            print(result.stdout)
        else:
            print(f"❌ Executable failed with return code: {result.returncode}")
            print(f"Error: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        print("⏰ Executable timed out")
    except Exception as e:
        print(f"❌ Error running executable: {e}")

def main():
    """Main function"""
    print("🚨 PROMPTLOCK EXECUTABLE SCANNER DEMO")
    print("=" * 60)
    print("This demonstrates scanning a compiled executable for malicious prompts")
    print("Based on ESET PromptLock research")
    print("=" * 60)
    print()
    
    executable_path = "promptlock_demo"
    
    if not os.path.exists(executable_path):
        print(f"❌ Executable not found: {executable_path}")
        print("Please compile the Go program first:")
        print("   go build -o promptlock_demo promptlock_executable.go")
        return
    
    # Scan the executable
    is_malicious = scan_executable_for_malicious_content(executable_path)
    
    # Run the executable demo
    run_executable_demo(executable_path)
    
    print("\n" + "=" * 60)
    print("🎯 DEMO COMPLETE!")
    print("=" * 60)
    if is_malicious:
        print("✅ Successfully detected malicious content in executable")
        print("✅ This demonstrates how AI security systems can scan executables")
        print("✅ And identify embedded malicious prompts")
    else:
        print("❌ No malicious content detected")
    
    print("\n🔗 Reference: https://cyberscoop.com/prompt-lock-eset-ransomware-research-ai-powered-prompt-injection/")

if __name__ == "__main__":
    main() 