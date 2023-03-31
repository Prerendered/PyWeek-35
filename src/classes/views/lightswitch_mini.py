import arcade

from constants import CONSTANTS as C
from classes.managers.game_manager import GameManager


class LightSwitchMini(arcade.View):
    """Light Switch Mini Game"""

    SWITCH_SIZE = 0.5

    def __init__(self):
        super().__init__()

        self.switch_on = arcade.Sprite(
            "./src/assets/art/light_switch/light_switch_on.png",
            LightSwitchMini.SWITCH_SIZE,
        )
        self.switch_off = arcade.Sprite(
            "./src/assets/art/light_switch/light_switch_off.png",
            LightSwitchMini.SWITCH_SIZE,
        )

        for sprite in [self.switch_on, self.switch_off]:
            sprite.center_x = C.SCREEN_WIDTH / 2
            sprite.center_y = C.SCREEN_HEIGHT / 2
            
        self.clear()
        self.switch_off.draw()

    def on_show_view(self):
        """Called when switching to this view"""
        arcade.set_background_color(C.BACKGROUND_COLOR)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Handle mouse press events."""
        pass

    def on_key_press(self, key, modifiers):
        """Handle key release events."""

        if key == arcade.key.SPACE:
            self.clear()
            self.switch_on.draw()
            arcade.draw_text(
                "Press q to exit",
                C.SCREEN_WIDTH / 2,
                C.SCREEN_HEIGHT / 2 - 250,
                arcade.color.WHITE,
                30,
                anchor_x="center",
            )
        
        # TODO: Go back to previous view instead of closing the window 
        if key == arcade.key.Q:
            resume_game = GameManager.instance.get_game_view()
            self.window.show_view(resume_game)