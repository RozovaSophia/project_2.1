from datetime import time
import logging

with open("filename.txt", encoding="UTF-8" "w") as file:
    contents = file.read()
    def log(filename):
        def actual_log(function):
            def wrapper(*args, **kwargs):
                time_1 = time.time()
                result = function(*args, **kwargs)
                time_2 = time.time()
                if filename:
                    file_handler = logging.basicConfig(filename, level=logging.INFO, encoding='utf-8', mode='a')
                else:
                    print(f"Function {function.__name__} took {time_2 - time_1} seconds")
                return result
            return wrapper
        return actual_log