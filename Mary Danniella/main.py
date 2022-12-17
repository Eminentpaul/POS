from tkinter import *
from tkinter import ttk, messagebox as mgs
from ttkthemes import themed_tk as tk
import sqlite3
import _datetime as d
import os
import tempfile

root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")
root.configure(bg="#FBFADD")
# root.attributes("-fullscreen", True)
root.geometry("1350x750+0+0")
root.title("MARY DANIELLA RECOREDS")
root.iconbitmap("md.ico")


global index

index = 1

# root.resizable(0, 0)

def main():
    # try:
    menubar = Menu(root)
    root.configure(menu=menubar)

    dated = d.datetime.today()
    table_name = dated.date()

    year = table_name.year
    month = table_name.strftime("%B")
    day = table_name.day

    index = 1
    global Daily
    Daily = f"{str(day)}_{str(month)}_{str(year)}"

    def admin_login():
        # try:
        username = username_entry.get()
        password = password_entry.get()

        if (username == "" or password == ""):
            mgs.showinfo("Message", "All are required")
        else:
            cons = sqlite3.connect('Mary_Daniella.db')
            cursors = cons.cursor()
            cursors.execute("SELECT * FROM Admin")
            rows = cursors.fetchall()

            users = []
            passd = []

            for row in rows:
                users.append(row[0])
                passd.append(row[1])
                pass

            for x in users:
                user = x
                pass
            for y in passd:
                passs = y
                pass
            if user == username and passs == password:
                if (cursors.execute("SELECT * FROM Admin WHERE password='" + password + "'")):
                    mgs.showinfo("Message", "Successfully log-in")
                    username_entry.delete(0, END)
                    password_entry.delete(0, END)
                    admin_dashboard()
            else:
                mgs.showinfo("Message", "Incorrect username or password")
        # except:
        #     mgs.showinfo("Message", "ERROR")

    def cashier_logins():
        # try:
        global Daily

        con = sqlite3.connect(f"Store_{month}_{year}.db")
        cursor = con.cursor()

        q = f"""CREATE TABLE IF NOT EXISTS exp_{Daily}(
            Description text,
            Amount text)"""

        table = f"""CREATE TABLE IF NOT EXISTS today_{Daily}(
                customer_name text,
                phone_number integer,
                kg integer,
                product text,
                total intger,
                amount_words text)"""
        if (cursor.execute(table) and cursor.execute(q)):

            username = username_entry.get()
            password = password_entry.get()

            if (username == "" or password == ""):
                mgs.showinfo("Message", "All are required")
            else:
                cons = sqlite3.connect('Mary_Daniella.db')
                cursors = cons.cursor()
                cursors.execute("SELECT * FROM Staff")
                rows = cursors.fetchall()

                users = []
                passd = []

                for row in rows:
                    users.append(row[0])
                    passd.append(row[1])
                    pass

                for x in users:
                    user = x
                    pass
                for y in passd:
                    passs = y
                    pass
                if user == username and passs == password:
                    if (cursors.execute("SELECT * FROM Staff WHERE password='" + password + "'")):
                        mgs.showinfo("Message", "Successfully log-in")
                        username_entry.delete(0, END)
                        password_entry.delete(0, END)
                        cashier_dashboard()
                else:
                    mgs.showinfo("Message", "Incorrect username or password")
        else:
            mgs.showinfo("Message", "Not Created")
        # except:
        #     mgs.showinfo("Message", "ERROR")

    def exit():
        response = mgs.askyesno("LOGOUT", "Are You Sure you want to Exit?")
        if response == 1:
            root.quit()
        else:
            pass

    bus_name = Label(root, text="MARY DANIELLA GAS", bg="#FBFADD", fg="red",
                     font=("tahoma", 35, "bold"), pady=40).pack()

    loginframe = LabelFrame(root, text="LOGIN", bg="#FBFADD",
                            font=("tahoma", 20, "bold"), fg="green",
                            borderwidth='2',
                            relief=GROOVE, height=200, width=550)
    loginframe.pack()

    username = Label(loginframe, text="USERNAME: ",
                     bg="#FBFADD", fg="#315C3B",
                     font=("verdana", 12, "bold")).place(x=65, y=15)
    username_entry = Entry(loginframe, fg="#315C3B",
                           font=("verdana", 12, "bold"), bg="#DDF0ED")
    username_entry.place(x=210, y=16)

    password_number = Label(loginframe, text="PASSWORD: ", bg="#FBFADD", fg="#315C3B",
                            font=("verdana", 12, "bold")).place(x=65, y=75)
    password_entry = Entry(loginframe, fg="#315C3B",
                           font=("verdana", 12, "bold"), show="*", bg="#DDF0ED")
    password_entry.place(x=210, y=76)

    button = ttk.Button(loginframe, text="Staff Login",
                        command=cashier_logins).place(x=150, y=110)

    button2 = ttk.Button(loginframe, text="Admin Login",
                         command=admin_login).place(x=300, y=110)
    button3 = ttk.Button(root, text="EXIT",
                         command=exit).place(x=1200, y=600)
    # except:
    #     mgs.showinfo("Message", "ERROR")


