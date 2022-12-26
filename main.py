from limit import Limit


def culc(f, x, side=''):

    a = Limit(f, x, side)

    a.calculate_limit()

    return main()


def main():
    function = input('input equation: ')
    arg = float(input('input value: '))
    side = input('input side (+/-): ')

    print(culc(function, arg, side))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
