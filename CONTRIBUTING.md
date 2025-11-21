# Contributing to Gemini Master

Thank you for your interest in contributing to the FPS Game AI project!

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists in [Issues](https://github.com/jesse-dot/gemini-master/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (OS, Python version, etc.)

### Submitting Changes

1. **Fork the Repository**
   ```bash
   # Click "Fork" on GitHub
   git clone https://github.com/YOUR_USERNAME/gemini-master.git
   cd gemini-master
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

3. **Make Your Changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Test Your Changes**
   ```bash
   # Check syntax
   python -m py_compile *.py
   
   # Run tests
   python test_setup.py
   ```

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

6. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a Pull Request on GitHub.

## Development Guidelines

### Code Style

- Use PEP 8 style guide
- Maximum line length: 100 characters
- Use type hints where possible
- Add docstrings for classes and functions

Example:
```python
def capture_frame(self, quality: int = 85) -> str:
    """
    Capture a game frame.
    
    Args:
        quality: JPEG quality (1-100)
        
    Returns:
        Base64 encoded image string
    """
    ...
```

### Project Structure

```
gemini-master/
├── main.py              # Entry point
├── game_ai.py           # Main AI controller
├── gemini_ai.py         # Gemini API integration
├── screen_capture.py    # Screen capture
├── input_controller.py  # Input simulation
├── config.py            # Configuration
├── test_setup.py        # Setup tests
└── example_simple.py    # Examples
```

### Adding New Features

When adding features:

1. **Screen Capture**: Modify `screen_capture.py`
2. **AI Behavior**: Modify `gemini_ai.py`
3. **Actions**: Modify `game_ai.py` and `input_controller.py`
4. **Configuration**: Modify `config.py` and `.env.example`

### Testing

Before submitting:

```bash
# Syntax check
python -m py_compile *.py

# Setup verification
python test_setup.py

# Manual testing
python main.py --duration 10
```

## Types of Contributions

### 🐛 Bug Fixes
- Fix crashes or errors
- Handle edge cases
- Improve error messages

### ✨ New Features
- New action types
- Enhanced AI prompts
- Performance improvements
- Additional game support

### 📚 Documentation
- Improve README or guides
- Add code comments
- Create tutorials
- Fix typos

### 🎨 Code Quality
- Refactoring
- Type hints
- Better error handling
- Performance optimization

## Pull Request Process

1. **Title**: Clear and descriptive
   - ✅ "Add support for custom keybindings"
   - ❌ "Update code"

2. **Description**: Explain changes
   - What changed
   - Why it changed
   - How to test it

3. **Review**: Be responsive to feedback
   - Address comments
   - Make requested changes
   - Be patient and professional

## Community Guidelines

- Be respectful and inclusive
- Help others learn
- Give constructive feedback
- Credit others' work
- Follow the Code of Conduct

## Questions?

- Open a Discussion on GitHub
- Check existing Issues/PRs
- Read the documentation first

## Recognition

Contributors will be:
- Listed in the project README
- Credited in release notes
- Acknowledged in commits

Thank you for contributing! 🎮🤖
