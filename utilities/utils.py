from datetime import datetime as dt

# Decorator to see execution time of a function
def my_timing(func):
    def wrapper(*args,**kwargs):
        start = dt.now()
        result = func(*args,**kwargs)
        # Other Statements
        end = dt.now()
        print(f"Execution Time: {end-start} ms")

        return result
    return wrapper

@my_timing
def add(a,b):
    return a+b

if __name__ == '__main__':
    print(add(45,67))