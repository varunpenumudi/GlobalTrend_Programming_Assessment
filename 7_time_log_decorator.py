import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, *kwargs)
        end_time = time.perf_counter()
        time_taken = round(end_time - start_time)
        print(f"Time taken is {time_taken} seconds")

    return wrapper


@time_decorator
def do_something():
    time.sleep(3)
    print("Done Something ")


if __name__ == "__main__":
    do_something()
