import comlex
import calc
import ui
import spy


def controller():
    inp = ui.inp()
    if ui.check(inp): 
        res = comlex.compl(inp)
    else:
        res = calc.calc(inp)
    spy.my_logger(inp,res)
    ui.output(res)