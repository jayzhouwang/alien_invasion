class Settings:
    """A class to store all settings for Alien Ivasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleer_direction of 1 represent right; -1 represent left.
        self.fleet_direction = 1
