#!/usr/bin/env python3
"""Main entry point for the FPS game AI."""
import argparse
import sys
from config import Config
from game_ai import GameAI


def main():
    """Main function to run the game AI."""
    parser = argparse.ArgumentParser(
        description="AI for playing FPS games using Google Gemini Live API"
    )
    parser.add_argument(
        "--duration",
        type=float,
        help="Maximum duration to run in seconds (default: unlimited)",
        default=None
    )
    parser.add_argument(
        "--iterations",
        type=int,
        help="Maximum number of iterations (default: unlimited)",
        default=None
    )
    parser.add_argument(
        "--interval",
        type=float,
        help="Update interval in seconds (default: from config or 0.5)",
        default=None
    )
    parser.add_argument(
        "--quality",
        type=int,
        help="Screenshot JPEG quality 1-100 (default: from config or 85)",
        default=None
    )
    parser.add_argument(
        "--api-key",
        type=str,
        help="Gemini API key (default: from .env file)",
        default=None
    )
    
    args = parser.parse_args()
    
    try:
        # Load configuration
        config = Config()
        
        # Override with command line arguments if provided
        api_key = args.api_key or config.api_key
        update_interval = args.interval or config.update_interval
        screenshot_quality = args.quality or config.screenshot_quality
        screen_region = config.screen_region
        
        print("=" * 60)
        print("FPS Game AI - Powered by Google Gemini Live API")
        print("=" * 60)
        print(f"Update interval: {update_interval}s")
        print(f"Screenshot quality: {screenshot_quality}")
        print(f"Screen region: {screen_region or 'Full primary monitor'}")
        print()
        print("SAFETY: Move mouse to any corner to trigger failsafe stop!")
        print()
        print("Starting in 3 seconds...")
        print("Make sure your game window is visible and focused...")
        print()
        
        import time
        for i in range(3, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        
        print("GO!\n")
        
        # Initialize and run the game AI
        game_ai = GameAI(
            api_key=api_key,
            screen_region=screen_region,
            update_interval=update_interval,
            screenshot_quality=screenshot_quality
        )
        
        game_ai.run(
            duration=args.duration,
            max_iterations=args.iterations
        )
        
    except KeyboardInterrupt:
        print("\n\nStopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
