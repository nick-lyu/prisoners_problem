import random


def prisoners_try(n=100):
    prisoner_boxes = list(range(n))
    random.shuffle(prisoner_boxes)
    for i in range(n):
        current_num = i
        for j in range(n // 2):
            if prisoner_boxes[current_num] == i:
                break
            else:
                current_num = prisoner_boxes[current_num]
            if j == n // 2 - 1:
                return False
    return True


if __name__ == '__main__':
    cycle_nums = 10000
    result = [prisoners_try() for i in range(cycle_nums)].count(True)
    print(f'{result * 100 / cycle_nums}% успешных открытий всех коробок из {cycle_nums} попыток')
