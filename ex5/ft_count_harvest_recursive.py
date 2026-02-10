def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recursive_counter(days)
    print("Harvest time!")


def recursive_counter(n):
    if (n == 0):
        return
    recursive_counter(n - 1)
    print("Day", n)
