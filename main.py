start = 0
Elapse = 0

def on_button_pressed_a():
    global start
    start = input.running_time()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Elapse
    Elapse = input.running_time() - start
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_number(Elapse / 1000)
basic.forever(on_forever)
