import multiprocessing


def print_even():
    for i in range(2, 21, 2):
        print(f"Even: {i}")


def print_odd():
    for i in range(1, 21, 2):
        print(f"Odd: {i}")


if __name__ == "__main__":
    process1 = multiprocessing.Process(target=print_even)
    process2 = multiprocessing.Process(target=print_odd)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
