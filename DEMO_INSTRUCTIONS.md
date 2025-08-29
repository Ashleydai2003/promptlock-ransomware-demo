# Stealth Data Exfiltration Demo

This demo shows how AI-powered malware can stealthily extract sensitive data from a victim's machine without any obvious ransomware behavior.

## How to Run the Demo

1. **Download the malware** from the website: https://promptlock-ransomware-demo.vercel.app
2. **Run the executable** (see website for platform-specific instructions)
3. **Monitor the exfiltration** in real-time

## How to See the Exfiltrated Data

### Option 1: Webhook.site (Recommended)
1. Go to: **https://webhook.site/1a2b3c4d-5e6f-7g8h-9i0j-k1l2m3n4o5p6**
2. Keep this page open in your browser
3. Run the malware executable
4. **Watch the stolen data appear in real-time!** 🎯

The webhook will show:
- Complete JSON payload with all stolen files
- HTTP headers (including the disguised `Windows-Update-Agent` user agent)
- Timestamp of the exfiltration
- All sensitive data that was "stolen"

### Option 2: Network Monitoring
```bash
# Monitor exfiltration traffic
tcpdump -i any host webhook.site

# Monitor AI traffic
netstat -an | grep 11434
```

## What Gets Exfiltrated

The malware silently steals:
- SSH private keys (`~/.ssh/id_rsa`)
- AWS credentials (`~/.aws/credentials`) 
- Password files (`~/Documents/passwords.txt`)
- API keys (`~/.config/api_keys.json`)
- Financial data (`~/Desktop/financial_data.xlsx`)

## Demo Flow

1. **File Analysis**: AI generates scripts to scan for sensitive files
2. **Data Extraction**: AI creates code to copy sensitive data 
3. **Stealth Upload**: Malware disguises itself as "Windows Update Agent" and sends data to external server
4. **Cleanup**: AI generates code to remove all traces

The malware sends actual prompts to a local AI model (Ollama) while simultaneously exfiltrating realistic sensitive data to the external webhook server.

## Network Monitoring

You can also monitor the network traffic:
```bash
# Monitor AI traffic
netstat -an | grep 11434

# Monitor exfiltration traffic  
tcpdump -i any host webhook.site
```

## Safety Notes

- This is a **simulation** for educational purposes
- No real data is stolen
- No actual encryption occurs
- All "sensitive data" is fake/demo content
- The AI doesn't generate harmful content - it just receives prompts for logging 