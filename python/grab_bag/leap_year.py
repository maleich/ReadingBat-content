# @desc When is the next leap year after the given year?
# @desc by Aiden '24

def next_leap_year(current_year):
    final = current_year - current_year % 4
    return final + 4


def main():
    print(next_leap_year(2018))
    print(next_leap_year(2020))
    print(next_leap_year(2055))
    print(next_leap_year(37669))


if __name__ == '__main__':
    main()
