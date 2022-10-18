let start = 0
let Elapse = 0
input.onButtonPressed(Button.A, function () {
    start = input.runningTime()
})
input.onButtonPressed(Button.B, function () {
    Elapse = input.runningTime() - start
})
basic.forever(function () {
    basic.showNumber(Elapse / 1000)
})
