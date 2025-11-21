"""Screen capture module for capturing game frames."""
import mss
import numpy as np
from PIL import Image
import io
import base64
from typing import Tuple, Optional


class ScreenCapture:
    """Handles screen capture for the AI to see the game."""
    
    def __init__(self, region: Optional[Tuple[int, int, int, int]] = None):
        """
        Initialize screen capture.
        
        Args:
            region: Optional tuple of (x, y, width, height) for capture region.
                   If None, captures entire primary monitor.
        """
        self.sct = mss.mss()
        self.region = region
        
    def capture(self) -> Image.Image:
        """
        Capture the screen or specified region.
        
        Returns:
            PIL Image of the captured screen.
        """
        if self.region:
            x, y, width, height = self.region
            monitor = {
                "top": y,
                "left": x,
                "width": width,
                "height": height
            }
        else:
            monitor = self.sct.monitors[1]  # Primary monitor
        
        screenshot = self.sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        return img
    
    def capture_as_base64(self, quality: int = 85) -> str:
        """
        Capture screen and return as base64 encoded JPEG.
        
        Args:
            quality: JPEG quality (1-100)
            
        Returns:
            Base64 encoded string of the image
        """
        img = self.capture()
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=quality)
        img_bytes = buffer.getvalue()
        return base64.b64encode(img_bytes).decode('utf-8')
    
    def capture_as_numpy(self) -> np.ndarray:
        """
        Capture screen and return as numpy array.
        
        Returns:
            Numpy array of the image (RGB)
        """
        img = self.capture()
        return np.array(img)
    
    def get_monitor_info(self) -> dict:
        """
        Get information about available monitors.
        
        Returns:
            Dictionary with monitor information
        """
        return {
            "monitors": self.sct.monitors,
            "primary": self.sct.monitors[1]
        }
