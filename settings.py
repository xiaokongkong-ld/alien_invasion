class Settings:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)


        self.ships_limit = 3


        self.bullet_width = 3
        self.bullet_height = 55
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10

        self.speedup_scale = 1.5

        self.initialize_dynamix_settings()

    def initialize_dynamix_settings(self):

        self.ship_speed = 10.5
        self.bullet_speed = 10.0
        self.alien_speed = 2.0
        self.fleet_drop_speed = 20

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points *= self.speedup_scale

