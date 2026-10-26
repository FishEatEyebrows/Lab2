import statistics

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    avg = calc_average(num_list)
    print("Average number: ", avg)
    max, min = find_min_max(num_list)
    print("Maximum number: ", max, "Minimum number: ", min)
    sorted_list = sort_temperature(num_list)
    print("Sorted list: ", sorted_list)
    median = calc_median_temp(sorted_list)
    print("Median number: ", median)


def display_main_menu():
    print("Enter some numbers seperated by commas")

def get_user_input():
    inputs = input().split(",")
    return inputs

def calc_average(y):
    total = 0
    for x in y:
        total += float(x)
    average = total / len(y)
    return float(average)

def find_min_max(x):
    maximum = max(x)
    minimum = min(x)
    return maximum, minimum
10
def sort_temperature(z):
    new_list = []
    for x in z:
        new_list.append(float(x))
    new_list.sort()
    return new_list

def calc_median_temp(b):
    m = statistics.median(b)
    return m

if __name__ == "__main__":
    main()