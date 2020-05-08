import tkinter as tk


class BookStoreUI:
    def __init__(self, service):
        self.window = tk.Tk()
        self.window.wm_title('BookStore')

        self.lst_result = None
        self.selected_index = -1
        self.selected_record = None

        self.var_title = tk.StringVar()
        self.var_author = tk.StringVar()
        self.var_year = tk.StringVar()
        self.var_isbn = tk.StringVar()

        self.service = service

        self.__init_ui__()
        self.action_btn_view()

    def __init_ui__(self):
        lbl_title = tk.Label(self.window, text="Title")
        lbl_author = tk.Label(self.window, text="Author")
        lbl_year = tk.Label(self.window, text="Year")
        lbl_isbn = tk.Label(self.window, text="ISBN")

        txt_title = tk.Entry(self.window, textvariable=self.var_title, width=80)
        txt_author = tk.Entry(self.window, textvariable=self.var_author, width=80)
        txt_year = tk.Entry(self.window, textvariable=self.var_year, width=80)
        txt_isbn = tk.Entry(self.window, textvariable=self.var_isbn, width=80)

        self.lst_result = tk.Listbox(self.window, width=200, height=40)
        lst_scroll = tk.Scrollbar(self.window)
        self.lst_result.config(yscrollcommand=lst_scroll.set)
        lst_scroll.config(command=self.lst_result.yview)
        self.lst_result.bind('<<ListboxSelect>>', self.action_lst_view)

        btn_view = tk.Button(self.window, text="View", width=20, command=self.action_btn_view)
        btn_search = tk.Button(self.window, text="Search", width=20, command=self.action_btn_search)
        btn_add = tk.Button(self.window, text="Add", width=20, command=self.action_btn_add)
        btn_update = tk.Button(self.window, text="Update", width=20, command=self.action_btn_update)
        btn_delete = tk.Button(self.window, text="Delete", width=20, command=self.action_btn_delete)
        btn_close = tk.Button(self.window, text="Close", width=20, command=self.action_btn_close)

        lbl_title.grid(row=0, column=0)
        txt_title.grid(row=0, column=1)
        lbl_author.grid(row=0, column=2)
        txt_author.grid(row=0, column=3)

        lbl_year.grid(row=1, column=0)
        txt_year.grid(row=1, column=1)
        lbl_isbn.grid(row=1, column=2)
        txt_isbn.grid(row=1, column=3)

        self.lst_result.grid(row=2, column=0, rowspan=18, columnspan=4)
        lst_scroll.grid(row=2, column=4, rowspan=6)

        btn_view.grid(row=2, column=5)
        btn_search.grid(row=3, column=5)
        btn_add.grid(row=4, column=5)
        btn_update.grid(row=5, column=5)
        btn_delete.grid(row=6, column=5)
        btn_close.grid(row=7, column=5)

    def show_ui(self):
        self.window.mainloop()

    def action_btn_view(self):
        self.lst_result.delete(0, tk.END)
        for (idx, record) in enumerate(self.service.view_data()):
            self.lst_result.insert(idx, record)

    def action_btn_search(self):
        self.lst_result.delete(0, tk.END)
        for (idx, record) in enumerate(self.service.search_data(self.var_title.get(), self.var_author.get(),
                                                                self.var_year.get(), self.var_isbn.get())):
            self.lst_result.insert(idx, record)

    def action_btn_add(self):
        self.service.insert_data(self.var_title.get(), self.var_author.get(), self.var_year.get(), self.var_isbn.get())
        self.action_btn_view()

    def action_btn_update(self):
        record_id = self.selected_record[0]
        self.service.update_data(record_id, self.var_title.get(), self.var_author.get(), self.var_year.get(), self.var_isbn.get())
        self.action_btn_view()

    def action_btn_delete(self):
        record_id = self.selected_record[0]
        self.service.delete_data(record_id)
        self.action_btn_view()

    def action_btn_close(self):
        self.window.destroy()

    def action_lst_view(self, event):
        if self.lst_result.curselection():
            self.selected_index = self.lst_result.curselection()[0]
            self.selected_record = self.lst_result.get(self.selected_index)

            self.var_title.set(self.selected_record[1])
            self.var_author.set(self.selected_record[2])
            self.var_year.set(self.selected_record[3])
            self.var_isbn.set(self.selected_record[4])
        else:
            self.selected_index = -1
            self.selected_record = None

            self.var_title.set('')
            self.var_author.set('')
            self.var_year.set('')
            self.var_isbn.set('')

