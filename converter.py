import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(
        description="Convert temperature between Celsius and Fahrenheit."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--celsius', type=float, help='Temperature in Celsius to convert to Fahrenheit.')
    group.add_argument('-f', '--fahrenheit', type=float, help='Temperature in Fahrenheit to convert to Celsius.')

    args = parser.parse_args()

    if args.celsius is not None:
        f = celsius_to_fahrenheit(args.celsius)
        print(f"{args.celsius:.2f}°C = {f:.2f}°F")
    elif args.fahrenheit is not None:
        c = fahrenheit_to_celsius(args.fahrenheit)
        print(f"{args.fahrenheit:.2f}°F = {c:.2f}°C")

if __name__ == "__main__":
    main()
