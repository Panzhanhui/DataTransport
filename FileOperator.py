file_data=None
def drop(event):
    global file_data
    file_path = event.data
    if file_path:
        try:
            with open(file_path, 'r',encoding='utf-8') as file:
                file_data = file.read()
                print('===',file_data)
                # return file_data
                # label_result.config(text=f'文件数据:\n{file_data}')
        except Exception as e:
            print ('读取文件时发生错误')
def on_drag_leave(event):
 
        event.widget.configure(bg='white')    