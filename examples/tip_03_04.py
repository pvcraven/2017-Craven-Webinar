"""
Tip 3:
    Function completion
    PEP-8
    Spell checking

Tip 4:
    Use type hinting
"""

# Function completion when you type-to
# Pull up documentation with Ctrl-Q
# If you try setting the background color with only 2 numbers, you'll get an type hint warning
# Forget to put a space after a comma, and get a PEP-8 warning
# This is a program a student wrote his second week of class
# He wrote it and, like many students, also made sure PyCharm showed no issues.
# See that you don't have to declare or create classes to do stuff in arcade!

import arcade

arcade.open_window(800, 600, "Flying V")

arcade.set_background_color((53, 242, 252))


arcade.start_render()

"""Guitar Body"""
arcade.draw_triangle_filled(450, 300, 150, 300, 20, 100, arcade.color.CADMIUM_RED)
arcade.draw_triangle_filled(450, 300, 150, 300, 20, 500, arcade.color.CADMIUM_RED)

"""Guitar Neck"""
arcade.draw_rectangle_filled(450, 300, 350, 50, arcade.color.DEEP_CHAMPAGNE)

"""Guitar Head"""
arcade.draw_triangle_filled(625, 260, 625, 340, 751, 300, arcade.color.BLACK)

"""Guitar Pickups"""
arcade.draw_rectangle_filled(270, 300, 50, 80, arcade.color.SILVER)

"""Fret Separators"""
arcade.draw_line(625, 325, 625, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(604, 325, 604, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(583, 325, 583, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(562, 325, 562, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(541, 325, 541, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(520, 325, 520, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(499, 325, 499, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(478, 325, 478, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(457, 325, 457, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(436, 325, 436, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(415, 325, 415, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(394, 325, 394, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(373, 325, 373, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(352, 325, 352, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(331, 325, 331, 275, arcade.color.BROWN, border_width=2)
arcade.draw_line(310, 325, 310, 275, arcade.color.BROWN, border_width=2)

"""Fret Indicators"""
arcade.draw_circle_filled(572.5, 300, 5, arcade.color.LIGHT_BROWN)
arcade.draw_circle_filled(530.5, 300, 5, arcade.color.LIGHT_BROWN)
arcade.draw_circle_filled(383.5, 312, 5, arcade.color.LIGHT_BROWN)
arcade.draw_circle_filled(383.5, 288, 5, arcade.color.LIGHT_BROWN)

"""Strings"""
arcade.draw_line(260, 280, 640, 280, arcade.color.GRAY, border_width=1)
arcade.draw_line(260, 288, 670, 288, arcade.color.GRAY, border_width=1)
arcade.draw_line(260, 296, 700, 296, arcade.color.GRAY, border_width=1)
arcade.draw_line(260, 304, 700, 304, arcade.color.GRAY, border_width=1)
arcade.draw_line(260, 312, 670, 312, arcade.color.GRAY, border_width=1)
arcade.draw_line(260, 320, 640, 320, arcade.color.GRAY, border_width=1)

"""String Exits"""
arcade.draw_circle_filled(640, 280, 2, arcade.color.SILVER)
arcade.draw_circle_filled(670, 288, 2, arcade.color.SILVER)
arcade.draw_circle_filled(700, 296, 2, arcade.color.SILVER)
arcade.draw_circle_filled(700, 304, 2, arcade.color.SILVER)
arcade.draw_circle_filled(670, 312, 2, arcade.color.SILVER)
arcade.draw_circle_filled(640, 320, 2, arcade.color.SILVER)

"""String Entrances"""
arcade.draw_circle_filled(260, 280, 2, arcade.color.BLACK)
arcade.draw_circle_filled(260, 288, 2, arcade.color.BLACK)
arcade.draw_circle_filled(260, 296, 2, arcade.color.BLACK)
arcade.draw_circle_filled(260, 304, 2, arcade.color.BLACK)
arcade.draw_circle_filled(260, 312, 2, arcade.color.BLACK)
arcade.draw_circle_filled(260, 320, 2, arcade.color.BLACK)

"""Volume and Tone Knobs"""
arcade.draw_circle_filled(160, 190, 10, arcade.color.BLACK)
arcade.draw_circle_filled(210, 215, 10, arcade.color.BLACK)
arcade.draw_circle_filled(260, 240, 10, arcade.color.BLACK)
arcade.draw_circle_outline(160, 190, 11, arcade.color.ANTI_FLASH_WHITE, border_width=2)
arcade.draw_circle_outline(210, 215, 11, arcade.color.ANTI_FLASH_WHITE, border_width=2)
arcade.draw_circle_outline(260, 240, 11, arcade.color.ANTI_FLASH_WHITE, border_width=2)

arcade.finish_render()

arcade.run()
