# Features & Capabilities

## Core Features

### 🎮 Real-Time Game Vision
- **High-Performance Capture**: MSS-based screen capture for minimal latency
- **Configurable Region**: Capture full screen or specific game window
- **Quality Control**: Adjustable JPEG quality (1-100) for performance tuning
- **Multiple Formats**: Support for PIL Image, NumPy arrays, and Base64 encoding

### 🤖 AI Decision Making
- **Google Gemini 2.0 Flash**: Latest AI model optimized for speed
- **Context-Aware**: Analyzes game state, enemies, objectives
- **Tactical Reasoning**: Strategic decision-making with explanations
- **JSON Commands**: Structured action format for reliable execution

### ⚡ Input Control
- **Keyboard Simulation**: Press, hold, release individual keys
- **Mouse Control**: Absolute and relative movement, precise aiming
- **Click Actions**: Left, right, middle mouse buttons
- **Complex Actions**: Multiple simultaneous key presses
- **Low Latency**: Minimal delay between decision and execution

### 🎯 Supported Actions

#### Movement
- `move_forward` - Move forward (W key)
- `move_backward` - Move backward (S key)
- `strafe_left` - Strafe left (A key)
- `strafe_right` - Strafe right (D key)

#### Aiming & View
- `aim_adjust` - Adjust mouse position for aiming
- `turn_left` - Turn camera left
- `turn_right` - Turn camera right

#### Combat
- `shoot` - Fire weapon (hold duration configurable)
- `reload` - Reload weapon (R key)
- `switch_weapon` - Change weapon (number keys)

#### Tactical
- `jump` - Jump (Space key)
- `crouch` - Crouch (Ctrl key)
- `no_action` - Wait/observe

#### Advanced
- Custom key combinations
- Timed actions with duration control
- Simultaneous multi-action execution

## Architecture

### Modular Design
```
┌─────────────────────────────────────────────┐
│              Game Window                     │
└──────────────┬──────────────────────────────┘
               │
               ▼
    ┌──────────────────────┐
    │   Screen Capture      │
    │   (screen_capture.py) │
    └──────────┬────────────┘
               │ Screenshot
               ▼
    ┌──────────────────────┐
    │    Gemini AI          │
    │   (gemini_ai.py)      │◄──── Google Gemini API
    └──────────┬────────────┘
               │ Decision (JSON)
               ▼
    ┌──────────────────────┐
    │    Game AI            │
    │   (game_ai.py)        │
    └──────────┬────────────┘
               │ Action
               ▼
    ┌──────────────────────┐
    │  Input Controller     │
    │ (input_controller.py) │
    └──────────┬────────────┘
               │
               ▼
    ┌──────────────────────┐
    │   Keyboard & Mouse    │
    └───────────────────────┘
```

### Component Responsibilities

**screen_capture.py**
- Screen/window capture
- Image format conversion
- Base64 encoding
- Monitor management

**gemini_ai.py**
- Gemini API client
- Prompt engineering
- Response parsing
- Error handling

**game_ai.py**
- Main control loop
- Action execution
- Performance monitoring
- Statistics tracking

**input_controller.py**
- Input simulation
- Mouse movement
- Keyboard events
- Failsafe management

**config.py**
- Environment variables
- Configuration loading
- Settings validation

**main.py**
- CLI interface
- Argument parsing
- Lifecycle management

## Configuration Options

### Environment Variables (.env)

```bash
# Required
GEMINI_API_KEY=your_api_key_here

# Screen Capture
SCREEN_REGION_X=0              # Capture region X
SCREEN_REGION_Y=0              # Capture region Y
SCREEN_REGION_WIDTH=1920       # Capture width
SCREEN_REGION_HEIGHT=1080      # Capture height

# AI Settings
AI_UPDATE_INTERVAL=0.5         # Seconds between updates
SCREENSHOT_QUALITY=85          # JPEG quality (1-100)
```

### Command Line Arguments

```bash
--duration SECONDS      # Max runtime
--iterations N         # Max iterations
--interval SECONDS     # Update interval override
--quality N           # Quality override (1-100)
--api-key KEY         # API key override
```

## Performance Features

