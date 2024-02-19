# Expand previous Homework 5 with additional class, which allow to provide records by text file:
# 1.Define your input format (one or many records)
# 2.Default folder or user provided file path
# 3.Remove file if it was successfully processed
# 4.Apply case normalization functionality form Homework 3/4

import os
import time
from task_4 import normalization

class ExportToFile:

    default_path = 'C:\\Users\\ana_kalandadze\Desktop\dev'

    def to_txt(self, data):
        
        file_path = input('Plase provide file path(in case of using default please leave empty) ')

        if not file_path:
            file_path = os.path.join(self.default_path,"news.txt")

        with open(file_path, 'w') as file:
            file.write(normalization(data))
        
        return file_path

    def remove_file(self, file_path, delay = 30):

        time.sleep(delay)

        if os.path.exists(file_path):
            os.remove(file_path)
            