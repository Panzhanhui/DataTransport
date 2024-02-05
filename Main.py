import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES
class Mainwindow:
    
    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(title="选择文件", filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])
        if file_path:
            # label_result.config(text=f'选择的文件路径：{file_path}')
            pass

    def onCreate(self):
        window = TkinterDnD.Tk()
    
        window.drop_target_register(DND_FILES)
        # 创建编辑框
        entry = tk.Entry(window, width=30)
        entry.pack(pady=10)

        Mainwindow().open_file_dialog()
        window.mainloop()
Mainwindow().onCreate()