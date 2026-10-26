
import os  # for handling file reading
import matplotlib.pyplot as plt  # for creating charts

# Name of the text file created by precipitation_analysis.py.
INPUT_FILE = 'precipitation.txt'


def main():
    months, precipitation = read_precipitation_file(INPUT_FILE)

    if len(months) > 0:
        show_bar_chart(months, precipitation)


def read_precipitation_file(filename):
    # Create two empty lists to store the data.
    months = []
    precipitation = []

    # Look for the file in the same folder as this program.
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    try:
        with open(path, 'r') as input_file:
            # Read each line from the file.
            for line in input_file:
                # Separate the month and precipitation amount.
                month, amount = line.strip().split(',')

                # Add the values to their lists.
                months.append(month)
                precipitation.append(float(amount))

    except FileNotFoundError:
        print(f"Could not find '{filename}'. Run precipitation_analysis.py first.")
    except ValueError:
        print(f"'{filename}' is not in the expected 'month,amount' format.")
        months = []
        precipitation = []

    return months, precipitation


def show_bar_chart(months, precipitation):
    # Use the first three letters of each month name so the labels fit.
    short_names = [month[:3] for month in months]

    # Create a bar chart.
    plt.bar(short_names, precipitation)

    # Add a title and labels.
    plt.title('Monthly Precipitation')
    plt.xlabel('Months')
    plt.ylabel('Precipitation (inches)')

    # Display the chart.
    plt.show()


# Call the main function only if this file is run directly.
if __name__ == '__main__':
    main()
