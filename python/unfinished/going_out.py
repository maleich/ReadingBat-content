# @desc# @desc When you get ready for school, you need to spend 30-45 minutes . if it's the weekend however you do not need to get ready
# @desc# @desc by Zara '24

def getting_ready(time, is_weekend):
    return time >= 40 if is_weekend else time in range(30,45)


def main():
    getting_ready(40, False)
    getting_ready(20, True)


if __name__ == '__main__':
    main()