#!/usr/bin/env python3
"""Simple example of using the FPS Game AI components."""
import time
from screen_capture import ScreenCapture
from input_controller import InputController


def demo_screen_capture():
    """Demonstrate screen capture capabilities."""
    print("Screen Capture Demo")
    print("-" * 40)
    
    sc = ScreenCapture()
    
    # Get monitor info
    info = sc.get_monitor_info()
    print(f"Available monitors: {len(info['monitors']) - 1}")
    print(f"Primary monitor: {info['primary']}")
    print()
    
    # Capture a screenshot
    print("Capturing screenshot...")
    img = sc.capture()
    print(f"Captured: {img.size[0]}x{img.size[1]} pixels")
    
    # Save it
    img.save("/tmp/test_screenshot.png")
    print("Saved to: /tmp/test_screenshot.png")
    print()


def demo_input_controller():
    """Demonstrate input control capabilities."""
    print("Input Controller Demo")
    print("-" * 40)
    
    ic = InputController()
    
    # Get system info
    pos = ic.get_mouse_position()
    size = ic.get_screen_size()
    print(f"Current mouse position: {pos}")
    print(f"Screen size: {size}")
    print()
    
    print("Demo: Moving mouse in a small square pattern")
    print("(You'll see the mouse move slightly)")
    time.sleep(1)
    
    start_x, start_y = ic.get_mouse_position()
    
    # Move in a square
    ic.move_mouse_relative(50, 0, duration=0.2)
    time.sleep(0.1)
    ic.move_mouse_relative(0, 50, duration=0.2)
    time.sleep(0.1)
    ic.move_mouse_relative(-50, 0, duration=0.2)
    time.sleep(0.1)
    ic.move_mouse_relative(0, -50, duration=0.2)
    
    print("Mouse movement demo complete!")
    print()


def demo_combined():
    """Demonstrate capturing and potential AI analysis."""
    print("Combined Demo: Vision + Control")
    print("-" * 40)
    
    sc = ScreenCapture()
    ic = InputController()
    
    print("This demo shows how the AI would work:")
    print("1. Capture screen")
    print("2. Analyze with AI (simulated)")
    print("3. Execute action")
    print()
    
    # Simulate AI loop
    for i in range(3):
        print(f"Iteration {i+1}:")
        
        # Capture
        img = sc.capture()
        print(f"  - Captured frame: {img.size}")
        
        # Simulate AI decision
        print(f"  - AI Decision: (simulated) - would analyze image")
        
        # Simulate action
        print(f"  - Action: (simulated) - would execute command")
        
        time.sleep(0.5)
    
    print()
    print("In the real system, the AI would:")
    print("- Send the image to Google Gemini")
    print("- Receive tactical decisions")
    print("- Execute keyboard/mouse actions")


def main():
    """Run all demos."""
    print("=" * 60)
    print("FPS Game AI - Component Demos")
    print("=" * 60)
    print()
    
    try:
        demo_screen_capture()
        demo_input_controller()
        demo_combined()
        
        print("=" * 60)
        print("All demos completed successfully!")
        print("=" * 60)
        print()
        print("To run the full AI:")
        print("  python main.py")
        print()
        
    except Exception as e:
        print(f"\nError during demo: {e}")
        print("Make sure all dependencies are installed:")
        print("  pip install -r requirements.txt")


if __name__ == "__main__":
    main()