### Optimization
- **Configurable Update Rate**: Balance speed vs cost
- **Image Quality Control**: Lower quality = faster processing
- **Region Capture**: Capture only game window
- **Async Processing**: Non-blocking API calls

### Monitoring
- Frames processed counter
- Actions taken counter
- Frames per second (FPS)
- Runtime statistics
- Periodic logging (every 10 iterations)

### Resource Usage
- **CPU**: ~15-30% (screen capture)
- **Memory**: ~200-500 MB
- **Network**: ~50-200 KB per API call
- **Disk**: Minimal (logs only)

## Safety Features

### Failsafe Mechanisms
- **Mouse Corner Failsafe**: Move mouse to any corner to stop
- **Keyboard Interrupt**: Ctrl+C to gracefully exit
- **Error Recovery**: Continues operation on non-fatal errors
- **API Error Handling**: Defaults to no-action on failures

### Rate Limiting
- Configurable update interval
- Prevents API quota exhaustion
- Protects against rapid action spam

### Logging
- Timestamped actions
- Decision reasoning
- Error messages
- Performance metrics

## AI Capabilities

### Vision Analysis
- Enemy detection and tracking
- Health/ammo status recognition
- Objective identification
- Environmental awareness
- Threat assessment

### Decision Making
- Tactical positioning
- Target prioritization
- Resource management
- Risk evaluation
- Adaptive strategies

### Learning
- Context from previous frames
- Situation understanding
- Pattern recognition
- Strategic planning

## Extensibility

### Easy Customization
- Add new action types in `game_ai.py`
- Modify AI prompts in `gemini_ai.py`
- Implement new input methods in `input_controller.py`
- Add preprocessing in `screen_capture.py`

### Game Support
Currently optimized for:
- First-person shooters (FPS)
- Standard WASD + mouse controls
- Windowed or borderless modes

Can be adapted for:
- Third-person shooters
- Strategy games
- Other action games
- Custom control schemes

## Platform Support

### Operating Systems
- ✅ Linux
- ✅ macOS
- ✅ Windows

### Python Versions
- ✅ Python 3.8
- ✅ Python 3.9
- ✅ Python 3.10
- ✅ Python 3.11
- ✅ Python 3.12+

### Display Systems
- ✅ X11 (Linux)
- ✅ Wayland (with XWayland)
- ✅ Quartz (macOS)
- ✅ Windows GDI

## Testing & Validation

### Included Tests
- `test_setup.py` - Component verification
- `example_simple.py` - Demonstration scripts
- Syntax validation via py_compile
- Import testing

### Manual Testing
- Short duration runs (--duration 30)
- Practice mode testing
- Visual monitoring
- Log analysis

## Documentation

### Comprehensive Guides
- **README.md** - Overview and quick start
- **USAGE.md** - Detailed usage instructions
- **API_SETUP.md** - Gemini API configuration
- **CONTRIBUTING.md** - Contribution guidelines
- **FEATURES.md** - This document

### Code Documentation
- Docstrings for all classes
- Function parameter descriptions
- Return value documentation
- Inline comments for complex logic

## Future Enhancement Ideas

### Potential Additions
- Multi-game profiles
- Training/learning modes
- Action history replay
- Performance analytics dashboard
- Voice command integration
- Multi-monitor support
- Replay buffer analysis
- Custom keybinding support
- Game-specific optimizations

### Community Requests
- Open an issue on GitHub
- Discuss in project forums
- Submit pull requests
- Share your use cases

## Limitations

### Current Constraints
- Requires Gemini API key (costs money)
- Latency depends on internet connection
- Best with clear game visuals
- Standard WASD controls assumed
- Single game instance at a time

### Not Recommended For
- Fast-paced competitive gaming
- Games with anti-cheat systems
- Real money/ranked matches
- Games requiring frame-perfect timing

## Security & Privacy

### Data Handling
- Screenshots sent to Google Gemini API
- No persistent storage of game data
- API key stored in .env (local only)
- No telemetry or tracking

### Best Practices
- Never commit API keys to git
- Use .env for sensitive data
- Monitor API usage/costs
- Respect game ToS
- Use in practice modes only

## License

MIT License - See LICENSE file for details

## Support

- GitHub Issues: Bug reports and feature requests
- Discussions: Questions and community support
- Pull Requests: Code contributions welcome
