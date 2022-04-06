def laps_to_miles(user_laps):
    return user_laps * .25

if __name__ == '__main__':
    print(f'{laps_to_miles(float(input())):.2f}')
