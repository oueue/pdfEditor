import PyPDF2
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import filedialog
from tkinter import END

#global variables
file_list = []
pdfWriter = PyPDF2.PdfFileWriter()

#functions
def import_file():
    global file_list, scr
    tmp = filedialog.askopenfilenames(filetypes = [("PDF", ".pdf")])
    for i in tmp:
        if i not in file_list:
            file_list.append(i)
    scr.delete('1.0', END)
    print(file_list)
    for i in file_list:
        scr.insert('1.0', i)
        scr.insert('1.0', "\n")

def output_file():
    save_file = filedialog.asksaveasfile(initialfile = 'merge.pdf', mode = 'wb')
    pdfWriter.write(save_file)
    save_file.close()

def merge():
    global file_list
    win1 = tk.Tk()
    tk.Label(win1, text = "合并中......请等待")
    for pdf in file_list:
        pdfFileObj = open(pdf, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for pageNum in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    win1.destroy()

#frame
win = tk.Tk()
win.geometry("580x300")
frame = ttk.LabelFrame(win, text = '要拼合的pdf文件')
frame.grid(column = 0, row = 7)

scrol_w = 50
scrol_h = 15
scr = scrolledtext.ScrolledText(win, width = scrol_w, height = scrol_h, wrap = tk.WORD)
scr.grid(column = 0, columnspan = 5, sticky = tk.W, padx = 20)

button2 = tk.Button(win, text = "合并pdf文件", command = merge)
button2.grid(column = 0, row = 5)

ttk.Label(frame, text = "                          -----文件名-----          ").grid(column = 0, row = 0, sticky = tk.W,padx = 25)
ttk.Label(frame, text = "                           -----顺序----- ").grid(column = 1, row = 0, sticky = tk.W)
ttk.Label(frame, text = "   -----删除-----  ").grid(column = 2, row = 0, sticky = tk.W)
win.resizable(False,False)


menu_bar = Menu(win)
win.config(menu = menu_bar)
file_menu = Menu(menu_bar, tearoff = 0)
file_menu.add_command(label = "导入", command = import_file)
file_menu.add_command(label = "导出", command = output_file)
menu_bar.add_cascade(label = "文件", menu = file_menu)


win.mainloop()
