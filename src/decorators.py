def log(filename=None):
    def actual_log(function):
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{function.__name__} ok\n")
                else:
                    print(f"{function.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{function.__name__} error: {str(e)}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{function.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
        return wrapper
    return actual_log


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)


@log()
def new_func(x, y):
    return x - y
