def drop(event):
    file_path = event.data
    if file_path:
        try:
            with open(file_path, 'r') as file:
                file_data = file.read()
                return file_data
                # label_result.config(text=f'文件数据:\n{file_data}')
        except Exception as e:
            return '读取文件时发生错误'