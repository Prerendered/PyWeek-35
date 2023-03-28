import arcade

from src.classes.managers.game_manager import GameManager
from src.constants import CONSTANTS as C


class ScoreView(arcade.View):
    def __init__(self, game_view):
        """Base class for the 'score' view."""
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        arcade.set_background_color(C.BACKGROUND_COLOR)

    # TODO: add a rating and a completion time
    # TODO: add sprites for the rating
    def on_draw(self):
        """Draw the game over screen"""
        self.clear()
        self._draw_centered_text("Game Over", 54, 200)
        self._draw_centered_text(f"Rating", 38, 100)
        self._draw_centered_text(f"Score:", 22, -40, "right")
        self._draw_centered_text(f"Time:", 22, -100, "right")
        
        # Whitespace in front of first character required to center text properly 
        # and avoid weird spacing
        self._draw_centered_text(f" {GameManager.instance.score}", 22, -40, "left")
        self._draw_centered_text(f" 10s", 22, -100, "left") # Placeholder for Time

        self._draw_centered_text("Press any key to restart", 12, -250)
        self._draw_centered_text("Press ESC to exit", 12, -300)

    def _draw_centered_text(
        self, text: str, font_size: int, y_offset: int, anchor: str = "center"
    ):
        """Helper function to draw text centered on the screen"""
        x = C.SCREEN_WIDTH / 2
        y = C.SCREEN_HEIGHT / 2 + y_offset
        arcade.draw_text(text, x, y, arcade.color.WHITE, font_size, anchor_x=anchor)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            arcade.exit()
        else:
            self.game_view.setup()
            self.window.show_view(self.game_view)
