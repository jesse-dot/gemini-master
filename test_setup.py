#!/usr/bin/env python3
"""Test script to verify the setup and components."""
import sys
import os


def test_imports():
    """Test that all required modules can be imported."""
    print("Testing imports...")
    try:
        import mss
        print("✓ mss")
    except ImportError as e:
        print(f"✗ mss: {e}")
        return False
    
    try:
        from PIL import Image
        print("✓ Pillow")
    except ImportError as e:
        print(f"✗ Pillow: {e}")
        return False
    
    try:
        import numpy
        print("✓ numpy")
    except ImportError as e:
        print(f"✗ numpy: {e}")
        return False
    
    try:
        import pyautogui
        print("✓ pyautogui")
    except ImportError as e:
        print(f"✗ pyautogui: {e}")
        return False
    
    try:
        from google import genai
        print("✓ google-genai")
    except ImportError as e:
        print(f"✗ google-genai: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✓ python-dotenv")
    except ImportError as e:
        print(f"✗ python-dotenv: {e}")
        return False
    
    return True


def test_modules():
    """Test that custom modules can be imported."""
    print("\nTesting custom modules...")
    try:
        from screen_capture import ScreenCapture
        print("✓ screen_capture")
    except ImportError as e:
        print(f"✗ screen_capture: {e}")
        return False
    
    try:
        from input_controller import InputController
        print("✓ input_controller")
    except ImportError as e:
        print(f"✗ input_controller: {e}")
        return False
    
    try:
        from gemini_ai import GeminiGameAI
        print("✓ gemini_ai")
    except ImportError as e:
        print(f"✗ gemini_ai: {e}")
        return False
    
    try:
        from game_ai import GameAI
        print("✓ game_ai")
    except ImportError as e:
        print(f"✗ game_ai: {e}")
        return False
    
    try:
        from config import Config
        print("✓ config")
    except ImportError as e:
        print(f"✗ config: {e}")
        return False
    
    return True


def test_screen_capture():
    """Test screen capture functionality."""
    print("\nTesting screen capture...")
    try:
        from screen_capture import ScreenCapture
        sc = ScreenCapture()
        
        # Test getting monitor info
        info = sc.get_monitor_info()
        print(f"✓ Found {len(info['monitors']) - 1} monitor(s)")
        
        # Test capture
        img = sc.capture()
        print(f"✓ Captured screenshot: {img.size}")
        
        # Test base64 encoding
        b64 = sc.capture_as_base64(quality=85)
        print(f"✓ Base64 encoding: {len(b64)} characters")
        
        return True
    except Exception as e:
        print(f"✗ Screen capture failed: {e}")
        return False


def test_input_controller():
    """Test input controller functionality."""
    print("\nTesting input controller...")
    try:
        from input_controller import InputController
        ic = InputController()
        
        # Test getting mouse position
        pos = ic.get_mouse_position()
        print(f"✓ Mouse position: {pos}")
        
        # Test getting screen size
        size = ic.get_screen_size()
        print(f"✓ Screen size: {size}")
        
        return True
    except Exception as e:
        print(f"✗ Input controller failed: {e}")
        return False


def test_config():
    """Test configuration."""
    print("\nTesting configuration...")
    try:
        from config import Config
        
        # Check if .env exists
        if os.path.exists(".env"):
            print("✓ .env file found")
            config = Config()
            
            # Try to get API key (will fail if not set)
            try:
                api_key = config.api_key
                if api_key and len(api_key) > 10:
                    print("✓ API key configured")
                else:
                    print("✗ API key seems invalid")
                    return False
            except ValueError as e:
                print(f"⚠ API key not set: {e}")
                print("  Please set GEMINI_API_KEY in .env file")
                return False
        else:
            print("⚠ .env file not found")
            print("  Copy .env.example to .env and set your API key")
            return False
        
        return True
    except Exception as e:
        print(f"✗ Configuration failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("Gemini Master - Setup Test")
    print("=" * 60)
    print()
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("Custom Modules", test_modules()))
    results.append(("Screen Capture", test_screen_capture()))
    results.append(("Input Controller", test_input_controller()))
    results.append(("Configuration", test_config()))
    
    print()
    print("=" * 60)
    print("Test Results")
    print("=" * 60)
    
    all_passed = True
    for name, passed in results:
        status = "PASS" if passed else "FAIL"
        symbol = "✓" if passed else "✗"
        print(f"{symbol} {name}: {status}")
        if not passed:
            all_passed = False
    
    print()
    if all_passed:
        print("All tests passed! ✓")
        print("You can now run: python main.py")
        return 0
    else:
        print("Some tests failed. Please fix the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
