"""
Lab 12 - Final Project
Audio from http://opengameart.org
"""
import arcade
import random

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 8
BALL_SPEED = 4

INSTRUCTION_PAGE = 0
GAME_RUNNING = 1
LEVEL_COMPLETE_PAGE = 2
GAME_OVER = 3
GAME_END = 4


def create_power_up(x, y, power_up_list, all_sprites_list):
    power_up = None
    power_up_type = random.randrange(3)
    if power_up_type == 0:
        # Image from Game Freezer: http://www.gamesfreezer.eu/2015_06_01_archive.html
        power_up = arcade.Sprite("images/extra_life.png", 0.4 * SPRITE_SCALING)
    if power_up_type == 1:
        # Image from Prek-8.com:
        power_up = arcade.Sprite("images/add_balls.png", 0.4 * SPRITE_SCALING)
    if power_up_type == 2:
        # image from ClipartFest: https://clipartfest.com/categories/view/
        power_up = arcade.Sprite("images/speed_up.png", 0.4 * SPRITE_SCALING)
    power_up.power_up_value = power_up_type
    power_up.change_y = -2
    power_up.center_x = x
    power_up.center_y = y
    power_up_list.append(power_up)
    all_sprites_list.append(power_up)
    

class Ball(arcade.Sprite):

    def __init__(self, all_sprites_list, power_up_list, wall_list,
                 brick_list, blue_brick_list, orange_brick_list, wall_brick_list,
                 player_sprite, application):
        # Image from Kenney.nl
        super().__init__("images/ball.png", 2 * SPRITE_SCALING)
        self.all_sprites_list = all_sprites_list
        self.wall_list = wall_list
        self.brick_list = brick_list
        self.blue_brick_list = blue_brick_list
        self.orange_brick_list = orange_brick_list
        self.wall_brick_list = wall_brick_list
        self.power_up_list = power_up_list
        self.player_sprite = player_sprite
        self.brick_sound = arcade.load_sound("sounds/brick_hit.wav")
        self.center_x = self.player_sprite.center_x
        self.center_y = 0.05 * SCREEN_HEIGHT + SCREEN_HEIGHT/15
        self.change_x = random.randrange(-3, 4)
        self.change_y = BALL_SPEED
        self.application = application

    def update(self):

        self.center_x += self.change_x

        orange_brick_hit_list = arcade.check_for_collision_with_list(self, self.orange_brick_list)
        for brick in orange_brick_hit_list:
            # Image from Kenney.nl
            blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
            blue_brick.center_x = brick.center_x
            blue_brick.center_y = brick.center_y
            self.all_sprites_list.append(blue_brick)
            self.brick_list.append(blue_brick)
            self.blue_brick_list.append(blue_brick)
            brick.kill()
            arcade.play_sound(self.brick_sound)
            self.application.score += 1
            if self.change_x > 0:
                self.right = brick.left
            else:
                self.left = brick.right
        if len(orange_brick_hit_list) > 0:
            self.change_x *= -1

        blue_brick_hit_list = arcade.check_for_collision_with_list(self, self.blue_brick_list)
        for brick in blue_brick_hit_list:
            brick.kill()
            arcade.play_sound(self.brick_sound)
            self.application.score += 1
            if random.randrange(10) == 0:
                create_power_up(self.center_x, self.center_y, self.power_up_list, self.all_sprites_list)
            if self.change_x > 0:
                self.right = brick.left
            else:
                self.left = brick.right

        if len(blue_brick_hit_list) > 0:
            self.change_x *= -1

        wall_hit_list = arcade.check_for_collision_with_list(self, self.wall_list)
        for wall in wall_hit_list:
            if self.change_x > 0:
                self.right = wall.left
            else:
                self.left = wall.right
        if len(wall_hit_list) > 0:
            self.change_x *= -1

        wall_brick_hit_list = arcade.check_for_collision_with_list(self, self.wall_brick_list)
        for wall_brick in wall_brick_hit_list:
            if self.change_x > 0:
                self.right = wall_brick.left
            else:
                self.left = wall_brick.right
        if len(wall_brick_hit_list) > 0:
            self.change_x *= -1

        self.center_y += self.change_y

        orange_brick_hit_list = arcade.check_for_collision_with_list(self, self.orange_brick_list)
        for brick in orange_brick_hit_list:
            # Image from Kenney.nl
            blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
            blue_brick.center_x = brick.center_x
            blue_brick.center_y = brick.center_y
            self.all_sprites_list.append(blue_brick)
            self.brick_list.append(blue_brick)
            self.blue_brick_list.append(blue_brick)
            brick.kill()
            arcade.play_sound(self.brick_sound)
            if self.change_y > 0:
                self.top = brick.bottom
            else:
                self.bottom = brick.top
            self.application.score += 1
        if len(orange_brick_hit_list) > 0:
            self.change_y *= -1

        blue_brick_hit_list = arcade.check_for_collision_with_list(self, self.blue_brick_list)
        for brick in blue_brick_hit_list:
            brick.kill()
            arcade.play_sound(self.brick_sound)
            if random.randrange(10) == 0:
                create_power_up(self.center_x, self.center_y, self.power_up_list, self.all_sprites_list)
            if self.change_y > 0:
                self.top = brick.bottom
            else:
                self.bottom = brick.top
            self.application.score += 1
        if len(blue_brick_hit_list) > 0:
            self.change_y *= -1

        wall_hit_list = arcade.check_for_collision_with_list(self, self.wall_list)
        for wall in wall_hit_list:
            if self.change_y > 0:
                self.top = wall.bottom
            else:
                self.bottom = wall.top
        if len(wall_hit_list) > 0:
            self.change_y *= -1

        wall_brick_hit_list = arcade.check_for_collision_with_list(self, self.wall_brick_list)
        for wall_brick in wall_brick_hit_list:
            if self.change_y > 0:
                self.top = wall_brick.bottom
            else:
                self.bottom = wall_brick.top
        if len(wall_brick_hit_list) > 0:
            self.change_y *= -1

    def get_score(self):
        arcade.draw_text("Score: " + str(self.score), 40, 10, arcade.color.WHITE, 24)


