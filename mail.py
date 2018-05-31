#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import tkinter as tk
import tkinter.filedialog
from tkinter import messagebox
from smtplib import SMTP, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


smtp_server='smtp.gmail.com'
port= 587
login='pymailbo1@gmail.com' # test mail account
passwrd='Sqwe1456FDgwe'


msg = MIMEMultipart()
def open_file():
    try:
        filename = tk.filedialog.askopenfilename(initialdir=".", title="Select file",
                                                 filetypes=(("all files", "*.*"),))
        with open(filename, 'rb') as file:
            fn=os.path.basename(filename)
            part = MIMEBase('application', "octet-stream")
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(fn))
            msg.attach(part)
            label_attach['text']+=fn+' '
    except FileNotFoundError:
        pass


def send_mail(subject, mes_to, mes_body):
    try:
        msg['To'] = mes_to
        msg['From'] = login
        msg['Subject'] = subject+'\n\n'
        msg.attach(MIMEText(mes_body))
        msmtp = SMTP(smtp_server, port)
        msmtp.ehlo()
        msmtp.starttls()
        msmtp.ehlo()
        msmtp.login(login, passwrd)
        msmtp.send_message(msg)
        msmtp.close()
    except SMTPException as ex:
        messagebox.showerror('Ошибка', 'Сообщение не отправлено')


window=tk.Tk()
window.geometry('505x620')
window.geometry('+' + str(window.winfo_screenwidth() // 2 - 252) + '+' + str(window.winfo_screenheight() // 2 - 310))
window.resizable(0, 0)
window.option_add('*Font', 'Arial 12 normal')
menu=tk.Menu(window)
menu.add_command(label='Прикрепить файл', command=open_file)
window.config(menu=menu)
window.title('Mail Sendler')
tk.Label(window, text="Получатель").place(x=42, y=5)
tk.Label(window, text='Тема письма').place(x=42, y=52)
edit_subject=tk.Entry(window, width=46)
edit_mto=tk.Entry(window, width=46)
tk.Label(window, text="Текст письма").place(x=40, y=100)
label_attach=tk.Label(window, text='Файлы: ', justify=tk.LEFT, wraplength=300)
text_edit=tk.Text(window, height=22, width=46, wrap=tk.WORD)
btn_ok=tk.Button(window, pady=10, padx=10, text="Отправить", bg='green', fg='white', font='Arial 12 bold',
                 command=lambda :send_mail(edit_subject.get(),edit_mto.get(),text_edit.get(1.0,tk.END)), )
label_attach.place(x=44, y=535)
text_edit.place(x=43, y=125)
edit_mto.place(x=44, y=26)
edit_subject.place(x=44, y=75)
btn_ok.place(x=341, y=535)
window.mainloop()
