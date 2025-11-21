"""Input controller module for simulating keyboard and mouse actions."""
import pyautogui
import time
from typing import Tuple, List
from enum import Enum


class MouseButton(Enum):
    """Mouse button types."""
    LEFT = "left"
    RIGHT = "right"
    MIDDLE = "middle"


class InputController:
    """Handles keyboard and mouse input simulation for controlling the game."""
    
    def __init__(self):
        """Initialize the input controller."""
        # Safety feature: allow moving mouse to corners to abort
        pyautogui.FAILSAFE = True
        # Disable pause between actions for faster response
        pyautogui.PAUSE = 0.01
        
    def move_mouse(self, x: int, y: int, duration: float = 0.0):
        """
        Move mouse to absolute position.
        
        Args:
            x: X coordinate
            y: Y coordinate
            duration: Time to move in seconds (0 for instant)
        """
        pyautogui.moveTo(x, y, duration=duration)
    
    def move_mouse_relative(self, dx: int, dy: int, duration: float = 0.0):
        """
        Move mouse relative to current position.
        
        Args:
            dx: Change in X
            dy: Change in Y
            duration: Time to move in seconds (0 for instant)
        """
        pyautogui.moveRel(dx, dy, duration=duration)
    
    def click(self, button: MouseButton = MouseButton.LEFT, clicks: int = 1):
        """
        Perform mouse click.
        
        Args:
            button: Which mouse button to click
            clicks: Number of clicks
        """
        pyautogui.click(button=button.value, clicks=clicks)
    
    def mouse_down(self, button: MouseButton = MouseButton.LEFT):
        """
        Press and hold mouse button.
        
        Args:
            button: Which mouse button to hold
        """
        pyautogui.mouseDown(button=button.value)
    
    def mouse_up(self, button: MouseButton = MouseButton.LEFT):
        """
        Release mouse button.
        
        Args:
            button: Which mouse button to release
        """
        pyautogui.mouseUp(button=button.value)
    
    def press_key(self, key: str):
        """
        Press and release a key.
        
        Args:
            key: Key to press (e.g., 'w', 'space', 'shift')
        """
        pyautogui.press(key)
    
    def key_down(self, key: str):
        """
        Press and hold a key.
        
        Args:
            key: Key to hold down
        """
        pyautogui.keyDown(key)
    
    def key_up(self, key: str):
        """
        Release a key.
        
        Args:
            key: Key to release
        """
        pyautogui.keyUp(key)
    
    def type_text(self, text: str, interval: float = 0.0):
        """
        Type text.
        
        Args:
            text: Text to type
            interval: Interval between keystrokes
        """
        pyautogui.write(text, interval=interval)
    
    def hotkey(self, *keys: str):
        """
        Press a combination of keys.
        
        Args:
            *keys: Keys to press together (e.g., 'ctrl', 'c')
        """
        pyautogui.hotkey(*keys)
    
    def get_mouse_position(self) -> Tuple[int, int]:
        """
        Get current mouse position.
        
        Returns:
            Tuple of (x, y) coordinates
        """
        return pyautogui.position()
    
    def get_screen_size(self) -> Tuple[int, int]:
        """
        Get screen size.
        
        Returns:
            Tuple of (width, height)
        """
        return pyautogui.size()
