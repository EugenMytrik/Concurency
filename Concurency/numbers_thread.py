import threading


def print_even():
    for i in range(2, 21, 2):
        print(f"Even: {i}")


def print_odd():
    for i in range(1, 21, 2):
        print(f"Odd: {i}")


if __name__ == "__main__":
    thread1 = threading.Thread(target=print_even)
    thread2 = threading.Thread(target=print_odd)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
