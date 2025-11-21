"""Main game AI controller that coordinates vision, AI, and input."""
import time
import logging
from typing import Optional, Tuple, Dict, Any
import base64
from screen_capture import ScreenCapture
from input_controller import InputController, MouseButton
from gemini_ai import GeminiGameAI


class GameAI:
    """Main controller for the FPS game-playing AI."""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        screen_region: Optional[Tuple[int, int, int, int]] = None,
        update_interval: float = 0.5,
        screenshot_quality: int = 85
    ):
        """
        Initialize the game AI.
        
        Args:
            api_key: Gemini API key
            screen_region: Screen region to capture (x, y, width, height)
            update_interval: Seconds between AI updates
            screenshot_quality: JPEG quality for screenshots (1-100)
        """
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Initialize components
        self.screen_capture = ScreenCapture(region=screen_region)
        self.input_controller = InputController()
        self.ai = GeminiGameAI(api_key=api_key)
        
        # Settings
        self.update_interval = update_interval
        self.screenshot_quality = screenshot_quality
        self.running = False
        
        # Statistics
        self.frames_processed = 0
        self.actions_taken = 0
        self.start_time = None
        
    def execute_action(self, action_data: Dict[str, Any]):
        """
        Execute an action based on AI decision.
        
        Args:
            action_data: Dictionary containing action and parameters
        """
        action = action_data.get("action", "no_action")
        params = action_data.get("parameters", {})
        reasoning = action_data.get("reasoning", "")
        
        self.logger.info(f"Action: {action} | Reasoning: {reasoning}")
        
        try:
            if action == "no_action":
                return
            
            # Mouse movement for aiming
            if action in ["aim_adjust", "turn_left", "turn_right"]:
                dx = params.get("mouse_dx", 0)
                dy = params.get("mouse_dy", 0)
                if dx != 0 or dy != 0:
                    self.input_controller.move_mouse_relative(dx, dy)
            
            # Movement actions
            if action == "move_forward":
                self.input_controller.key_down("w")
                time.sleep(params.get("duration", 0.1))
                self.input_controller.key_up("w")
            elif action == "move_backward":
                self.input_controller.key_down("s")
                time.sleep(params.get("duration", 0.1))
                self.input_controller.key_up("s")
            elif action == "strafe_left":
                self.input_controller.key_down("a")
                time.sleep(params.get("duration", 0.1))
                self.input_controller.key_up("a")
            elif action == "strafe_right":
                self.input_controller.key_down("d")
                time.sleep(params.get("duration", 0.1))
                self.input_controller.key_up("d")
            
            # Shooting and combat
            elif action == "shoot":
                duration = params.get("duration", 0.1)
                self.input_controller.mouse_down(MouseButton.LEFT)
                time.sleep(duration)
                self.input_controller.mouse_up(MouseButton.LEFT)
            elif action == "reload":
                self.input_controller.press_key("r")
            elif action == "switch_weapon":
                weapon_key = params.get("weapon_key", "1")
                self.input_controller.press_key(weapon_key)
            
            # Other actions
            elif action == "jump":
                self.input_controller.press_key("space")
            elif action == "crouch":
                self.input_controller.press_key("ctrl")
            
            # Handle multiple keys if specified
            keys = params.get("keys", [])
            if keys:
                for key in keys:
                    self.input_controller.key_down(key)
                time.sleep(params.get("duration", 0.1))
                for key in keys:
                    self.input_controller.key_up(key)
            
            self.actions_taken += 1
            
        except Exception as e:
            self.logger.error(f"Error executing action: {e}")
    
    def run(self, duration: Optional[float] = None, max_iterations: Optional[int] = None):
        """
        Run the AI game loop.
        
        Args:
            duration: Optional max duration in seconds
            max_iterations: Optional max number of iterations
        """
        self.logger.info("Starting game AI...")
        self.logger.info(f"Update interval: {self.update_interval}s")
        self.logger.info("Move mouse to any corner of the screen to stop (failsafe)")
        
        self.running = True
        self.start_time = time.time()
        iteration = 0
        
        try:
            while self.running:
                iteration += 1
                
                # Check stop conditions
                if max_iterations and iteration > max_iterations:
                    self.logger.info(f"Reached max iterations: {max_iterations}")
                    break
                
                if duration and (time.time() - self.start_time) > duration:
                    self.logger.info(f"Reached max duration: {duration}s")
                    break
                
                # Capture screen
                frame_start = time.time()
                try:
                    image_base64 = self.screen_capture.capture_as_base64(
                        quality=self.screenshot_quality
                    )
                    image_bytes = base64.b64decode(image_base64)
                    
                    self.frames_processed += 1
                    
                    # Get AI decision
                    action_data = self.ai.analyze_frame(image_bytes)
                    
                    # Execute action
                    self.execute_action(action_data)
                    
                except Exception as e:
                    self.logger.error(f"Error in main loop: {e}")
                
                # Maintain update interval
                elapsed = time.time() - frame_start
                if elapsed < self.update_interval:
                    time.sleep(self.update_interval - elapsed)
                
                # Log statistics periodically
                if iteration % 10 == 0:
                    runtime = time.time() - self.start_time
                    fps = self.frames_processed / runtime if runtime > 0 else 0
                    self.logger.info(
                        f"Stats | Iterations: {iteration} | "
                        f"Frames: {self.frames_processed} | "
                        f"Actions: {self.actions_taken} | "
                        f"FPS: {fps:.2f}"
                    )
        
        except KeyboardInterrupt:
            self.logger.info("Interrupted by user")
        except Exception as e:
            self.logger.error(f"Fatal error: {e}")
        finally:
            self.stop()
    
    def stop(self):
        """Stop the AI and cleanup."""
        self.running = False
        if self.start_time:
            runtime = time.time() - self.start_time
            self.logger.info(f"Session ended. Runtime: {runtime:.2f}s")
            self.logger.info(f"Total frames processed: {self.frames_processed}")
            self.logger.info(f"Total actions taken: {self.actions_taken}")
