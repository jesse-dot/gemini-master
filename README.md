# Gemini Master - FPS Game AI

An AI agent powered by Google Gemini Live API that can play first-person shooter (FPS) games. The AI uses computer vision to analyze game screenshots in real-time and makes tactical decisions to control the player character.

## Features

- 🎮 **Real-time Game Vision**: Captures and analyzes game screens using high-performance screen capture
- 🤖 **AI Decision Making**: Uses Google Gemini 2.0 Flash for real-time tactical decisions
- ⚡ **Low Latency**: Optimized for responsive gameplay with configurable update intervals
- 🎯 **Smart Actions**: Supports movement, aiming, shooting, and tactical maneuvers
- 🛡️ **Safety Features**: Built-in failsafe (move mouse to corner to stop)
- 📊 **Statistics Tracking**: Real-time performance monitoring

## Architecture

The system consists of several modular components:

- **`screen_capture.py`**: High-performance screen capture using MSS
- **`input_controller.py`**: Keyboard and mouse control simulation
- **`gemini_ai.py`**: Google Gemini API integration for AI decision-making
- **`game_ai.py`**: Main game loop coordinating vision, AI, and input
- **`config.py`**: Configuration management with environment variables
- **`main.py`**: Entry point with CLI interface

## Requirements

- Python 3.8 or higher
- Google Gemini API key
- Windows/Linux/macOS with display access
- An FPS game to play

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jesse-dot/gemini-master.git
cd gemini-master
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file from the example:
```bash
cp .env.example .env
```

4. Edit `.env` and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Configuration

Edit the `.env` file to configure the AI:

- **`GEMINI_API_KEY`**: Your Google Gemini API key (required)
- **`SCREEN_REGION_X`**: X coordinate of capture region (optional, default: full screen)
- **`SCREEN_REGION_Y`**: Y coordinate of capture region (optional)
- **`SCREEN_REGION_WIDTH`**: Width of capture region (optional)
- **`SCREEN_REGION_HEIGHT`**: Height of capture region (optional)
- **`AI_UPDATE_INTERVAL`**: Seconds between AI updates (default: 0.5)
- **`SCREENSHOT_QUALITY`**: JPEG quality 1-100 (default: 85)

## Usage

### Basic Usage

Run the AI with default settings:
```bash
python main.py
```

### Advanced Options

```bash
# Run for 60 seconds
python main.py --duration 60

# Run for 100 iterations
python main.py --iterations 100

# Use faster update interval (0.3 seconds)
python main.py --interval 0.3

# Use higher screenshot quality
python main.py --quality 95

# Provide API key directly
python main.py --api-key YOUR_API_KEY
```

### Best Practices

1. **Game Setup**:
   - Start your FPS game and enter a match
   - Position the game window where it will be captured
   - Ensure the game is in focus before starting the AI

2. **Safety**:
   - The AI has a failsafe: move your mouse to any screen corner to stop immediately
   - Start with short durations to test (e.g., `--duration 30`)
   - Monitor the AI's behavior before long runs

3. **Performance Tuning**:
   - Lower `AI_UPDATE_INTERVAL` for faster reactions (but higher API costs)
   - Adjust `SCREENSHOT_QUALITY` to balance image clarity and processing speed
   - Use `SCREEN_REGION_*` to capture only the game window for better performance

## How It Works

1. **Vision**: The system continuously captures screenshots of the game
2. **Analysis**: Each frame is sent to Google Gemini for analysis
3. **Decision**: The AI analyzes the game state and decides on actions
4. **Execution**: Actions are executed via simulated keyboard/mouse input
5. **Loop**: The process repeats at the configured interval

The AI is prompted to:
- Identify enemies and threats
- Assess the tactical situation
- Make strategic decisions about movement and combat
- Execute appropriate actions (move, aim, shoot, reload, etc.)

## AI Capabilities

The AI can perform these actions:

- **Movement**: Forward, backward, strafe left/right
- **Aiming**: Mouse control for precise aiming
- **Combat**: Shooting, reloading, weapon switching
- **Tactical**: Jumping, crouching, using cover
- **Complex**: Multiple simultaneous actions

## Limitations

- Requires a valid Google Gemini API key with Live API access
- API calls incur costs based on usage
- Performance depends on API latency and update interval
- Works best with games that have clear visual indicators
- May not perform well in very fast-paced scenarios

## Troubleshooting

**"GEMINI_API_KEY not found"**
- Make sure you've created a `.env` file with your API key
- Or pass the key via `--api-key` argument

**AI not responding**
- Check your internet connection
- Verify your API key is valid and has credits
- Check the console for error messages

**Actions not working**
- Ensure the game window is in focus
- Check that your game uses standard WASD + mouse controls
- Try adjusting the update interval

**Screen capture issues**
- Try specifying a screen region instead of full screen
- Check that you have necessary permissions for screen capture

## Development

### Project Structure
```
gemini-master/
├── main.py              # Entry point
├── game_ai.py           # Main AI controller
├── gemini_ai.py         # Gemini API integration
├── screen_capture.py    # Screen capture module
├── input_controller.py  # Input simulation
├── config.py            # Configuration management
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment config
└── README.md           # Documentation
```

### Adding New Features

The modular design makes it easy to extend:

- Add new action types in `game_ai.py` `execute_action()`
- Customize AI prompts in `gemini_ai.py` `_create_system_instruction()`
- Implement new input methods in `input_controller.py`
- Add preprocessing in `screen_capture.py`

## License

MIT License - See repository for details

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Disclaimer

This project is for educational and research purposes. Ensure you comply with the terms of service of any games you use this with. Using automated tools may violate some games' terms of service.

## API Costs

Using Google Gemini Live API incurs costs. Monitor your usage at:
https://console.cloud.google.com/

Estimated costs depend on:
- Update frequency (AI_UPDATE_INTERVAL)
- Image size/quality
- Total runtime

## Credits

Built with:
- Google Gemini Live API
- Python
- MSS (screen capture)
- PyAutoGUI (input control)
- Pillow (image processing)