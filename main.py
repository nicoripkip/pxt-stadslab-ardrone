def on_forever():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        """)
basic.forever(on_forever)

def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)
