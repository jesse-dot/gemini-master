"""Configuration management for the FPS game AI."""
import os
from typing import Optional, Tuple
from dotenv import load_dotenv


class Config:
    """Configuration manager for the game AI."""
    
    def __init__(self, env_file: str = ".env"):
        """
        Initialize configuration.
        
        Args:
            env_file: Path to .env file
        """
        load_dotenv(env_file)
        
    @property
    def api_key(self) -> str:
        """Get Gemini API key."""
        key = os.getenv("GEMINI_API_KEY", "")
        if not key:
            raise ValueError(
                "GEMINI_API_KEY not found. Please set it in .env file or environment."
            )
        return key
    
    @property
    def screen_region(self) -> Optional[Tuple[int, int, int, int]]:
        """Get screen capture region."""
        x = os.getenv("SCREEN_REGION_X")
        y = os.getenv("SCREEN_REGION_Y")
        width = os.getenv("SCREEN_REGION_WIDTH")
        height = os.getenv("SCREEN_REGION_HEIGHT")
        
        if all([x, y, width, height]):
            return (int(x), int(y), int(width), int(height))
        return None
    
    @property
    def update_interval(self) -> float:
        """Get AI update interval in seconds."""
        return float(os.getenv("AI_UPDATE_INTERVAL", "0.5"))
    
    @property
    def screenshot_quality(self) -> int:
        """Get screenshot JPEG quality."""
        return int(os.getenv("SCREENSHOT_QUALITY", "85"))
