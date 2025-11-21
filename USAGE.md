# Usage Guide

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key**
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

3. **Test Setup**
   ```bash
   python test_setup.py
   ```

4. **Run the AI**
   ```bash
   python main.py
   ```

## Step-by-Step Guide

### 1. Getting a Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your API key
4. Add it to your `.env` file

### 2. Preparing Your Game

1. Launch your FPS game
2. Enter a match or practice mode
3. Set the game to windowed or borderless windowed mode (recommended)
4. Note the game window position if using custom screen region

### 3. Configuring Screen Capture

**Option A: Full Screen (Default)**
- Leave SCREEN_REGION_* variables empty in .env
- The AI will capture your entire primary monitor

**Option B: Custom Region**
- Set the capture region to match your game window:
  ```
  SCREEN_REGION_X=0
  SCREEN_REGION_Y=0
  SCREEN_REGION_WIDTH=1920
  SCREEN_REGION_HEIGHT=1080
  ```

To find your game window coordinates:
```python
from screen_capture import ScreenCapture
sc = ScreenCapture()
print(sc.get_monitor_info())
```

### 4. Running the AI

**Basic Run**
```bash
python main.py
```

**Test Run (30 seconds)**
```bash
python main.py --duration 30
```

**Fast Reactions (0.2s interval)**
```bash
python main.py --interval 0.2
```

**High Quality Screenshots**
```bash
python main.py --quality 95
```

**Limited Iterations**
```bash
python main.py --iterations 50
```

### 5. Monitoring Performance

The AI logs statistics every 10 iterations:
- Iterations: Number of AI decision cycles
- Frames: Number of screenshots captured
- Actions: Number of actions executed
- FPS: Frames processed per second

### 6. Stopping the AI

- **Method 1**: Press `Ctrl+C` in the terminal
- **Method 2**: Move mouse to any screen corner (failsafe)
- **Method 3**: Let it run until --duration or --iterations limit

## Common Use Cases

### Testing in Practice Mode

```bash
# Short test run
python main.py --duration 30 --interval 0.5

# Observe the AI's behavior
# Adjust settings as needed
```

### Competitive Play

```bash
# Lower latency for faster reactions
python main.py --interval 0.3 --quality 75

# Note: Lower intervals increase API costs
```

### Recording Sessions

```bash
# Run for a full match (~15 minutes)
python main.py --duration 900 --interval 0.5 > session.log 2>&1

# Review the log file afterward
```

## Troubleshooting

### AI Not Moving

**Problem**: The AI analyzes frames but doesn't control the game.

**Solutions**:
- Ensure the game window is in focus
- Check that the game accepts keyboard/mouse input
- Verify the game uses standard WASD controls
- Try running as administrator (Windows)

### Actions Too Slow

**Problem**: The AI reacts slowly to game events.

**Solutions**:
- Decrease AI_UPDATE_INTERVAL (e.g., 0.2 or 0.3)
- Lower SCREENSHOT_QUALITY to reduce processing time
- Use a smaller screen region
- Check your internet connection speed

### High API Costs

**Problem**: Using too many API credits.

**Solutions**:
- Increase AI_UPDATE_INTERVAL (e.g., 1.0 or 2.0)
- Lower SCREENSHOT_QUALITY
- Use --duration to limit session length
- Monitor usage at Google Cloud Console

### Screen Capture Issues

**Problem**: Can't capture the game screen.

**Solutions**:
- Run the game in windowed mode
- Check screen capture permissions
- Try capturing full screen instead of region
- Use test_setup.py to verify screen capture works

### API Errors

**Problem**: Getting API errors from Gemini.

**Solutions**:
- Verify your API key is correct
- Check you have API credits/quota
- Ensure you have internet connection
- Try again later if there's an outage

## Advanced Configuration

### Custom Game Controls

Edit `game_ai.py` to match your game's controls:

```python
# Example: Change reload key from 'r' to 'f'
elif action == "reload":
    self.input_controller.press_key("f")
```

### AI Behavior Tuning

Edit `gemini_ai.py` to customize the AI's behavior:

```python
# Make AI more aggressive
temperature=0.3  # Lower = more deterministic

# Make AI more exploratory
temperature=0.7  # Higher = more random
```

### Multiple Action Support

The AI can execute multiple simultaneous actions:

```json
{
  "action": "aim_adjust",
  "parameters": {
    "mouse_dx": 50,
    "mouse_dy": -10,
    "keys": ["w", "shift"],
    "duration": 0.5
  }
}
```

This moves forward while sprinting and adjusting aim.

## Best Practices

1. **Start Small**: Test with short durations first
2. **Monitor Costs**: Keep an eye on API usage
3. **Game Settings**: Use medium graphics for clear visuals
4. **Practice Mode**: Test in bot matches or practice ranges
5. **Permissions**: Ensure the AI has necessary system permissions
6. **Backup Controls**: Keep manual control ready to take over

## Performance Tips

- **CPU**: Screen capture is CPU-intensive; close other apps
- **GPU**: Not heavily used; AI runs on Google's servers
- **Network**: Stable internet connection is crucial
- **RAM**: ~500MB typical usage; more with high-res captures

## Safety Reminders

- The failsafe (mouse to corner) works system-wide
- API calls cost money; monitor your usage
- Comply with game terms of service
- Don't use in ranked/competitive modes without permission
- Test in safe environments first

## Example Session

```
$ python main.py --duration 60 --interval 0.4

============================================================
FPS Game AI - Powered by Google Gemini Live API
============================================================
Update interval: 0.4s
Screenshot quality: 85
Screen region: Full primary monitor

SAFETY: Move mouse to any corner to trigger failsafe stop!

Starting in 3 seconds...
Make sure your game window is visible and focused...

3...
2...
1...
GO!

2024-11-21 23:30:00 - __main__ - INFO - Starting game AI...
2024-11-21 23:30:00 - __main__ - INFO - Update interval: 0.4s
2024-11-21 23:30:01 - __main__ - INFO - Action: aim_adjust | Reasoning: Enemy spotted at 2 o'clock, adjusting aim
2024-11-21 23:30:02 - __main__ - INFO - Action: shoot | Reasoning: Target in crosshairs, engaging
...
```
