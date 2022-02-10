import comlex
import calc
import ui


def controller():
    inp = ui.inp() # TODO разнести ипут для компл и для рац калькул.
    if ui.check(inp): # выод 1 или 0 j
        res = comlex.compl(inp)
    else:
        res = calc.calc(inp)
    ui.output(res)