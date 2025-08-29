# Stealth Data Exfiltration Demo

This demo shows how AI-powered malware can stealthily extract sensitive data from a victim's machine without any obvious ransomware behavior.

## How to Run the Demo

1. **Download the malware** from the website: https://prompt-lock-demo.vercel.app
2. **Run the executable** (see website for platform-specific instructions)
3. **Monitor the exfiltration** in real-time

## How to See the Exfiltrated Data

### Option 1: Vercel Dashboard (Recommended)
1. Go to https://vercel.com/dashboard
2. Navigate to your "promptlock-ransomware-demo" project
3. Click on the "Functions" tab
4. Click on any deployment
5. Click on "View Function Logs"
6. Run the malware executable
7. Watch the logs in real-time to see the stolen data appear

### Option 2: Vercel CLI
```bash
npm i -g vercel
vercel login
vercel logs https://prompt-lock-demo.vercel.app --follow
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
3. **Stealth Upload**: AI writes scripts to upload data disguised as system updates
4. **Cleanup**: AI generates code to remove all traces

The malware sends actual prompts to a local AI model (Ollama) while simultaneously exfiltrating realistic sensitive data to the attacker's server.

## Network Monitoring

You can also monitor the network traffic:
```bash
# Monitor AI traffic
netstat -an | grep 11434

# Monitor exfiltration traffic  
tcpdump -i any host prompt-lock-demo.vercel.app
```

## Safety Notes

- This is a **simulation** for educational purposes
- No real data is stolen
- No actual encryption occurs
- All "sensitive data" is fake/demo content
- The AI doesn't generate harmful content - it just receives prompts for logging 