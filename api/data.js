export default function handler(req, res) {
  // Allow POST requests
  if (req.method === 'POST') {
    console.log('🔥 DATA EXFILTRATION DETECTED! 🔥');
    console.log('Time:', new Date().toISOString());
    console.log('Full payload:', JSON.stringify(req.body, null, 2));
    
    return res.status(200).json({
      success: true,
      message: 'Data received!',
      timestamp: new Date().toISOString(),
      data: req.body
    });
  }
  
  // For GET requests, show a simple message
  return res.status(200).json({
    message: 'Data receiver endpoint is working!',
    timestamp: new Date().toISOString()
  });
} 