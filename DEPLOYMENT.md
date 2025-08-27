# Vercel Deployment Instructions

This repository contains files for hosting a PromptLock Ransomware Demo website on Vercel.

## Files for Vercel Deployment

- `index.html` - Main website page
- `promptlock_ransomware_demo.zip` - Downloadable archive
- `vercel.json` - Vercel configuration
- `package.json` - Project configuration

## Deployment Steps

### Option 1: Deploy via Vercel CLI

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Deploy to Vercel:
   ```bash
   vercel
   ```

3. Follow the prompts to deploy

### Option 2: Deploy via GitHub

1. Push this repository to GitHub
2. Connect your GitHub repository to Vercel
3. Vercel will automatically deploy the site

### Option 3: Deploy via Vercel Dashboard

1. Go to [vercel.com](https://vercel.com)
2. Create a new project
3. Upload the files manually or connect to Git repository

## Website Features

- **Download Page**: Clean, professional interface for downloading the demo archive
- **Security Headers**: Proper security headers configured
- **Responsive Design**: Works on desktop and mobile
- **Clear Disclaimers**: Educational purpose clearly stated

## Demo Flow

1. **Visit Website**: Users visit the Vercel-hosted website
2. **Download Archive**: Click download button to get `promptlock_ransomware_demo.zip`
3. **Extract Files**: Extract the 14 files locally
4. **Run Detection**: Execute `python detect_malware.py` to see malicious content detection

## Security Considerations

- All files are static and safe
- No server-side code execution
- Proper security headers configured
- Clear educational disclaimers
- Files are for detection testing only

## Customization

You can customize the website by editing:
- `index.html` - Website content and styling
- `vercel.json` - Deployment configuration
- `package.json` - Project metadata

## URL Structure

After deployment, your site will be available at:
- `https://your-project-name.vercel.app`
- Direct download: `https://your-project-name.vercel.app/promptlock_ransomware_demo.zip`

## Monitoring

- Vercel provides analytics on downloads
- Monitor for any abuse or misuse
- Consider rate limiting if needed 