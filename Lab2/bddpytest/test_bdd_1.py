import threading
import time
from pytest_bdd import scenario, given, when, then, parsers
from calculator import click_button, Calculator, graphic_interface
import pywinauto as pwa


def str_to_btn(string):
    s2b_dict = {'1': 'btn_1', '2': 'btn_2', '3': 'btn_3', '4': 'btn_4',
                '5': 'btn_5', '6': 'btn_6', '7': 'btn_7', '8': 'btn_8',
                '9': 'btn_9', '0': 'btn_0', '.': 'btn_dot', '+': 'btn_plus',
                '-': 'btn_minus', '*': 'btn_multiply', '/': 'btn_divide',
                '=': 'btn_res'}
    buttons = []
    for char in string:
        buttons.append(s2b_dict[char])
    return buttons


def find_app_and_action(buttons):
    button_list = ["btn_divide", "", "btn_res", "btn_0", "btn_dot",
                   "btn_multiply", "btn_3", "btn_2", "btn_1",
                   "btn_minus", "btn_6", "btn_5", "btn_4",
                   "btn_plus", "btn_9", "btn_8", "btn_7"]
    app = pwa.Application(backend="uia").connect(title="Калькулятор")
    main_window = app.window(title="Калькулятор")
    for btn in buttons:
        click_button(main_window, btn, button_list)
    time.sleep(1)
    main_window['Button{19}'].click_input()


def start_calculator(calc):
    graphic_interface(calc)


@scenario('my_features/first.feature', 'Sum of integers')
def test_sum_of_integers():
    pass


@given(parsers.cfparse("the first number is {a:Str}, the second number is {b:Str}",
                       extra_types={"Str": str}),
       target_fixture="variables")
def existing_variables(a, b):
    return {'a': a, 'b': b, 'operation': ''}


@when(parsers.cfparse("the operation is {operation:Str}",
                      extra_types={"Str": str}))
def set_operation(variables, operation):
    variables["operation"] += operation


@then(parsers.cfparse("the result should be {expected_res:Str}",
                      extra_types={"Str": str}))
def final_result(variables, expected_res):
    buttons = str_to_btn(variables["a"] + variables["operation"] + variables["b"] + '=')
    my_calc = Calculator()
    th1 = threading.Thread(target=start_calculator, args=(my_calc,))
    th2 = threading.Timer(interval=3, function=find_app_and_action, args=(buttons,))
    th1.start()
    th2.start()
    th2.join()
    if expected_res == 'ZeroDivisionError':
        assert my_calc.msg == 'Деление на ноль'
    else:
        assert my_calc.last == float(expected_res)
