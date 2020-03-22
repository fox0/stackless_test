import stackless


def main():
    # очередь
    stackless.tasklet(task)(2)
    stackless.tasklet(task)(3)
    stackless.tasklet(task)(4)
    stackless.tasklet(task)(5)
    stackless.tasklet(task)(6)
    stackless.run()


def task(arg):
    r = 1
    for i in range(100_000):
        r *= arg
    print(r)


if __name__ == '__main__':
    main()
