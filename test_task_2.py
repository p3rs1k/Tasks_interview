from task_2 import deg_to_dm


def test_task2():
    test = [
        (90, "90^0.0'E"),
        (50, "50^0.0'E"),
        (-90, "270^0.0'W"),
        (-89.1233, "271^7.398'E"),
        (-180.334, "180^20.04'W"),
        (180.334, "180^20.04'W"),
        (100, "100^0.0'W"),
        (32532.1222, "132^7.332'W"),

    ]
    for (given, expected) in test:
        assert deg_to_dm(given) == expected, "Wrong answer"
    print("Tests completed")


if __name__ == '__main__':
    test_task2()