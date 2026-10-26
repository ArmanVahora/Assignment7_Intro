
import os  # os module to handle PATH flexibility for writing to the file

MIN_PRECIPITATION = 0.0
MAX_PRECIPITATION = 366.0

OUTPUT_FILE = 'precipitation.txt'


def main():
    # Create a list of the month names.
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    # Create a list with 12 precipitation values.
    precipitation = [0.0] * 12

    # Ask the user to enter precipitation for each month.
    for i in range(len(months)):
        precipitation[i] = get_precipitation(months[i])

    # Analyze the precipitation data.
    analyze_precipitation(precipitation, months)

    # Save the data to a text file.
    path = write_precipitation_file(months, precipitation)
    print(f'Data saved to {path}')


def get_precipitation(month):
    # Ask for precipitation until the user enters a valid number.
    while True:
        try:
            amount = float(input(f'Enter precipitation for {month}: '))

            if MIN_PRECIPITATION <= amount <= MAX_PRECIPITATION:
                return amount
            else:
                print('Please enter a number between 0 and 366.')

        except ValueError:
            print('Invalid input. Please enter a number.')


def analyze_precipitation(precipitation, months):
    # Calculate total and average precipitation.
    total = sum(precipitation)
    average = total / len(precipitation)

    # Find the highest and lowest precipitation.
    highest = max(precipitation)
    lowest = min(precipitation)

    # Find the months with the highest and lowest precipitation.
    highest_index = precipitation.index(highest)
    lowest_index = precipitation.index(lowest)

    highest_month = months[highest_index]
    lowest_month = months[lowest_index]

    # Display the results.
    print('\nPrecipitation Analysis')
    print('----------------------')
    print(f'Total annual precipitation: {total:.2f} inches')
    print(f'Average monthly precipitation: {average:.2f} inches')
    print(f'Highest precipitation: {highest:.2f} inches in {highest_month}')
    print(f'Lowest precipitation: {lowest:.2f} inches in {lowest_month}')


def write_precipitation_file(months, precipitation, filename=OUTPUT_FILE):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    try:
        with open(path, 'w') as output_file:
            # Write each month and its precipitation to the file.
            for i in range(len(months)):
                output_file.write(f'{months[i]},{precipitation[i]}\n')

    except OSError as error:
        print(f"Could not save the data to '{path}': {error}")
        return None

    return path


# Call the main function only if this file is run directly.
if __name__ == '__main__':
    main()
