import threading
import time
import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES
import FileOperator as fo
import Network as ntk

file_data = None


class Mainwindow:

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="选择文件", filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])
        if file_path:
            # label_result.config(text=f'选择的文件路径：{file_path}')
            pass

    
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
        entry.pack(pady=(10))

        # create a label
        label_result = tk.Label(window, width=150, height=10,
                                relief="solid", borderwidth=1, anchor='nw', justify='left')
        label_result.pack(pady=10)
        label_result.place(relx=0.5, rely=0.95, anchor='s',
                           bordermode='outside')

        # Mainwindow().open_file_dialog()

        # set label_result to labelTag for Show
        fo.labelTag = label_result

        # create a transmit button
        button = tk.Button(window, text="transmit", command=ntk.start())
        button.pack(pady=10)

        window.mainloop()


Mainwindow().onCreate()
