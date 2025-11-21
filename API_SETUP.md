# Google Gemini API Setup Guide

This guide will help you get started with the Google Gemini API for the FPS Game AI.

## Getting Your API Key

### Step 1: Access Google AI Studio

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Accept the terms of service if prompted

### Step 2: Create an API Key

1. Click on "Get API key" or "Create API key"
2. Select or create a Google Cloud project
3. Your API key will be generated
4. Copy the API key (it looks like: `AIzaSy...`)

### Step 3: Configure the Project

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` in a text editor

3. Add your API key:
   ```
   GEMINI_API_KEY=AIzaSy_your_actual_key_here
   ```

4. Save the file

## API Pricing

Google Gemini API has different pricing tiers:

### Free Tier
- Limited requests per minute
- Good for testing and development
- Rate limits apply

### Paid Tier
- Higher rate limits
- Better for production use
- Pay-as-you-go pricing

Check current pricing at: https://ai.google.dev/pricing

## API Model Options

The default model is `gemini-2.0-flash-exp`:
- Fast responses
- Good for real-time gaming
- Lower cost

Alternative models:
- `gemini-1.5-pro`: More accurate, slower, higher cost
- `gemini-1.5-flash`: Balanced performance

To change the model, edit `gemini_ai.py`:
```python
def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-1.5-flash"):
```

## Usage Limits

Be aware of:

1. **Rate Limits**
   - Requests per minute (RPM)
   - Tokens per minute (TPM)
   - Will throttle if exceeded

2. **Quota**
   - Daily/monthly limits
   - Monitor at Google Cloud Console

3. **Costs**
   - Each screenshot = 1 API request
   - Update interval affects cost
   - Example: 0.5s interval = 120 requests/minute

## Optimizing Costs

1. **Increase Update Interval**
   ```
   AI_UPDATE_INTERVAL=1.0  # Lower frequency
   ```

2. **Reduce Image Quality**
   ```
   SCREENSHOT_QUALITY=75  # Smaller file size
   ```

3. **Limit Session Duration**
   ```bash
   python main.py --duration 300  # 5 minutes max
   ```

4. **Use Smaller Screen Region**
   ```
   SCREEN_REGION_WIDTH=1280
   SCREEN_REGION_HEIGHT=720
   ```

## Monitoring Usage

### Google Cloud Console

1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project
3. Navigate to "APIs & Services" > "Dashboard"
4. View API usage and quotas

### Application Logs

The application logs each API call:
```
2024-11-21 23:30:01 - INFO - Action: aim_adjust | Reasoning: ...
```

Count API calls in logs:
```bash
grep "Action:" session.log | wc -l
```

## Troubleshooting

### "API key not found"
- Check `.env` file exists
- Verify `GEMINI_API_KEY` is set
- No quotes around the key value

### "API key not valid"
- Verify key is correct (copy-paste again)
- Check key hasn't been restricted/deleted
- Ensure you're using Gemini API key (not other Google APIs)

### "Quota exceeded"
- Wait for quota reset (usually 1 minute)
- Increase update interval
- Consider paid tier

### "Rate limit exceeded"
- Slow down requests (increase interval)
- Implement exponential backoff
- Check for multiple instances running

## Security Best Practices

1. **Never Commit API Keys**
   - `.env` is in `.gitignore`
   - Don't share your `.env` file
   - Don't commit hardcoded keys

2. **Restrict API Keys**
   - In Google Cloud Console
   - Set API restrictions
   - Set application restrictions

3. **Monitor Usage**
   - Set up billing alerts
   - Review usage regularly
   - Disable unused keys

4. **Rotate Keys Regularly**
   - Generate new keys periodically
   - Revoke old keys
   - Update `.env` with new key

## Additional Resources

- [Gemini API Documentation](https://ai.google.dev/docs)
- [Python SDK Documentation](https://ai.google.dev/api/python)
- [Pricing Information](https://ai.google.dev/pricing)
- [Rate Limits](https://ai.google.dev/docs/quota)
- [Best Practices](https://ai.google.dev/docs/best_practices)

## Support

For API issues:
- [Google AI Forum](https://discuss.ai.google.dev/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/google-gemini-ai)
- [GitHub Issues](https://github.com/jesse-dot/gemini-master/issues)
