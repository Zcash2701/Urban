import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
import def_for_unloading as du
import openpyxl as op
from openpyxl.styles import PatternFill
from datetime import datetime

filename = ''
select_action = ['Выгрузка по НГЧ', 'Выгрузка по температурам', 'Выгрузка Бексаово, НГЧ14']

"""
9 ЧекБоксов (9 НГЧ)

1) Выделение температур
2) Выгрузка по НГЧ (чекбоксы)
3) Выгрузка Бекасово, НГЧ14

"""
def open_file():

    global filename
    filename = str(fd.askopenfilenames())
    filename = filename.replace('/', '//').replace('(', '').replace(')', '').replace("'", '').replace(",", '')
    #print((filename))
    answer_file_name_entry.insert(0, filename)
    return





window = tk.Tk()
window.title('Сплав В.')
window.geometry('500x300')
window.resizable(False, False)

button_add_file = tk.Button(text='Выбрать файл', command=open_file, height=1)
button_add_file.place(x=25, y=50)

label_file_name = tk.Label(text="Выбранный файл: ", height=2)
label_file_name.place(x=130, y=25)
answer_file_name_entry = tk.Entry(width=50)
answer_file_name_entry.place(x=130, y=50)


# Выбор действия. Выгрузка:
# 1) по t
# 2) НГЧ (чекбоксы)
# 3) Бекасово, нгч14


combox = ttk.Combobox(values=select_action, width=25)
combox.current(0)
combox.place(x=25, y=85)


def interface_for_temperature():
    global filename

    # Лабель и ввод минимальных помещение
    label_get_min_tem_pom = tk.Label(text='Min t пом.: ')
    label_get_min_tem_pom.place(x=25, y=130)
    entry_min_temp_pom = tk.Entry(width=15)
    entry_min_temp_pom.place(x=130, y=130)
    entry_min_temp_pom.insert(0, '15')

    # Лабель и ввод максимальных помещение
    label_get_max_tem_pom = tk.Label(text='Max t пом.: ')
    label_get_max_tem_pom.place(x=25, y=155)
    entry_max_temp_pom = tk.Entry(width=15)
    entry_max_temp_pom.place(x=130, y=155)
    entry_max_temp_pom.insert(0, '20')

    label_get_min_temp_cont = tk.Label(text='Min t контура: ')
    label_get_min_temp_cont.place(x=250, y=130)
    entry_min_temp_cont = tk.Entry(width=15)
    entry_min_temp_cont.place(x=340, y=130)
    entry_min_temp_cont.insert(0, '20')

    ## Лабель и ввод максимальных контур
    label_get_max_temp_cont = tk.Label(text='Max t контура: ')
    label_get_max_temp_cont.place(x=250, y=155)
    entry_max_temp_cont = tk.Entry(width=15)
    entry_max_temp_cont.place(x=340, y=155)
    entry_max_temp_cont.insert(0, '25')

    entry_ready_answer = tk.Entry(width=30)
    entry_ready_answer.place(x=150, y=250)

    min_pom = int(entry_min_temp_pom.get())
    max_pom = int(entry_max_temp_pom.get())
    min_cont = int(entry_min_temp_cont.get())
    max_cont = int(entry_max_temp_cont.get())

    list_info_temperature = (min_pom, max_pom, min_cont, max_cont)
    return list_info_temperature







def unloading_for_NG4():
    pass

def get_interface():
    if combox.get() == select_action[1]:
        interface_for_temperature()

        answer_name = du.by_temperature(filename,
                                        min_pom,
                                        max_pom,
                                        min_cont,
                                        max_cont)
        entry_ready_answer.insert(0, f'{answer_name} готова')

    elif combox.get() == select_action[0]:
        pass





button_select_action = ttk.Button(text='Выбрать', command=lets_work).place(x=250, y=85)



do_it_button = tk.Button(text='Выполнить', command=unloading_by_temperature)
do_it_button.place(x=25, y=250)


window.mainloop()