def cashier_dashboard():
    root.withdraw()
    from tkinter import ttk, messagebox as mg
    from ttkthemes import themed_tk as tk
    import sqlite3
    import _datetime as d
    import os
    import tempfile
    import time

    cashier = tk.ThemedTk()
    cashier.get_themes()
    cashier.set_theme("radiance")
    cashier.configure(bg="#FBFADD")
    # root.attributes("-fullscreen", True)
    cashier.geometry("1350x700+0+0")
    cashier.resizable(0, 0)
    cashier.title("MARY DANIELLA RECOREDS")
    cashier.iconbitmap("md.ico")

    menubar = Menu(cashier)
    cashier.configure(menu=menubar)

    # comp_name = Label(cashier, text="""MARY DANIELLA COOKING GAS""", font=('tahoma', 15, 'bold'))

    index = 1
    global price

    con = sqlite3.connect(f"Mary_Daniella.db")
    cursor = con.cursor()

    table = ("SELECT * FROM Kg_amount")
    cursor.execute(table)
    row = cursor.fetchall()

    for rows in row:
        if rows[0] == 'kg_amount':
            price = rows[1]

    dated = d.datetime.today()
    table_name = dated.date()
    # total = amount
    # dd = d.datetime()

    year = table_name.year
    month = table_name.strftime("%B").upper()

    def databases():
        dated = d.datetime.today()
        table_name = dated.date()

        year = table_name.year
        month = table_name.strftime("%B")
        day = table_name.day

        con = sqlite3.connect(f'Year_{year}.db')
        cursor = con.cursor()

        expense_month = f"""CREATE TABLE IF NOT EXISTS Expense_{month}(
                        Description text,
                        Amount integer)"""
        income_month = f"""CREATE TABLE IF NOT EXISTS Sales_{month}(
                        Date text,
                        Total_Kg integer,
                        Total_Amount integer)"""
        sales = f"""CREATE TABLE IF NOT EXISTS Trans_{year}(
                Month text,
                Total_Kg integer,
                Total_Exp integer,
                Total_Amount integer)"""
        customer = f"""CREATE TABLE IF NOT EXISTS Customers_{year}(
            Customers text,
            Kg text
        )"""
        cursor.execute(expense_month)
        cursor.execute(income_month)
        cursor.execute(sales)
        cursor.execute(customer)
        con.close()

    databases()

    # def calculator():
    #     from PIL import ImageTk, Image
    #     toplevel = Toplevel()
    #     toplevel.minsize(250, 240)
    #     toplevel.resizable(0, 0)
    #
    #     def on_click(number):
    #         # entry.delete(0, END)
    #         current = entry.get()
    #         entry.delete(0, END)
    #         entry.insert(0, f"{current}{number}")
    #
    #     def delete():
    #         entry.delete(0, END)
    #
    #     def plus():
    #         try:
    #             global first_num
    #             global operation
    #
    #             operation = "plus"
    #
    #             first_number = entry.get()
    #             first_num = int(first_number)
    #             entry.delete(0, END)
    #         except:
    #             pass
    #
    #     def minus():
    #         try:
    #             global first_num
    #             global operation
    #
    #             operation = "minus"
    #
    #             first_number = entry.get()
    #             first_num = int(first_number)
    #             entry.delete(0, END)
    #         except:
    #             pass
    #
    #     def times():
    #         try:
    #             global first_num
    #             global operation
    #
    #             operation = "times"
    #
    #             first_number = entry.get()
    #             first_num = int(first_number)
    #             entry.delete(0, END)
    #         except:
    #             pass
    #
    #     def divide():
    #         try:
    #             global first_num
    #             global operation
    #
    #             operation = "divide"
    #
    #             first_number = entry.get()
    #             first_num = int(first_number)
    #             entry.delete(0, END)
    #         except:
    #             pass
    #
    #     def equal_to():
    #         global operation
    #         second_number = int(entry.get())
    #         entry.delete(0, END)
    #
    #         if operation == "plus":
    #             result = entry.insert(0, first_num + second_number)
    #             return result
    #         elif operation == "minus":
    #             result = entry.insert(0, first_num - second_number)
    #             return result
    #         elif operation == "times":
    #             result = entry.insert(0, first_num * second_number)
    #             return result
    #         elif operation == "divide":
    #             result = entry.insert(0, first_num // second_number)
    #             return result
    #
    #     def sqr():
    #         try:
    #             first = entry.get()
    #             entry.delete(0, END)
    #
    #             first_num = int(first)
    #
    #             result = entry.insert(0, first_num ** 0.5)
    #             return result
    #         except:
    #             pass
    #
    #     def square():
    #         first = entry.get()
    #         entry.delete(0, END)
    #
    #         first_num = int(first)
    #
    #         result = entry.insert(0, first_num * first_num)
    #         return result
    #
    #     def percent():
    #         try:
    #             first = entry.get()
    #             entry.delete(0, END)
    #
    #             first_num = int(first)
    #
    #             result = int(entry.insert(0, first_num / 100))
    #             return result
    #         except:
    #             pass
    #
    #     entry = ttk.Entry(toplevel, justify="right", width=23, font=("tahoma", 12, "bold"))
    #     entry.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
    #
    #     # divisionImage = ImageTk.PhotoImage(Image.open("image/divi.png"))
    #     # squareImage = PhotoImage(file="square.png")
    #     # rootImage = PhotoImage(file="sqr.png")
    #     # perImage = PhotoImage(file="percentw.png")
    #     # delImage = PhotoImage(file="del.png")
    #
    #     # rootbtn = ttk.Button(toplevel, image=rootImage, command=sqr).place(x=3, y=35)
    #     # squarebtn = ttk.Button(toplevel, image=squareImage, command=square).place(x=65, y=35)
    #     # perbtn = ttk.Button(toplevel, image=perImage, command=percent).place(x=127, y=35)
    #     delbtn = ttk.Button(toplevel, text="C", width=1, command=delete).place(x=192, y=35)
    #
    #     btn7 = ttk.Button(toplevel, text="7", width=1, command=lambda: on_click(7)).place(x=4, y=70)
    #     btn8 = ttk.Button(toplevel, text="8", width=1, command=lambda: on_click(8)).place(x=67, y=70)
    #     btn9 = ttk.Button(toplevel, text="9", width=1, command=lambda: on_click(9)).place(x=129, y=70)
    #     divibtn = ttk.Button(toplevel, text="/", width=1, command=divide).place(x=194, y=70)
    #
    #     btn4 = ttk.Button(toplevel, text="4", width=1, command=lambda: on_click(4)).place(x=4, y=105)
    #     btn5 = ttk.Button(toplevel, text="5", width=1, command=lambda: on_click(5)).place(x=67, y=105)
    #     btn6 = ttk.Button(toplevel, text="6", width=1, command=lambda: on_click(6)).place(x=129, y=105)
    #     timesbtn = ttk.Button(toplevel, text="*", width=1, command=times).place(x=194, y=105)
    #
    #     btn1 = ttk.Button(toplevel, text="1", width=1, command=lambda: on_click(1)).place(x=4, y=140)
    #     btn2 = ttk.Button(toplevel, text="2", width=1, command=lambda: on_click(2)).place(x=67, y=140)
    #     btn3 = ttk.Button(toplevel, text="3", width=1, command=lambda: on_click(3)).place(x=129, y=140)
    #     minusbtn = ttk.Button(toplevel, text="-", width=1, command=minus).place(x=194, y=140)
    #
    #     btn0 = ttk.Button(toplevel, text="0", width=1, command=lambda: on_click(0)).place(x=4, y=175)
    #     pointbtn = ttk.Button(toplevel, text=".", width=1, command=lambda: on_click(".")).place(x=67, y=175)
    #     equalbtn = ttk.Button(toplevel, text="=", width=1, command=equal_to).place(x=129, y=175)
    #     plusbtn = ttk.Button(toplevel, text="+", width=1, command=plus).place(x=194, y=175)

    def totals():
        try:
            global price
            global amount
            price = int(price)
            done = kg_entry.get()

            if (done == ""):
                try:
                    value = total_entry.get()
                    p = int(value) / price
                    kg_entry.delete(0, END)
                    kg_entry.insert(0, p)
                    submit = ttk.Button(cashier, text="SUBMIT", command=submits).place(x=340, y=405)
                except:
                    total_entry.delete(0, END)
                    mg.showinfo("Message", "The Fields Requires only Number")

            elif (total_entry.get() == ""):
                try:
                    kg = float(done)
                    amount = price * kg
                    total_entry.delete(0, END)
                    total = total_entry.insert(0, amount)
                    submit = ttk.Button(cashier, text="SUBMIT", command=submits).place(x=340, y=405)
                except:

                    mg.showinfo("Message", "The Fields Requires only Number")
            else:
                mg.showinfo("Message", "The Field Number of Kg and Total Amount are Empty")
        except:
            mg.showinfo("Message", "The Field Number of Kg and Total Amount are Empty")
            kg_entry.delete(0, END)

    def resets():
        customer_entry.delete(0, END)
        phone_entry.delete(0, END)
        kg_entry.delete(0, END)
        total_entry.delete(0, END)
        amount_in_words.delete(1.0, END)
        cyl_gas.set("gas")
        submit = ttk.Button(cashier, text="SUBMIT", state=DISABLED).place(x=340, y=405)
        # print_button = ttk.Button(cashier, text="PRINT", state=DISABLED).place(x=750, y=400)

    def submits():
        global index
        global amount
        global receipts
        global name, kg

        name = customer_entry.get().upper()
        done = phone_entry.get()
        phone = f'+234-{done}'
        kg = float(kg_entry.get())
        product = cyl_gas.get().upper()
        amount_word = amount_in_words.get(1.0, END).upper()

        if (name == "" or phone == "" or kg == "" or amount_word == ""):
            mg.showinfo("Message", "All Fields are required")
        elif (len(done) > 11 or len(done)<11):
            mg.showinfo("Message", "Phone Number should not be Less or Greater than 11")
        else:
            dated = d.datetime.today()
            table_name = dated.date()
            total = amount

            year = table_name.year
            month = table_name.strftime("%B")
            day = table_name.day

            days = table_name.today().strftime("%d/%b/%Y")

            Daily = f"{str(day)}_{str(month)}_{str(year)}"

            con = sqlite3.connect(f"Store_{month}_{year}.db")
            cursor = con.cursor()
            insert = f"INSERT INTO today_{Daily} VALUES('" + name + "', '" + str(phone) + "', '" + str(
                kg) + "', '" + product + "', '" + str(total) + "', '" + amount_word + "')"
            if (cursor.execute(insert)):
                cursor.execute('commit')
                # print_button = ttk.Button(cashier, text="PRINT", command=prints).place(x=750, y=400)
                # mg.showinfo("Message", "Success")

                query = f"SELECT * FROM today_{Daily}"
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    if (row[0] == name):
                        print_out = f"""
    MARY DANIELLA COOKING GAS
    Address: Plot 45 Iwollo-Oghe Exp. Rd,
    opp. Timber Saw Mill, Ezeagu.
    Tel:- 08065737173, 09060457842, 09064720285

    JOB DESCRIPTION:
    NAME: {row[0]}
    PHONE NO.: {row[1]}
    NO. OF KG: {row[2]}kg
    PRODUCT: {row[3]}
    TOTAL: N{row[4]}
    AMOUNT IN WORDS: {row[5]}
    DATE: {days}
                """
                        receipts = Text(cashier, width=25, font=("arial", 12),
                                        bg="#EFF4F8",
                                        height=15, fg="#315C3B")
                        receipts.place(x=500, y=100)
                        receipts.insert(1.0, print_out)

                        print_button = ttk.Button(cashier, text="PRINT",
                                                  command=prints).place(x=550, y=400)

                        cust_insert()
                        std_list()
                        monthly_sales()
                        monthly_data()
                        customer_record()
                        resets()

                        customer_entry.delete(0, END)
                        phone_entry.delete(0, END)
                        kg_entry.delete(0, END)
                        amount_in_words.delete(1.0, END)
                        total_entry.delete(0, END)

                con.close()
            else:
                mg.showinfo("Message", "Not Success")

    def std_list():
        global total
        global index
        global monthly_total
        global monthly_kg
        dated = d.datetime.today()
        table_name = dated.date()

        year = table_name.year
        month = table_name.strftime("%B")
        day = table_name.day

        Daily = f"{str(day)}_{str(month)}_{str(year)}"

        con = sqlite3.connect(f"Store_{month}_{year}.db")
        cursor = con.cursor()
        query = f"SELECT * FROM today_{Daily}"
        cursor.execute(query)
        rows = cursor.fetchall()
        for i in treeview.get_children():
            treeview.delete(i)
            pass

        # insData = f"           NAME                     PHONE NUMBER         NO. OF KG           PRODUCT          TOTAL(N)            AMOUNT IN WORDS    "
        # listbox.insert(0, insData)

        val = []
        dd = []
        for row in rows:
            val.append(row[4])
            dd.append(row[2])
            # print(row[0])
            # insertData = f"  {row[0]}    {row[1]}               {row[2]} kg                     {row[3]}                    {row[4]}                 {row[5]}"
            # listbox.insert(listbox.size() + 1, insertData)
            # # index += 1
            treeview.insert("", 'end', values=row)
        total = 0
        for x in val:
            total += x
            monthly_total = total
        total_label = Label(cashier,
                            text=
                            f"""TOTAL SALES: 
    N{total}""", bg="#FBFADD", fg="red",
                            font=("verdana", 12, "bold")).place(x=600, y=450)

        month_kg = 0
        for _ in dd:
            month_kg += round(float(_), 1)
            monthly_kg = month_kg

        # print(month_kg)
        monthly_data()
        monthly_sales()
        yearly_sales()

    def cust_insert():
        custormer_name = customer_entry.get().upper()
        kgs = float(kg_entry.get())

        dated = d.datetime.today()
        table_name = dated.date()

        year = table_name.year
        month = table_name.strftime("%B")
        day = table_name.day

        con = sqlite3.connect(f"Year_{year}.db")
        curs = con.cursor()

        insert = f"INSERT INTO Customers_{year} VALUES('" + custormer_name + "', '" + str(kgs) + "')"
        if (curs.execute(insert)):
            curs.execute('commit')

    def customer_record():
        dated = d.datetime.today()
        table_name = dated.date()

        year = table_name.year
        month = table_name.strftime("%B")
        day = table_name.day

        con = sqlite3.connect(f"Year_{year}.db")
        curs = con.cursor()
        query2 = f"SELECT * FROM Customers_{year}"
        curs.execute(query2)
        cus = curs.fetchall()
        # print(cus)
        for a in customer_tree.get_children():
            customer_tree.delete(a)
            pass

        for cust in cus:
            customer_tree.insert("", 'end', values=cust)

    def logout():
        response = mg.askyesno("LOGOUT", "Are You Sure you want to logout?")
        if response == 1:
            cashier.withdraw()
            root.deiconify()
        else:
            pass

    def prints():
        global receipts
        try:
            q = receipts.get(1.0, END)
            if (q == ""):
                mg.showinfo("Message", "Nothing to Print")
            else:
                filename = tempfile.mktemp(".txt")
                open(filename, "w").write(q)
                os.startfile(filename, "print")

                os.startfile(filename, "print")

                receipts.delete(1.0, END)

                # print_button = ttk.Button(cashier, text="PRINT", state=DISABLED).place(x=750, y=400)

                # submit = ttk.Button(cashier, text="SUBMIT", state=DISABLED).place(x=400, y=405)
                resets()
                # std_list()
        except:
            mg.showinfo("Message", "Nothing to Print")

    def exp_insert():
        top = Toplevel()
        top.minsize(400, 160)
        top.resizable(0, 0)
        top.iconbitmap("md.ico")
        top.title("EXPENSES")
        # expframe = LabelFrame(top, text="Expenses", bg="#FBFADD",
        #                       font=("tahoma", 15, "bold"), fg="blue", borderwidth='4',
        #                       relief=GROOVE, height=130, width=240)
        # expframe.place(x=500, y=325)

        dated = d.datetime.today()
        table_name = dated.date()
        total = amount

        year = table_name.year
        month = table_name.strftime("%B")
        day = table_name.day

        Daily = f"{str(day)}_{str(month)}_{str(year)}"

        def month_exps():
            description = des_entry.get().upper()
            am = exp_amount_entry.get()
            con = sqlite3.connect(f"Year_{year}.db")
            cursor = con.cursor()
            if (description == "" or am == ""):
                pass
                # mg.showinfo("Message", "All Fields are Required")
            else:
                insert = f"INSERT INTO Expense_{month} VALUES('" + description + "', '" + am + "')"
                if (cursor.execute(insert)):
                    cursor.execute('commit')
                # print("Successful")
            con.close()

        def exps():
            description = des_entry.get().upper()
            am = exp_amount_entry.get()
            conn = sqlite3.connect(f"Store_{month}_{year}.db")
            cursor = conn.cursor()

            if(description=="" or am==""):
                mg.showinfo("Message", "All Fields are Required")
            else:
                insert = f"INSERT INTO exp_{Daily} VALUES('" + description + "', '" + am + "')"
                if (cursor.execute(insert)):
                    cursor.execute('commit')

            today_exps()
            month_exps()
            fill_exp()

            des_entry.delete(0, END)
            exp_amount_entry.delete(0, END)

            conn.close()

        des = Label(top, text="Description: ", fg="#315C3B",
                    font=("arial", 15, "bold")).place(x=5, y=10)
        des_entry = Entry(top,
                          font=("arial", 13, "bold"), bg="#DDF0ED")
        des_entry.place(x=150, y=16)

        exp_amount_entry = Entry(top, fg="#315C3B",
                                 font=("arial", 13, "bold"), bg="#DDF0ED")
        exp_amount_entry.place(x=150, y=45)

        exp_submit = ttk.Button(top, text="Submit", command=exps).place(x=70, y=100)

        exp_amount = Label(top, text="Amount: ", fg="#315C3B",
                           font=("arial", 15, "bold")).place(x=5, y=42)

    def today_exps():
        dated = d.datetime.today()
        table_name = dated.date()
        total = amount

        year = table_name.year
        month = table_name.strftime("%B")
        day = table_name.day

        Daily = f"{str(day)}_{str(month)}_{str(year)}"
        conn = sqlite3.connect(f"Store_{month}_{year}.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM exp_{Daily}")
        rows = cursor.fetchall()

        for b in today_exp_view.get_children():
            today_exp_view.delete(b)

        t = []

        for row in rows:
            t.append(row[1])
            today_exp_view.insert("", 'end', values=row)

        global todays_expens
        todays_expens = 0
        for ii in t:
            todays_expens += int(ii)
        # print(todays_expens)

    def fill_exp():
        try:
            global expenses_
            dated = d.datetime.today()
            table_name = dated.date()
            total = amount

            year = table_name.year
            month = table_name.strftime("%B")
            conn = sqlite3.connect(f"Year_{year}.db")
            cursor = conn.cursor()

            check = f"SELECT * FROM Expense_{month}"
            cursor.execute(check)
            rows = cursor.fetchall()

            for v in exp_month.get_children():
                exp_month.delete(v)
                pass

            tot_exp = []

            for row in rows:
                tot_exp.append(row[1])
                exp_month.insert("", 'end', values=row)

            exp_total = 0
            for t in tot_exp:
                exp_total += t
                expenses_ = exp_total

            total_exp = Label(monthframe, text=f"Total Exp.: N{exp_total}", fg="#315C3B",
                              font=("arial", 15, "bold")).place(x=320, y=260)

            yearly_data()
            yearly_sales()
        except:
            pass

    def monthly_data():
        # databases()
        try:
            global monthly_total
            global monthly_kg
            dated = d.datetime.today()
            table_name = dated.date()

            year = table_name.year
            month = table_name.strftime("%B")
            day = table_name.strftime("%d %b")

            con = sqlite3.connect(f'Year_{year}.db')
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM Sales_{month}")
            data = cursor.fetchall()
            # print(con)
            # print(monthly_kg, monthly_total)
            # # print(data)
            for datum in data:
                # print(monthly_kg, monthly_total)
                if datum[0] == str(day):
                    # print(datum[0])
                    if (cursor.execute(
                            f"UPDATE Sales_{month} SET Total_Kg='" + str(float(monthly_kg)) + "', Total_Amount='" + str(float(monthly_total)) + "' WHERE Date='" + str(day) + "'")):
                        cursor.execute('commit')
                        # print("Successfully")
                        break
                    else:
                        print("Not Successful")

            else:
                fill = f"INSERT INTO Sales_{month} VALUES('" + str(day) + "', '" + str(float(monthly_kg)) + "', '" + str(float(monthly_total)) + "')"
                if (cursor.execute(fill)):
                    cursor.execute('commit')
                    # print("Successfully")
                else:
                    print("Not Successful")
        except:
            pass

        # Daily = f"{str(day)}/{str(month)}_{str(year)}"
        # Sales_{month}

    # total_monthly_kg = 0
    # total_monthly_sales = 0

    def monthly_sales():
        try:
            global total_monthly_kg
            global total_monthly_sales

            dated = d.datetime.today()
            table_name = dated.date()

            year = table_name.year
            month = table_name.strftime("%B")
            day = table_name.strftime("%d %b")

            con = sqlite3.connect(f'Year_{year}.db')
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM Sales_{month}")
            data = cursor.fetchall()

            for dd in total_sales_month.get_children():
                total_sales_month.delete(dd)
                pass
            kgs = []
            totas = []
            for rows in data:
                kgs.append(rows[1])
                totas.append(rows[2])
                total_sales_month.insert("", 'end', values=rows)

            mm = 0
            for m in kgs:
                mm += float(m)
                total_monthly_kg = mm

            oo = 0
            for o in totas:
                oo += float(o)
                total_monthly_sales = oo

            fill_exp()
            yearly_data()
        except:
            pass
        # global total_monthly_sales, total_monthly_kg

        # print(total_monthly_kg, total_monthly_sales)
        # print

    def yearly_data():
        global total_monthly_kg
        global total_monthly_sales
        global expenses_

        try:
            global monthly_total
            global monthly_kg
            dated = d.datetime.today()
            table_name = dated.date()

            year = table_name.year
            month = table_name.strftime("%B")
            day = table_name.strftime("%d %b")

            con = sqlite3.connect(f'Year_{year}.db')
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM Trans_{year}")
            data = cursor.fetchall()
            # print(con)
            # print(monthly_kg, monthly_total)
            # # print(data)
            for datum in data:
                # print(monthly_kg, monthly_total)
                if datum[0] == str(month):
                    # print(datum[0])
                    if (cursor.execute(
                            f"UPDATE Trans_{year} SET Total_Kg='" + str(float(total_monthly_kg)) + "', Total_Exp='" + str(float(expenses_)) + "', Total_Amount='" + str(float(total_monthly_sales)) + "' WHERE Month='" + str(month) + "'")):
                        cursor.execute('commit')
                        # print("Successfully")
                        break
                    else:
                        print("Not Successful")

            else:
                fill = f"INSERT INTO Trans_{year} VALUES('" + str(month) + "', '" + str(float(
                    total_monthly_kg)) + "', '" + str(float(expenses_)) + "', '" + str(float(total_monthly_sales)) + "')"
                if (cursor.execute(fill)):
                    cursor.execute('commit')
                    # print("Successfully")
                else:
                    print("Not Successful")
        except:
            # global total_monthly_kg
            # global total_monthly_sales
            try:
                expenses_ = 0
                dated = d.datetime.today()
                table_name = dated.date()

                year = table_name.year
                month = table_name.strftime("%B")
                day = table_name.strftime("%d %b")

                con = sqlite3.connect(f'Year_{year}.db')
                cursor = con.cursor()
                cursor.execute(f"SELECT * FROM Trans_{year}")
                data = cursor.fetchall()
                # print(con)
                # print(monthly_kg, monthly_total)
                # # print(data)
                for datum in data:
                    # print(monthly_kg, monthly_total)
                    if datum[0] == str(month):
                        # print(datum[0])
                        if (cursor.execute(
                                f"UPDATE Trans_{year} SET Total_Kg='" + str(float(total_monthly_kg)) + "', Total_Exp='" + str(
                                    float(expenses_)) + "', Total_Amount='" + str(float(
                                    total_monthly_sales)) + "' WHERE Month='" + str(month) + "'")):
                            cursor.execute('commit')
                            # print("Successfully")
                            break
                        else:
                            print("Not Successful")

                else:
                    fill = f"INSERT INTO Trans_{year} VALUES('" + str(month) + "', '" + str(float(
                        total_monthly_kg)) + "', '" + str(float(expenses_)) + "', '" + str(float(total_monthly_sales)) + "')"
                    if (cursor.execute(fill)):
                        cursor.execute('commit')
                        print("Successfully")
                    else:
                        print("Not Successful")
            except:
                pass

    # yearly_data()

    def yearly_sales():
        dated = d.datetime.today()
        table_name = dated.date()

        year = table_name.year
        month = table_name.strftime("%B")
        day = table_name.strftime("%d %b")

        con = sqlite3.connect(f'Year_{year}.db')
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM Trans_{year}")
        datum = cursor.fetchall()

        for w in total_sales_year.get_children():
            total_sales_year.delete(w)
            pass

        for z in datum:
            total_sales_year.insert("", 'end', values=z)

    submenu = Menu(menubar, tearoff=False, bg="#FBFADD", fg="#315C3B",
                   font=("arial", 12))
    menubar.add_cascade(label="FILE", menu=submenu)
    submenu.add_command(label="Insert Expenses", command=exp_insert)
    submenu.add_command(label="Exit", command=logout)

    # submenu = Menu(menubar, tearoff=False, bg="#FBFADD", fg="red",
    #                font=("tahoma", 12, "bold"))
    # menubar.add_cascade(label="CALCULATOR", menu=submenu)
    # submenu.add_command(label="Calculator", command=calculator)

    bus_name = Label(cashier, text="MARY DANIELLA GAS", bg="#FBFADD", fg="red",
                     font=("tahoma", 35, "bold"), pady=5).place(x=30, y=10)

    leftframe = LabelFrame(cashier, text="DATA ENTRY", bg="#FBFADD",
                           font=("tahoma", 20, "bold"), fg="green", borderwidth='2',
                           relief=GROOVE, height=360, width=470)
    leftframe.place(x=15, y=85)

    # CUSTOMER'S DATA
    # entry = ttk.Entry(leftframe, width=30, font=("tahoma", 8, "bold"))
    # entry.place(x=12, y=20)

    customer_name = Label(leftframe, text="CUST.'S NAME: ", bg="#FBFADD", fg="#315C3B",
                          font=("verdana", 12, "bold")).place(x=15, y=15)
    customer_entry = Entry(leftframe,
                           font=("arial", 12, "bold"), bg="#DDF0ED")
    customer_entry.place(x=210, y=16)

    phone_number = Label(leftframe, text="PHONE NO.: ", bg="#FBFADD", fg="#315C3B",
                         font=("verdana", 12, "bold")).place(x=15, y=60)
    phone_entry = Entry(leftframe, fg="#315C3B",
                        font=("arial", 12, "bold"), bg="#DDF0ED")
    phone_entry.place(x=210, y=61)

    kg_label = Label(leftframe, text="NUMBER OF KG: ", bg="#FBFADD", fg="#315C3B",
                     font=("verdana", 12, "bold")).place(x=15, y=105)
    kg_entry = Entry(leftframe, fg="#315C3B",
                     font=("arial", 12, "bold"), bg="#DDF0ED")
    kg_entry.place(x=210, y=106)

    product = Label(leftframe, text="PRODUCT: ", bg="#FBFADD", fg="#315C3B",
                    font=("arial", 12, "bold")).place(x=15, y=145)
    # global cyl_gas
    cyl_gas = StringVar()
    cyl_gas.set("gas")

    Radiobutton(leftframe, text="Gas", font=("verdana", 12, "bold"), bg="#FBFADD",
                variable=cyl_gas, value="gas").place(x=210, y=144)
    Radiobutton(leftframe, text="Cylinder", font=("verdana", 12, "bold"), bg="#FBFADD",
                variable=cyl_gas, value="cylinder").place(x=290, y=144)

    total_value = Label(leftframe, text="TOTAL: ", bg="#FBFADD", fg="#315C3B",
                        font=("verdana", 12, "bold")).place(x=15, y=183)
    total_entry = Entry(leftframe, fg="red", width=10,
                        font=("arial", 12, "bold"), bg="#DDF0ED")
    total_entry.place(x=210, y=183)

    amount = Label(leftframe, text="AMO.IN WORDS: ", bg="#FBFADD", fg="#315C3B",
                   font=("verdana", 12, "bold")).place(x=15, y=227)

    amount_in_words = Text(leftframe, width=20, font=("verdana", 12, "bold"), bg="#DDF0ED",
                           height=3, fg="#315C3B")
    amount_in_words.place(x=210, y=223)

    sales = Label(cashier, text="RECEIPT", bg="#FBFADD", fg="#315C3B",
                  font=("tahoma", 12, "bold")).place(x=600, y=65)

    # receipt = Text(cashier, width=30, bg="#EFF4F8",
    #                height=18, state=DISABLED, fg="#315C3B")
    # receipt.place(x=500, y=100)

    total = ttk.Button(cashier, text="TOTAL", command=totals).place(x=200, y=405)

    reset = ttk.Button(cashier, text="RESET", command=resets).place(x=60, y=405)

    submit = ttk.Button(cashier, text="SUBMIT", state=DISABLED).place(x=340, y=405)

    treeview = ttk.Treeview(cashier, height=9, columns=(1, 2, 3, 4, 5, 6), show="headings")
    treeview.place(x=10, y=450)

    treeview.column("1", width=150, anchor=W)
    treeview.column("2", width=100, anchor=W)
    treeview.column("3", width=50, anchor=S)
    treeview.column("4", width=50, anchor=S)
    treeview.column("5", width=80, anchor=S)
    treeview.column("6", width=150, anchor=W)

    treeview.heading("1", text="NAMES", anchor=S)
    treeview.heading("2", text="PHONE NO", anchor=S)
    treeview.heading("3", text="KGS", anchor=S)
    treeview.heading("4", text="PRODUCT", anchor=S)
    treeview.heading("5", text="AMOUNT", anchor=S)
    treeview.heading("6", text="AMOUNT IN WORDS", anchor=S)

    """TODAY EXPENSES"""
    today_exp = Label(cashier, text="TODAY EXPENSES", bg="#FBFADD", fg="#315C3B",
                      font=("verdana", 10, "bold")).place(x=600, y=490)

    today_exp_view = ttk.Treeview(cashier, columns=(1, 2), height=6, show="headings")
    today_exp_view.place(x=600, y=510)

    today_exp_view.column("1", width=100)
    today_exp_view.column("2", width=50, anchor=S)

    today_exp_view.heading("1", text="Desc.", anchor=S)
    today_exp_view.heading("2", text="Amo.", anchor=S)

    """MONTHLY"""

    monthframe = LabelFrame(cashier, text=f"MONTH OF {month}",
                            font=("tahoma", 15, "bold"), fg="blue", borderwidth='2',
                            relief=GROOVE, height=320, width=550)
    monthframe.place(x=770, y=5)

    total_sale_month = Label(monthframe, text="Total Sales of the Month", fg="#315C3B",
                             font=("verdana", 15, "bold")).place(x=5, y=2)

    total_sales_month = ttk.Treeview(monthframe, columns=(1, 2, 3), height=10, show="headings")
    total_sales_month.place(x=10, y=30)

    total_sales_month.column("1", width=100, anchor=S)
    total_sales_month.column("2", width=80, anchor=S)
    total_sales_month.column("3", width=80, anchor=S)

    total_sales_month.heading("1", text="Date", anchor=S)
    total_sales_month.heading("2", text="Total Kg", anchor=S)
    total_sales_month.heading("3", text="Total", anchor=S)

    total_kg = Label(monthframe, text=f"Total Kg:", fg="#315C3B",
                     font=("arial", 15, "bold")).place(x=2, y=260)

    month_total_amount = Label(monthframe, text=f"Total:N", fg="#315C3B",
                               font=("arial", 15, "bold")).place(x=135, y=260)

    """Expenses"""
    total_month_expenses = Label(monthframe, text="All the Month Expenses", fg="#315C3B",
                                 font=("verdana", 15, "bold")).place(x=320, y=2)

    exp_month = ttk.Treeview(monthframe, columns=(1, 2), height=10, show="headings")
    exp_month.place(x=315, y=30)

    exp_month.column("1", width=140)
    exp_month.column("2", width=80, anchor=S)
    # total_sales_month.column("3", width=80)

    exp_month.heading("1", text="Desc.", anchor=S)
    exp_month.heading("2", text="Amount", anchor=S)
    # total_sales_month.heading("3", text="Total", anchor=S)

    total_exp = Label(monthframe, text=f"Total Exp.:", fg="#315C3B",
                      font=("arial", 15, "bold")).place(x=320, y=260)

    """END MONTHLY"""

    """YEARLY"""

    yearframe = LabelFrame(cashier, text=f"YEAR - {year}", bg="#E3B7D5",
                           font=("tahoma", 15, "bold"), fg="#B3539E", borderwidth='2',
                           relief=GROOVE, height=320, width=550)
    yearframe.place(x=770, y=330)

    total_sale_year = Label(yearframe, text="Sales & Expenses", bg="#E3B7D5", fg="#315C3B",
                            font=("verdana", 15, "bold")).place(x=5, y=2)

    total_sales_year = ttk.Treeview(yearframe, columns=(1, 2, 3, 4), height=10, show="headings")
    total_sales_year.place(x=5, y=30)

    total_sales_year.column("1", width=90)
    total_sales_year.column("2", width=50, anchor=S)
    total_sales_year.column("3", width=50, anchor=S)
    total_sales_year.column("4", width=70, anchor=S)

    total_sales_year.heading("1", text="Month", anchor=S)
    total_sales_year.heading("2", text="Kg", anchor=S)
    total_sales_year.heading("3", text="Exp.", anchor=S)
    total_sales_year.heading("4", text="Total", anchor=S)

    """customers"""
    customer = Label(yearframe, text="All Customers", bg="#E3B7D5", fg="red",
                     font=("verdana", 15, "bold")).place(x=320, y=2)

    customer_tree = ttk.Treeview(yearframe, columns=(1, 2), height=10, show="headings")
    customer_tree.place(x=290, y=30)

    customer_tree.column("1", width=160)
    customer_tree.column("2", width=80, anchor=S)
    # total_sales_month.column("3", width=80)

    customer_tree.heading("1", text="Customers", anchor=S)
    customer_tree.heading("2", text="Kg", anchor=S)
    # total_sales_month.heading("3", text="Total", anchor=S)

    """END YEARLY"""

    loging = ttk.Button(cashier, text="LOGOUT", command=logout).place(x=1200, y=653)

    # sep_image = PhotoImage(file="separator.png")
    # separator = Label(cashier, image=sep_image).place(x=756)
    #
    # month_separator = Label(monthframe, image=sep_image).place(x=300)
    #
    # year_separator = Label(yearframe, image=sep_image).place(x=275)

    # databases()
    std_list()
    today_exps()
    monthly_sales()
    monthly_data()
    yearly_sales()
    customer_record()
    fill_exp()


