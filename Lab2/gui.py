import tkinter as tk


def graphic_interface(calculator):
    def clear_error():
        lbl_error["text"] = ""

    def on_key_clicked(val):
        if calculator.get_last():
            lbl_value["text"] = ""
            calculator.del_last()
        if val == ".":
            if val in lbl_value["text"]:
                return
        lbl_value["text"] += str(val)

    def on_operation_clicked(val):
        try:
            calculator.set_first_arg(lbl_value["text"])
        except Exception as e:
            lbl_error["text"] = calculator.print_error(e)
            return
        lbl_value["text"] = ""
        calculator.set_operation(val)

    def on_res_clicked():
        if calculator.get_a() is None:
            return
        try:
            calculator.set_second_arg(lbl_value["text"])
        except Exception as e:
            lbl_error["text"] = calculator.print_error(e)
            lbl_value["text"] = ""
            return
        try:
            lbl_value["text"] = str(calculator.print_result())
        except Exception as e:
            lbl_error["text"] = calculator.print_error(e)
            window.after(1000, clear_error)
            lbl_value["text"] = str(calculator.get_a())
            return
        calculator.set_first_arg(str(calculator.get_b()))

    window = tk.Tk()
    window.title("Калькулятор")
    # window.geometry("500x500")
    window.resizable(0, 0)

    lbl_value = tk.Label(font="Arial 24")
    lbl_value.grid(row=0, column=0, sticky="w")

    lbl_error = tk.Label(font="Arial 20", fg="red")
    lbl_error.grid(row=1, column=0, sticky="w")

    frm_buttons = tk.Frame(master=window, borderwidth=3, relief=tk.SUNKEN)
    btn_7 = tk.Button(master=frm_buttons, font="Arial 20", text="7", height=2, width=5,
                      command=lambda: on_key_clicked(7))
    btn_8 = tk.Button(master=frm_buttons, font="Arial 20", text="8", height=2, width=5,
                      command=lambda: on_key_clicked(8))
    btn_9 = tk.Button(master=frm_buttons, font="Arial 20", text="9", height=2, width=5,
                      command=lambda: on_key_clicked(9))
    btn_plus = tk.Button(master=frm_buttons, font="Arial 20", text="+", height=2, width=5,
                         command=lambda: on_operation_clicked("+"))

    btn_7.grid(row=0, column=0)
    btn_8.grid(row=0, column=1)
    btn_9.grid(row=0, column=2)
    btn_plus.grid(row=0, column=3)

    btn_4 = tk.Button(master=frm_buttons, font="Arial 20", text="4", height=2, width=5,
                      command=lambda: on_key_clicked(4))
    btn_5 = tk.Button(master=frm_buttons, font="Arial 20", text="5", height=2, width=5,
                      command=lambda: on_key_clicked(5))
    btn_6 = tk.Button(master=frm_buttons, font="Arial 20", text="6", height=2, width=5,
                      command=lambda: on_key_clicked(6))
    btn_minus = tk.Button(master=frm_buttons, font="Arial 20", text="-", height=2, width=5,
                          command=lambda: on_operation_clicked("-"))

    btn_4.grid(row=1, column=0)
    btn_5.grid(row=1, column=1)
    btn_6.grid(row=1, column=2)
    btn_minus.grid(row=1, column=3)

    btn_1 = tk.Button(master=frm_buttons, font="Arial 20", text="1", height=2, width=5,
                      command=lambda: on_key_clicked(1))
    btn_2 = tk.Button(master=frm_buttons, font="Arial 20", text="2", height=2, width=5,
                      command=lambda: on_key_clicked(2))
    btn_3 = tk.Button(master=frm_buttons, font="Arial 20", text="3", height=2, width=5,
                      command=lambda: on_key_clicked(3))
    btn_multiply = tk.Button(master=frm_buttons, font="Arial 20", text="*", height=2, width=5,
                             command=lambda: on_operation_clicked("*"))

    btn_1.grid(row=2, column=0)
    btn_2.grid(row=2, column=1)
    btn_3.grid(row=2, column=2)
    btn_multiply.grid(row=2, column=3)

    btn_dot = tk.Button(master=frm_buttons, font="Arial 20", text=".", height=2, width=5,
                        command=lambda: on_key_clicked("."))
    btn_0 = tk.Button(master=frm_buttons, font="Arial 20", text="0", height=2, width=5,
                      command=lambda: on_key_clicked(0))
    btn_res = tk.Button(master=frm_buttons, font="Arial 20", text="=", height=2, width=5, command=on_res_clicked)
    btn_divide = tk.Button(master=frm_buttons, font="Arial 20", text="/", height=2, width=5,
                           command=lambda: on_operation_clicked("/"))

    btn_dot.grid(row=3, column=0)
    btn_0.grid(row=3, column=1)
    btn_res.grid(row=3, column=2)
    btn_divide.grid(row=3, column=3)

    frm_buttons.grid(row=2, column=0)

    window.mainloop()
