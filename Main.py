import threading
import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES
import FileOperator as fo

file_data = None


class Mainwindow:

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="选择文件", filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])
        if file_path:
            # label_result.config(text=f'选择的文件路径：{file_path}')
            pass

    def updateLabel(self):
        global file_data
        while True:
            print(file_data)
            if not file_data:
                file_data = fo.file_data

    def onCreate(self):
        global file_data
        # create a window
        window = TkinterDnD.Tk()

        drop = fo.drop

        window.drop_target_register(DND_FILES)
        window.dnd_bind('<<Drop>>', drop)
        window.dnd_bind('<Leave>', fo.on_drag_leave)

        # 创建编辑框
        entry = tk.Entry(window, width=30)
        entry.pack(pady=10)

        # create a label
        label_result = tk.Label(window, width=40, height=10,
                                relief="solid", borderwidth=1, anchor='nw', justify='left')
        label_result.pack(pady=10)

        # Mainwindow().open_file_dialog()
        print(file_data, '===')
        t = threading.Thread(target=Mainwindow().updateLabel)
        t.start()
        label_result.config(text='file_data')

        window.mainloop()


Mainwindow().onCreate()