def admin_dashboard():
    root.withdraw()
    from tkinter import ttk, messagebox as mg
    from ttkthemes import themed_tk as tk
    import sqlite3
    import _datetime as d
    import os
    import tempfile

    admin_page = tk.ThemedTk()
    admin_page.get_themes()
    admin_page.set_theme("radiance")
    admin_page.configure(bg="#DEEFF5")
    # root.attributes("-fullscreen", True)
    admin_page.geometry("1350x750+0+0")
    # admin_page.resizable(0, 0)
    admin_page.title("MARY DANIELLA RECOREDS")
    admin_page.iconbitmap("md.ico")

    index = 0

    def std_list():
        try:
            global index
            dated = d.datetime.today()
            table_name = dated.date()

            year = table_name.year
            month = table_name.strftime("%B")
            day = table_name.day

            Daily = f"{str(day)}_{str(month)}_{str(year)}"

            con = sqlite3.connect(f"Store_{month}_{year}.db")
            cursor = con.cursor()
            query = f"SELECT * FROM today_{Daily}"
            cursor.execute(query)
            rows = cursor.fetchall()
            listbox.delete(0, listbox.size())

            insData = f"           NAME                     PHONE NUMBER         NO. OF KG           PRODUCT          TOTAL(N)            AMOUNT IN WORDS    "
            listbox.insert(0, insData)
            val = []
            for row in rows:
                val.append(row[4])
                insertData = f"{index}    {row[0]}    {row[1]}               {row[2]}                     {row[3]}                    {row[4]}                 {row[5]}"
                listbox.insert(listbox.size() + 1, insertData)
                index += 1
            total = 0
            for x in val:
                total += x

            total_label = Label(admin_page, text=f"TODAY'S TOTAL SALES: N{total}", bg="#DEEFF5", fg="black",
                                font=("verdana", 12, "bold")).place(x=1000, y=400)

            # print(total)
        except:
            total = 0

    def logout():
        response = mg.askyesno("LOGOUT", "Are You Sure you want to logout?")
        if response == 1:
            admin_page.withdraw()
            root.deiconify()
        else:
            pass

    def create_account():
        try:
            username = username_entry.get()
            password = password_entry.get()

            if (username == "" or password == ""):
                mg.showinfo("Message", "All fields are required")
            else:
                con = sqlite3.connect("Mary_Daniella.db")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM Staff")
                rows = cursor.fetchall()

                users = []

                for row in rows:
                    users.append(row[0])
                    if (row[0] == username):
                        mg.showinfo("Message", "Username has been used")
                        break
                else:
                    if (cursor.execute("INSERT INTO Staff VALUES('" + username + "', '" + password + "')")):
                        cursor.execute('commit')
                        mg.showinfo("Message", "Account Created Successfully")

                        username_entry.delete(0, END)
                        password_entry.delete(0, END)
                # print(users)
        except:
            mg.showinfo("Message", "Not Account Created Successfully")

    def delete_account():
        try:
            con = sqlite3.connect('Mary_Daniella.db')
            cursor = con.cursor()
            username = username_entry.get()

            if (username == ""):
                mg.showinfo("Message", "The First Name is needed")
            else:
                cursor.execute("SELECT * FROM Staff")
                rows = cursor.fetchall()

                users = []

                for row in rows:
                    users.append(row[0])
                    pass

                for x in users:
                    if x == username:
                        cursor.execute("DELETE FROM Staff WHERE username='" + username + "'")
                        cursor.execute('commit')
                        mg.showinfo("Message", "Deleted Successfully")
                        username_entry.delete(0, END)
                        break

            con.close()

            # cursor.execute('commit')
        except:
            mg.showinfo("Message", "Not Deleted Successful")

    def Kg_Amount():
        try:
            con = sqlite3.connect('Mary_Daniella.db')
            cursor = con.cursor()
            amounts = amount_entry.get()
            done = int(amounts)
            types = isinstance(done, int)
            # print(types)
            if types == True:
                if (amounts == ""):
                    mg.showinfo("Message", "The Amount Field is Needed")
                else:
                    cursor.execute("SELECT * FROM Kg_amount")
                    rows = cursor.fetchall()

                    users = []

                    for row in rows:
                        if row[0] == "kg_amount":
                            p = row[1]
                            # print(p)
                            cursor.execute("UPDATE Kg_amount SET amount='" + amounts + "' WHERE price='kg_amount'")
                            done = cursor.execute('commit')
                            if done:
                                mg.showinfo("Message", "Amount Changed Successfully")
                                amount_entry.delete(0, END)
                    # break
            else:
                mg.showinfo("Message", "Only Number is allowed")
        except:
            mg.showinfo("Message", "Amount Not Changed Successfully")


    bus_name = Label(admin_page, text="MARY DANIELLA GAS - Admin Dashboard", bg="#DEEFF5", fg="red",
                     font=("tahoma", 35, "bold"), pady=10).place(x=30, y=20)
    # /************************** CREATING ACCOUNT******************************************
    leftframe = LabelFrame(admin_page, text="Create Cashier Account", bg="white",
                           font=("tahoma", 20, "bold"), fg="green", borderwidth='2',
                           relief=GROOVE, height=150, width=390)
    leftframe.place(x=15, y=120)

    username_name = Label(leftframe, text="Username: ", bg="white", fg="#315C3B",
                          font=("verdana", 12, "bold")).place(x=15, y=15)
    username_entry = Entry(leftframe, fg="#315C3B",
                           font=("verdana", 12, "bold"), bg="#DEEFF5")
    username_entry.place(x=140, y=16)

    password = Label(leftframe, text="Password: ", bg="white", fg="#315C3B",
                     font=("verdana", 12, "bold")).place(x=15, y=45)
    password_entry = Entry(leftframe, fg="#315C3B",
                           font=("verdana", 12, "bold"), bg="#DEEFF5")
    password_entry.place(x=140, y=46)

    dele = ttk.Button(leftframe, text="DELETE", command=delete_account).place(x=100, y=76)

    create = ttk.Button(leftframe, text="CREATE", command=create_account).place(x=250, y=76)

    # /************************** CREATING ACCOUNT******************************************

    # /************************** CHANGING KG AMOUNT ******************************************

    nextframe = LabelFrame(admin_page, text="Changing Kg Amount & Queuing Expenses", bg="white",
                           font=("tahoma", 10, "bold"), fg="green", borderwidth='2',
                           relief=SUNKEN, height=150, width=300)
    nextframe.place(x=420, y=120)

    # CUSTOMER'S DATA
    # entry = ttk.Entry(leftframe, width=30, font=("tahoma", 8, "bold"))
    # entry.place(x=12, y=20)

    expense = Label(nextframe, text="EXPENSES: ", bg="white", fg="#315C3B",
                    font=("verdana", 12, "bold")).place(x=15, y=15)
    expense_entry = Entry(nextframe, fg="#315C3B", width=9,
                          font=("verdana", 12, "bold"), bg="#E3EFCE")
    expense_entry.place(x=15, y=45)

    amount = Label(nextframe, text="AMOUNT: ", bg="white", fg="#374899",
                   font=("verdana", 12, "bold")).place(x=180, y=16)
    amount_entry = Entry(nextframe, fg="#315C3B", width=8,
                         font=("verdana", 12, "bold"), bg="#F6E29B")
    amount_entry.place(x=180, y=46)

    exp = ttk.Button(nextframe, text="EXPENSE").place(x=10, y=76)

    loging = ttk.Button(admin_page, text="LOGOUT", command=logout).place(x=1200, y=40)


    change = ttk.Button(nextframe, text="CHANGE", command=Kg_Amount).place(x=160, y=76)

    # /************************** CHANGING KG AMOUNT******************************************

    listbox = Listbox(admin_page, width=150, height=11, font=("verdana", 9))
    listbox.place(x=10, y=460)
    # listbox.insert(0, "Paulinus")

    std_list()


main()

root.mainloop()
