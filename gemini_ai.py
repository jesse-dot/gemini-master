"""Google Gemini AI integration for game playing."""
import os
from typing import Optional, Dict, Any
from google import genai
from google.genai import types


class GeminiGameAI:
    """AI controller using Google Gemini Live API for FPS game playing."""
    
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-2.0-flash-exp"):
        """
        Initialize the Gemini AI.
        
        Args:
            api_key: Google Gemini API key. If None, reads from GEMINI_API_KEY env var.
            model_name: Name of the Gemini model to use
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not provided and not found in environment")
        
        self.client = genai.Client(api_key=self.api_key)
        self.model_name = model_name
        self.system_instruction = self._create_system_instruction()
        
    def _create_system_instruction(self) -> str:
        """Create the system instruction for FPS game playing."""
        return """You are an AI agent designed to play first-person shooter (FPS) games.

Your role:
- Analyze screenshots from the game in real-time
- Make strategic decisions about movement, aiming, and shooting
- Identify enemies, objectives, and important game elements
- Provide clear, actionable commands to control the player character

When analyzing a game screenshot, you should:
1. Identify enemy positions and threat levels
2. Assess the current situation (health, ammo, position)
3. Determine the best tactical action
4. Provide specific commands in JSON format

Command format (respond ONLY with valid JSON):
{
  "action": "move_forward" | "move_backward" | "strafe_left" | "strafe_right" | "turn_left" | "turn_right" | "aim_adjust" | "shoot" | "reload" | "switch_weapon" | "crouch" | "jump" | "no_action",
  "parameters": {
    "mouse_dx": <integer for horizontal mouse movement, -1000 to 1000>,
    "mouse_dy": <integer for vertical mouse movement, -1000 to 1000>,
    "duration": <float for how long to perform action in seconds>,
    "keys": [<list of keys to press like "w", "a", "s", "d", "space", "ctrl", "r">]
  },
  "reasoning": "<brief explanation of your decision>"
}

Remember:
- Be aggressive but tactical
- Prioritize survival and objective completion
- React quickly to threats
- Use cover when available
- Manage resources (health, ammo)
- Always respond with valid JSON only
"""
    
    def analyze_frame(self, image_data: str, context: Optional[str] = None) -> Dict[str, Any]:
        """
        Analyze a game frame and return action decision.
        
        Args:
            image_data: Base64 encoded image data
            context: Optional additional context about the game state
            
        Returns:
            Dictionary containing action decision and reasoning
        """
        try:
            # Prepare the prompt
            prompt = "Analyze this FPS game screenshot and provide your next action command."
            if context:
                prompt += f"\n\nAdditional context: {context}"
            
            # Create image part
            image_part = types.Part.from_bytes(
                data=image_data,
                mime_type="image/jpeg"
            )
            
            # Generate response
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=[image_part, prompt],
                config=types.GenerateContentConfig(
                    system_instruction=self.system_instruction,
                    temperature=0.4,  # Lower temperature for more consistent gameplay
                    max_output_tokens=500,
                )
            )
            
            # Parse response
            response_text = response.text.strip()
            
            # Try to extract JSON from response
            import json
            
            # Remove markdown code blocks if present
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
            
            try:
                action = json.loads(response_text)
                return action
            except json.JSONDecodeError:
                # If JSON parsing fails, return a safe no-action response
                return {
                    "action": "no_action",
                    "parameters": {},
                    "reasoning": f"Failed to parse AI response: {response_text[:100]}"
                }
                
        except Exception as e:
            return {
                "action": "no_action",
                "parameters": {},
                "reasoning": f"Error in AI analysis: {str(e)}"
            }
    
    def analyze_frame_with_text(self, image_data: str, text: str) -> str:
        """
        Analyze a frame with custom text prompt.
        
        Args:
            image_data: Base64 encoded image data
            text: Custom text prompt
            
        Returns:
            AI response as string
        """
        try:
            image_part = types.Part.from_bytes(
                data=image_data,
                mime_type="image/jpeg"
            )
            
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=[image_part, text],
                config=types.GenerateContentConfig(
                    system_instruction=self.system_instruction,
                    temperature=0.4,
                )
            )
            
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