class MyApplication(arcade.Window):
    """ Main application class. """
    def __init__(self, width, height):

        super().__init__(width, height)
        # Sprite lists
        self.all_sprites_list = None

        # Set up the player.

        self.score = 0
        self.player_sprite = None
        self.player_sound = arcade.load_sound("sounds/player_hit.wav")
        self.wall_list = None
        self.brick_list = None
        self.wall_brick_list = None
        self.blue_brick_list = None
        self.orange_brick_list = None
        self.power_up_value = None
        self.power_up_list = None
        self.ball = None
        self.ball_list = None
        self.lives = 3
        self.next_level = False
        self.level = None
        self.current_state = INSTRUCTION_PAGE

    def setup(self):

        # Sprite lists
        self.score = 0
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.brick_list = arcade.SpriteList()
        self.blue_brick_list = arcade.SpriteList()
        self.orange_brick_list = arcade.SpriteList()
        self.wall_brick_list = arcade.SpriteList()
        self.power_up_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.level = 0
        self.next_level = False
        # Image from Kenney.nl
        self.player_sprite = arcade.Sprite("images/player.png",
                                           0.25 * SPRITE_SCALING)
        self.player_sprite.center_x = 0.5 * SCREEN_WIDTH
        self.player_sprite.center_y = 0.075 * SCREEN_HEIGHT
        self.all_sprites_list.append(self.player_sprite)

        arcade.set_background_color(arcade.color.AMAZON)

        # -- Set up the boundary walls.
        for y in range(18, 600, 32):
            # Image from Kenney.nl
            wall = arcade.Sprite("images/wall.png", 0.5 * SPRITE_SCALING)
            wall.center_x = 18
            wall.center_y = y
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        for y in range(18, 600, 32):
            # Image from Kenney.nl
            wall = arcade.Sprite("images/wall.png", 0.5 * SPRITE_SCALING)
            wall.center_x = 582
            wall.center_y = y
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        for x in range(12, 600, 32):
            # Image from Kenney.nl
            wall = arcade.Sprite("images/wall.png", 0.5 * SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 596
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

    def level_1(self):
        self.next_level = False
        ball = Ball(self.all_sprites_list, self.power_up_list,
                    self.wall_list, self.brick_list, self.blue_brick_list,
                    self.orange_brick_list, self.wall_brick_list, self.player_sprite, self)
        self.ball_list.append(ball)
        self.all_sprites_list.append(ball)

        for row in range(4):
            for column in range(-(8 - 2 * row), 0):
                # Image from Kenney.nl
                blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
                blue_brick.center_x = SCREEN_WIDTH / 10 * row + SCREEN_WIDTH / 2
                blue_brick.center_y = 30 * column + 590
                self.all_sprites_list.append(blue_brick)
                self.brick_list.append(blue_brick)
                self.blue_brick_list.append(blue_brick)

        for column in range(4):
            for row in range(-2 * column, 0):
                # Image from Kenney.nl
                blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
                blue_brick.center_x = 60 * column + 60
                blue_brick.center_y = 30 * row + 590
                self.all_sprites_list.append(blue_brick)
                self.brick_list.append(blue_brick)
                self.blue_brick_list.append(blue_brick)

    def level_2(self):
        self.next_level = False
        ball = Ball(self.all_sprites_list, self.power_up_list,
                    self.wall_list, self.brick_list, self.blue_brick_list,
                    self.orange_brick_list, self.wall_brick_list, self.player_sprite, self)
        self.ball_list.append(ball)
        self.all_sprites_list.append(ball)

        for row in range(4):
            for column in range(0, (4 - row)):
                # Image from Kenney.nl
                blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
                blue_brick.center_x = SCREEN_WIDTH / 10 * row + 70
                blue_brick.center_y = 30 * column + 300
                self.all_sprites_list.append(blue_brick)
                self.brick_list.append(blue_brick)
                self.blue_brick_list.append(blue_brick)

        for row in range(4):
            for column in range(-(4 - row), 0):
                # Image from Kenney.nl
                blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
                blue_brick.center_x = SCREEN_WIDTH / 10 * row + 70
                blue_brick.center_y = 30 * column + 590
                self.all_sprites_list.append(blue_brick)
                self.brick_list.append(blue_brick)
                self.blue_brick_list.append(blue_brick)

        for column in range(5):
            for row in range(0, column):
                # Image from Kenney.nl
                blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
                blue_brick.center_x = 60 * column + 290
                blue_brick.center_y = 30 * row + 300
                self.all_sprites_list.append(blue_brick)
                self.brick_list.append(blue_brick)
                self.blue_brick_list.append(blue_brick)

        for column in range(5):
            for row in range(-column, 0):
                # Image from Kenney.nl
                blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
                blue_brick.center_x = 60 * column + 290
                blue_brick.center_y = 30 * row + 590
                self.all_sprites_list.append(blue_brick)
                self.brick_list.append(blue_brick)
                self.blue_brick_list.append(blue_brick)

        for column in range(5):
            # Image from Kenney.nl
            wall_brick = arcade.Sprite("images/black_brick.png", 0.6 * SPRITE_SCALING)
            wall_brick.center_x = 60 * column + 180
            wall_brick.center_y = 430
            self.all_sprites_list.append(wall_brick)
            self.wall_brick_list.append(wall_brick)

    def level_3(self):
        self.next_level = False
        ball = Ball(self.all_sprites_list, self.power_up_list,
                    self.wall_list, self.brick_list, self.blue_brick_list,
                    self.orange_brick_list, self.wall_brick_list, self.player_sprite, self)
        self.ball_list.append(ball)
        self.all_sprites_list.append(ball)
        # Image from Kenney.nl
        orange_brick = arcade.Sprite("images/orange_brick.png", 0.6 * SPRITE_SCALING)
        orange_brick.center_x = SCREEN_WIDTH / 2
        orange_brick.center_y = 3 * SCREEN_HEIGHT / 4
        self.all_sprites_list.append(orange_brick)
        self.brick_list.append(orange_brick)
        self.orange_brick_list.append(orange_brick)

        for row in range(3):
            # Image from Kenney.nl
            blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
            blue_brick.center_x = 240
            blue_brick.center_y = 30 * row + 420
            self.all_sprites_list.append(blue_brick)
            self.brick_list.append(blue_brick)
            self.blue_brick_list.append(blue_brick)

        for row in range(3):
            # Image from Kenney.nl
            blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
            blue_brick.center_x = 360
            blue_brick.center_y = 30 * row + 420
            self.all_sprites_list.append(blue_brick)
            self.brick_list.append(blue_brick)
            self.blue_brick_list.append(blue_brick)
        # Image from Kenney.nl
        blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
        blue_brick.center_x = 300
        blue_brick.center_y = 420
        self.all_sprites_list.append(blue_brick)
        self.brick_list.append(blue_brick)
        self.blue_brick_list.append(blue_brick)
        # Image from Kenney.nl
        blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
        blue_brick.center_x = 300
        blue_brick.center_y = 480
        self.all_sprites_list.append(blue_brick)
        self.brick_list.append(blue_brick)
        self.blue_brick_list.append(blue_brick)

        for row in range(5):
            # Image from Kenney.nl
            orange_brick = arcade.Sprite("images/orange_brick.png", 0.6 * SPRITE_SCALING)
            orange_brick.center_x = 180
            orange_brick.center_y = 30 * row + 390
            self.all_sprites_list.append(orange_brick)
            self.brick_list.append(orange_brick)
            self.orange_brick_list.append(orange_brick)

        for row in range(5):
            # Image from Kenney.nl
            orange_brick = arcade.Sprite("images/orange_brick.png", 0.6 * SPRITE_SCALING)
            orange_brick.center_x = 420
            orange_brick.center_y = 30 * row + 390
            self.all_sprites_list.append(orange_brick)
            self.brick_list.append(orange_brick)
            self.orange_brick_list.append(orange_brick)

        for column in range(3):
            # Image from Kenney.nl
            orange_brick = arcade.Sprite("images/orange_brick.png", 0.6 * SPRITE_SCALING)
            orange_brick.center_x = 60 * column + 240
            orange_brick.center_y = 390
            self.all_sprites_list.append(orange_brick)
            self.brick_list.append(orange_brick)
            self.orange_brick_list.append(orange_brick)

        for column in range(3):
            # Image from Kenney.nl
            orange_brick = arcade.Sprite("images/orange_brick.png", 0.6 * SPRITE_SCALING)
            orange_brick.center_x = 60 * column + 240
            orange_brick.center_y = 510
            self.all_sprites_list.append(orange_brick)
            self.brick_list.append(orange_brick)
            self.orange_brick_list.append(orange_brick)

        for row in range(7):
            # Image from Kenney.nl
            blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
            blue_brick.center_x = 120
            blue_brick.center_y = 30 * row + 360
            self.all_sprites_list.append(blue_brick)
            self.brick_list.append(blue_brick)
            self.blue_brick_list.append(blue_brick)

        for row in range(7):
            # Image from Kenney.nl
            blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
            blue_brick.center_x = 480
            blue_brick.center_y = 30 * row + 360
            self.all_sprites_list.append(blue_brick)
            self.brick_list.append(blue_brick)
            self.blue_brick_list.append(blue_brick)

        for column in range(5):
            # Image from Kenney.nl
            blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
            blue_brick.center_x = 60 * column + 180
            blue_brick.center_y = 360
            self.all_sprites_list.append(blue_brick)
            self.brick_list.append(blue_brick)
            self.blue_brick_list.append(blue_brick)

        for column in range(5):
            # Image from Kenney.nl
            blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
            blue_brick.center_x = 60 * column + 180
            blue_brick.center_y = 540
            self.all_sprites_list.append(blue_brick)
            self.brick_list.append(blue_brick)
            self.blue_brick_list.append(blue_brick)

    def level_4(self):
        self.next_level = False
        ball = Ball(self.all_sprites_list, self.power_up_list,
                    self.wall_list, self.brick_list, self.blue_brick_list,
                    self.orange_brick_list, self.wall_brick_list, self.player_sprite, self)
        self.ball_list.append(ball)
        self.all_sprites_list.append(ball)

        for row in range(5):
            for column in range(8):
                # Image from Kenney.nl
                blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
                blue_brick.center_x = SCREEN_WIDTH / 10 * column + 90
                blue_brick.center_y = 30 * row + 430
                self.all_sprites_list.append(blue_brick)
                self.brick_list.append(blue_brick)
                self.blue_brick_list.append(blue_brick)

        for column in range(4):
            # Image from Kenney.nl
            wall_brick = arcade.Sprite("images/black_brick.png", 0.6 * SPRITE_SCALING)
            wall_brick.center_x = 120 * column + 110
            wall_brick.center_y = 220
            wall_brick.change_x = -2
            self.all_sprites_list.append(wall_brick)
            self.wall_brick_list.append(wall_brick)

        for column in range(4):
            # Image from Kenney.nl
            wall_brick = arcade.Sprite("images/black_brick.png", 0.6 * SPRITE_SCALING)
            wall_brick.center_x = 120 * column + 130
            wall_brick.center_y = 280
            wall_brick.change_x = 2
            self.all_sprites_list.append(wall_brick)
            self.wall_brick_list.append(wall_brick)

    def level_5(self):
        self.next_level = False
        ball = Ball(self.all_sprites_list,  self.power_up_list,
                    self.wall_list, self.brick_list, self.blue_brick_list,
                    self.orange_brick_list, self.wall_brick_list, self.player_sprite, self)
        self.ball_list.append(ball)
        self.all_sprites_list.append(ball)
        # Image from Kenney.nl
        orange_brick = arcade.Sprite("images/orange_brick.png", 0.6 * SPRITE_SCALING)
        orange_brick.center_x = 300
        orange_brick.center_y = 350
        self.all_sprites_list.append(orange_brick)
        self.brick_list.append(orange_brick)
        self.orange_brick_list.append(orange_brick)

        for row in range(3):
            # Image from Kenney.nl
            blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
            blue_brick.center_x = 240
            blue_brick.center_y = 30 * row + 320
            self.all_sprites_list.append(blue_brick)
            self.brick_list.append(blue_brick)
            self.blue_brick_list.append(blue_brick)

        for row in range(3):
            # Image from Kenney.nl
            blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
            blue_brick.center_x = 360
            blue_brick.center_y = 30 * row + 320
            self.all_sprites_list.append(blue_brick)
            self.brick_list.append(blue_brick)
            self.blue_brick_list.append(blue_brick)
        # Image from Kenney.nl
        blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
        blue_brick.center_x = 300
        blue_brick.center_y = 320
        self.all_sprites_list.append(blue_brick)
        self.brick_list.append(blue_brick)
        self.blue_brick_list.append(blue_brick)
        # Image from Kenney.nl
        blue_brick = arcade.Sprite("images/blue_brick.png", 0.6 * SPRITE_SCALING)
        blue_brick.center_x = 300
        blue_brick.center_y = 380
        self.all_sprites_list.append(blue_brick)
        self.brick_list.append(blue_brick)
        self.blue_brick_list.append(blue_brick)

        for row in range(5):
            # Image from Kenney.nl
            orange_brick = arcade.Sprite("images/orange_brick.png", 0.6 * SPRITE_SCALING)
            orange_brick.center_x = 180
            orange_brick.center_y = 30 * row + 290
            self.all_sprites_list.append(orange_brick)
            self.brick_list.append(orange_brick)
            self.orange_brick_list.append(orange_brick)

        for row in range(5):
            # Image from Kenney.nl
            orange_brick = arcade.Sprite("images/orange_brick.png", 0.6 * SPRITE_SCALING)
            orange_brick.center_x = 420
            orange_brick.center_y = 30 * row + 290
            self.all_sprites_list.append(orange_brick)
            self.brick_list.append(orange_brick)
            self.orange_brick_list.append(orange_brick)

        for column in range(3):
            # Image from Kenney.nl
            orange_brick = arcade.Sprite("images/orange_brick.png", 0.6 * SPRITE_SCALING)
            orange_brick.center_x = 60 * column + 240
            orange_brick.center_y = 290
            self.all_sprites_list.append(orange_brick)
            self.brick_list.append(orange_brick)
            self.orange_brick_list.append(orange_brick)

        for column in range(3):
            # Image from Kenney.nl
            orange_brick = arcade.Sprite("images/orange_brick.png", 0.6 * SPRITE_SCALING)
            orange_brick.center_x = 60 * column + 240
            orange_brick.center_y = 410
            self.all_sprites_list.append(orange_brick)
            self.brick_list.append(orange_brick)
            self.orange_brick_list.append(orange_brick)

        for column in range(4):
            # Image from Kenney.nl
            wall_brick = arcade.Sprite("images/black_brick.png", 0.6 * SPRITE_SCALING)
            wall_brick.center_x = 140 * column + 90
            wall_brick.center_y = 220
            wall_brick.change_x = 2
            wall_brick.change_y = 0
            self.all_sprites_list.append(wall_brick)
            self.wall_brick_list.append(wall_brick)

        for column in range(4):
            # Image from Kenney.nl
            wall_brick = arcade.Sprite("images/black_brick.png", 0.6 * SPRITE_SCALING)
            wall_brick.center_x = 140 * column + 90
            wall_brick.center_y = 480
            wall_brick.change_x = -2
            wall_brick.change_y = 0
            self.all_sprites_list.append(wall_brick)
            self.wall_brick_list.append(wall_brick)
        # Image from Kenney.nl
        wall_brick = arcade.Sprite("images/black_brick.png", 0.6 * SPRITE_SCALING)
        wall_brick.center_x = 90
        wall_brick.center_y = 350
        wall_brick.change_x = 0
        wall_brick.change_y = -2
        self.all_sprites_list.append(wall_brick)
        self.wall_brick_list.append(wall_brick)
        # Image from Kenney.nl
        wall_brick = arcade.Sprite("images/black_brick.png", 0.6 * SPRITE_SCALING)
        wall_brick.center_x = 510
        wall_brick.center_y = 350
        wall_brick.change_x = 0
        wall_brick.change_y = 2
        self.all_sprites_list.append(wall_brick)
        self.wall_brick_list.append(wall_brick)

    def add_life(self):
        self.lives += 1

    def add_balls(self):
        for i in range(3):
            ball = Ball(self.all_sprites_list, self.power_up_list,
                        self.wall_list, self.brick_list, self.blue_brick_list,
                        self.orange_brick_list, self.wall_brick_list, self.player_sprite, self)
            self.ball_list.append(ball)
            self.all_sprites_list.append(ball)

    def speed_up(self):
        for ball in self.ball_list:
            ball.change_y += 1

    def draw_instructions_page(self):
        arcade.draw_text("Welcome to Brick Breaker!", 50, 500, arcade.color.WHITE, 32)
        arcade.draw_text("Press SPACE to Continue", 55, 350, arcade.color.WHITE, 32)
        self.lives = 3

    def draw_game(self):
        """
        Draw all the sprites, along with the score.
        """
        # Draw all the sprites.
        self.all_sprites_list.draw()
        # Draw the score in the bottom left.
        Ball.get_score(self)
        arcade.draw_text("Level " + str(self.level), 455, 10, arcade.color.WHITE, 24)
        arcade.draw_text(str(self.lives) + " Lives left", 230, 10, arcade.color.WHITE, 24)

    def draw_level_complete(self):
        # Draw at the end of every level
        arcade.draw_text("Level  " + str(self.level), 150, 400, arcade.color.WHITE, 64)
        arcade.draw_text("Complete!", 100, 290, arcade.color.WHITE, 64)
        arcade.draw_text("Press Space to Continue", 65, 210, arcade.color.WHITE, 32)

    def draw_game_over(self):
        arcade.draw_text("Game Over", 80, 330, arcade.color.WHITE, 64)
        arcade.draw_text("Press R to Restart", 80, 220, arcade.color.WHITE, 40)
        arcade.draw_text("Press Q to Quit", 120, 140, arcade.color.WHITE, 40)

    def draw_game_end(self):
        arcade.draw_text("Congratulations!", 50, 520, arcade.color.WHITE, 52)
        arcade.draw_text("You Won!", 90, 420, arcade.color.WHITE, 72)
        arcade.draw_text("Your Final Score was ", 40, 300, arcade.color.WHITE, 40)
        arcade.draw_text(str(self.score), 280, 240, arcade.color.WHITE, 40)
        arcade.draw_text("Press R to Restart", 80, 140, arcade.color.WHITE, 40)
        arcade.draw_text("Press Q to Quit", 120, 70, arcade.color.WHITE, 40)

    def on_draw(self):

        arcade.start_render()
        # Draw all the sprites.
        self.all_sprites_list.draw()
        if self.current_state == INSTRUCTION_PAGE:
            self.draw_instructions_page()

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        elif self.current_state == LEVEL_COMPLETE_PAGE:
            self.draw_level_complete()

        elif self.current_state == GAME_END:
            self.draw_game_end()

        else:
            self.draw_game_over()
        Ball.get_score(self)

        if len(self.brick_list) == 0 and self.next_level:
            if self.level < 5:
                self.level += 1
                if self.level == 1:
                    self.level_1()
                elif self.level == 2:
                    self.level_2()
                elif self.level == 3:
                    self.level_3()
                elif self.level == 4:
                    self.level_4()
                elif self.level == 5:
                    self.level_5()

            else:
                self.draw_game_end()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.Q:
            MyApplication.close(self)
        elif key == arcade.key.SPACE and len(self.brick_list) == 0:
            if not self.next_level:
                if self.level < 6:
                    self.current_state = GAME_RUNNING
                    self.draw_game()
                    self.next_level = True
                else:
                    self.current_state = GAME_END
        elif key == arcade.key.R:
            self.current_state = INSTRUCTION_PAGE
            self.draw_instructions_page()
            MyApplication.setup(self)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A \
                or key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def animate(self, delta_time):

        for ball in self.ball_list:
            if ball.center_y < 0:
                ball.kill()
                if self.lives > 0 and len(self.ball_list) == 0:
                    self.lives -= 1
                    ball = Ball(self.all_sprites_list, self.power_up_list,
                                self.wall_list, self.brick_list, self.blue_brick_list,
                                self.orange_brick_list, self.wall_brick_list, self.player_sprite, self)
                    self.ball_list.append(ball)
                    self.all_sprites_list.append(ball)
                elif self.lives <= 0:
                    for power_up in self.power_up_list:
                        power_up.kill()
                    self.draw_game_over()
                    self.current_state = GAME_OVER

        for power_up in self.power_up_list:
            if power_up.top <= 0:
                power_up.kill()

        if len(self.brick_list) == 0 and self.level > 0:
            if not self.next_level:
                for wall_brick in self.wall_brick_list:
                    wall_brick.kill()
                for ball in self.ball_list:
                    ball.kill()
                for power_up in self.power_up_list:
                    power_up.kill()
                self.current_state = LEVEL_COMPLETE_PAGE
                self.draw_level_complete()

        wall_player_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.wall_list)
        for wall in wall_player_hit_list:
            if self.player_sprite.right >= wall.left and self.player_sprite.center_x > SCREEN_WIDTH / 2:
                self.player_sprite.right = wall.left

            elif self.player_sprite.left <= wall.right:
                self.player_sprite.left = wall.right

        for wall_brick in self.wall_brick_list:
            if self.current_state != GAME_RUNNING:
                wall_brick.change_x = 0
                wall_brick.change_y = 0
            elif self.level == 4:
                if wall_brick.left < 70:
                    for brick in self.wall_brick_list:
                        brick.change_x *= -1
                elif wall_brick.right > 550:
                    for brick in self.wall_brick_list:
                        brick.change_x *= -1
            elif self.level == 5:
                if wall_brick.center_x < 90 and wall_brick.change_x < 0:
                    wall_brick.change_x = 0
                    wall_brick.change_y = -2
                elif wall_brick.center_y < 220 and wall_brick.change_y < 0:
                    wall_brick.change_x = 2
                    wall_brick.change_y = 0
                elif wall_brick.center_x > 510 and wall_brick.change_x > 0:
                    wall_brick.change_x = 0
                    wall_brick.change_y = 2
                elif wall_brick.center_y > 480 and wall_brick.change_y > 0:
                    wall_brick.change_x = -2
                    wall_brick.change_y = 0

        ball_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.ball_list)
        for ball in ball_hit_list:
            arcade.play_sound(self.player_sound)
            if ball.change_y < 0:
                ball.change_y *= -1
            if ball.center_x < self.player_sprite.center_x:
                ball.change_x = random.randrange(-5, -2)
            elif ball.center_x > self.player_sprite.center_x:
                ball.change_x = random.randrange(3, 6)
            else:
                ball.change_x = 0

        power_up_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.power_up_list)
        for power_up in power_up_hit_list:
            power_up.kill()
            if power_up.power_up_value == 0:
                self.add_life()

            elif power_up.power_up_value == 1:
                self.add_balls()

            elif power_up.power_up_value == 2:
                self.speed_up()

        self.all_sprites_list.update()
        self.ball_list.update()
        self.player_sprite.update()
        self.wall_brick_list.update()

window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
window.setup()

arcade.run()
