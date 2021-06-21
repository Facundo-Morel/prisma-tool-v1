# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='MLA - Prisma', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getCSV ():
    global read_file
    
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_csv (import_file_path)
    read_file['liq_importe'].replace('.', ',')
    read_file['liq_importe'].replace('-', '')
    read_file['liq_ticket'].replace('.0', '')
    read_file['liq_fecha_liquidacion'] = pd.to_datetime(read_file['liq_fecha_liquidacion']).dt.date
    read_file['P6'] = read_file['liq_nro_tarjeta'].str[:6]
    read_file['U4'] = read_file['liq_nro_tarjeta'].str[-4:]
    read_file['PAY_PAYMENT_ID'] = ""
    read_file['GTWT_OPERATION'] = ""
    read_file['GTWT_STATUS'] = ""
    read_file['PAY_STATUS_ID'] = ""
    read_file['PAY_STATUS_DETAIL_CODE'] = ""
    read_file['GTWT_AMOUNT'] = ""
    read_file['GTW'] = ""
    read_file['PAY'] = ""
    read_file['ESTADO'] = ""    
    
browseButton_CSV = tk.Button(text="      Importar CSV    ", command=getCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_CSV)

def convertToExcel ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    read_file.to_excel (export_file_path, index = None, header=True)
    

saveAsButton_Excel = tk.Button(text='Convertir CSV a EXCEL', command=convertToExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_Excel)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Salir','Desea salir?',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='   Salir    ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()