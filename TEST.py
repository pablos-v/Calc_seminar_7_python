import seminar7.ui as ui
import mod1
import mod2

def controller():
    inp = ui.input()
    if check(inp): # выод 1 или 0 j
        res = mod1.calc1(inp)
    else:
        res = mod2.calc2(inp)
    ui.output(res)

# ff = '(2.45+2)*2'
# print(eval(ff))

