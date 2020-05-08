import tkinter as tk


def convert():
    input_value = float(var_input.get())
    grams_value = input_value * 1000
    var_grams.set('{}g'.format(grams_value))

    pounds_value = input_value * 2.20462
    var_pounds.set('{}lbs'.format(pounds_value))

    ounces_value = input_value * 35.274
    var_ounces.set('{}oz'.format(ounces_value))


window = tk.Tk()
window.rowconfigure([0, 1], minsize=30, weight=1)
window.columnconfigure([0, 1, 2], minsize=30, weight=1)

var_input = tk.StringVar()
var_grams = tk.StringVar()
var_pounds = tk.StringVar()
var_ounces = tk.StringVar()

lbl_kg = tk.Label(window, text="kg")
txt_input = tk.Entry(window, textvariable=var_input)
btn_convert = tk.Button(window, text="Convert", command=convert)
lbl_grams = tk.Label(window, textvariable=var_grams)
lbl_pounds = tk.Label(window, textvariable=var_pounds)
lbl_ounces = tk.Label(window, textvariable=var_ounces)

lbl_kg.grid(row=0, column=0)
txt_input.grid(row=0, column=1)
btn_convert.grid(row=0, column=2)
lbl_grams.grid(row=1, column=0)
lbl_pounds.grid(row=1, column=1)
lbl_ounces.grid(row=1, column=2)

window.mainloop()
