import tkinter as tk
import sys
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("700x700")
calculation = []
field = tk.Entry(root, width=50, borderwidth=7)
field.grid(row=0, column=0, columnspan=7)
error = ""


def clr():
    global field
    global calculation
    calculation = []
    field.delete(0, tk.END)


class Operations:

    def power(self, x, y):
        global calculation
        global error
        try:
            return x ** y
        except:
            field.delete(0, tk.END)
            error = "ERROR:", str(sys.exc_info()[0])[7:-1]
            calculation = []

    def product(self, x, y):
        global calculation
        global error
        try:
            return x * y
        except:
            field.delete(0, tk.END)
            error = "ERROR:", str(sys.exc_info()[0])[7:-1]
            calculation = []

    def division(self, x, y):
        global calculation
        global error
        try:
            return x/y
        except:
            field.delete(0, tk.END)
            error = "ERROR:", str(sys.exc_info()[0])[7:-1]
            calculation = []

    def add(self, x, y):
        global error
        global calculation
        try:
            return x + y
        except:
            field.delete(0, tk.END)
            error = "ERROR:", str(sys.exc_info()[0])[7:-1]
            calculation = []

    def subtract(self, x, y):
        global error
        global calculation
        try:
            return x - y
        except:
            field.delete(0, tk.END)
            error = "ERROR:", str(sys.exc_info()[0])[7:-1]
            calculation = []


op = Operations()


def append_(text):
    global calculation
    global field
    current = field.get()
    field.delete(0, tk.END)
    field.insert(0, str(current)+str(text))
    calculation = list(calculation)
    calculation.append(str(text))


def fin(calculation):
    global field
    global error
    operation_counts = calculation.count(
        "**"), calculation.count("*"), calculation.count("/"), calculation.count("+"), calculation.count("-"), calculation.count(".")
    power, product, division, add, subtract, points = operation_counts
    i = 0
    while i+1 <= len(calculation):
        try:
            if calculation[i].isnumeric() and calculation[i+1].isnumeric():
                k = "".join(calculation[i:i+2])
                del calculation[i:i+2]
                calculation.insert(i, k)
                continue
            i += 1
        except IndexError:
            break
    loop_count = 0
    while len(calculation) > 1:
        try:
            loop_count += 1
            if loop_count > 500:
                field.delete(0, tk.END)
                field.insert(0, "Something went wrong.")
                calculation = []
                break
            if points > 0:
                a = 0
                while a+1 <= len(calculation):
                    if calculation[a] == ".":
                        prev, post = calculation[a-1], calculation[a+1]
                        result = f"{prev}.{post}"
                        calculation.insert(a+2, result)
                        del calculation[a-1:a+2]
                    a += 1

            if power > 0:
                a = 0
                while a+1 <= len(calculation):
                    if calculation[a] == "**":
                        prev, post = float(
                            calculation[a-1]), float(calculation[a+1])
                        result = str(op.power(prev, post))
                        calculation.insert(a+2, result)
                        del calculation[a-1:a+2]
                    a += 1
            if product > 0:
                a = 0
                while a+1 <= len(calculation):
                    try:
                        if calculation.index("*") > calculation.index("/"):
                            break
                    except ValueError:
                        pass
                    if calculation[a] == "*":
                        prev, post = float(
                            calculation[a-1]), float(calculation[a+1])
                        result = str(op.product(prev, post))
                        calculation.insert(a+2, result)
                        del calculation[a-1:a+2]
                    a += 1
            if division > 0:
                a = 0
                while a+1 <= len(calculation):
                    if calculation[a] == "/":
                        prev, post = float(
                            calculation[a-1]), float(calculation[a+1])
                        result = str(op.division(prev, post))
                        calculation.insert(a+2, result)
                        del calculation[a-1:a+2]
                    a += 1
            if add > 0:
                a = 0
                while a+1 <= len(calculation):
                    try:
                        if calculation.index("+") > calculation.index("-"):
                            break
                    except ValueError:
                        pass
                    if calculation[a] == "+":
                        prev, post = float(
                            calculation[a-1]), float(calculation[a+1])
                        result = str(op.add(prev, post))
                        calculation.insert(a+2, result)
                        del calculation[a-1:a+2]
                    a += 1
            if subtract > 0:
                a = 0
                while a+1 <= len(calculation):
                    if calculation[a] == "-":
                        prev, post = float(
                            calculation[a-1]), float(calculation[a+1])
                        result = str(op.subtract(prev, post))
                        calculation.insert(a+2, result)
                        del calculation[a-1:a+2]
                    a += 1
            print(calculation)
            if calculation[0][0].isnumeric():
                field.delete(0, tk.END)
                field.insert(0, "".join(calculation))
            else:
                field.insert(0, error)
        except:
            print("Something went wrong.")


B0 = tk.Button(root, text="0", command=lambda: append_(0), width=7)
B1 = tk.Button(root, text="1", command=lambda: append_(1), width=7)
B2 = tk.Button(root, text="2", command=lambda: append_(2), width=7)
B3 = tk.Button(root, text="3", command=lambda: append_(3), width=7)
B4 = tk.Button(root, text="4", command=lambda: append_(4), width=7)
B5 = tk.Button(root, text="5", command=lambda: append_(5), width=7)
B6 = tk.Button(root, text="6", command=lambda: append_(6), width=7)
B7 = tk.Button(root, text="7", command=lambda: append_(7), width=7)
B8 = tk.Button(root, text="8", command=lambda: append_(8), width=7)
B9 = tk.Button(root, text="9", command=lambda: append_(9), width=7)

B0.grid(row=2, column=0)
B1.grid(row=2, column=1)
B2.grid(row=2, column=2)
B3.grid(row=2, column=3)
B4.grid(row=3, column=0)
B5.grid(row=3, column=1)
B6.grid(row=3, column=2)
B7.grid(row=3, column=3)
B8.grid(row=4, column=0)
B9.grid(row=4, column=1)

Dvision = tk.Button(root, text="/", command=lambda: append_("/"), width=7)
Power = tk.Button(root, text="**", command=lambda: append_("**"), width=7)
Product = tk.Button(root, text="*", command=lambda: append_("*"), width=7)
Minus = tk.Button(root, text="-", command=lambda: append_("-"), width=7)
Plus = tk.Button(root, text="+", command=lambda: append_("+"), width=7)
Dot = tk.Button(root, text=".", command=lambda: append_("."), width=7)
CLR = tk.Button(root, text="CLR", command=lambda: clr(), width=7)
Equal = tk.Button(
    root, text="=", command=lambda: fin(calculation), width=7)
Plus.grid(row=2, column=4)
Minus.grid(row=3, column=4)
Product.grid(row=4, column=4)
Dvision.grid(row=5, column=2)
Power.grid(row=4, column=3)
Dot.grid(row=4, column=2)
CLR.grid(row=5, column=3)
Equal.grid(row=5, column=4)
tk.mainloop()
