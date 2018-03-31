from load_file import load_file
from Path import Path
import matplotlib.pyplot as plt


def main():
    # Straight Path Test, set up your path
    x_start = 0
    y_start = 0
    straight_path_file = 'path_SRC\straight_path.csv'
    straight_line = load_file(straight_path_file)
    straight_path = Path(straight_line, x_start, y_start)

    # Test against simulated movement
    print('----------- Actual vs. Expected Straight Line-------------------')
    actual_line_file = 'path_SRC\straight_error_path.csv'
    actual_line = load_file(actual_line_file)

    line_error = []
    line_index = []

    for i in range(0, len(actual_line[0][:]) - 1):
        actual = [actual_line[0][i], actual_line[1][i]]
        error, index = straight_path.find_error(actual)
        line_error.append(error)
        line_index.append(index)
        # print("Error:", error)
        # print("Index: ", index)

    # Curve Path Test, set up your path
    circle_path_file = 'path_SRC\circle_path.csv'
    circle = load_file(circle_path_file)
    circle_path = Path(circle, x_start, y_start)

    curve_error = []
    curve_index = []

    # arbitrary test points
    print('----------- Actual vs. Expected Circle Path-------------------')
    actual_circle_file = 'path_SRC\circle_error_path.csv'
    actual_circle = load_file(actual_circle_file)
    for i in range(0, len(actual_circle[0][:]) - 1):
        actual = [actual_circle[0][i], actual_circle[1][i]]
        error, index = circle_path.find_error(actual)
        curve_error.append(error)
        curve_index.append(index)

    # plot errors
    # There is a plotting artifact on the last position, I need to figure out to solve the last position if you go beyond the last position.
    circle = plt.figure(1)
    plt.plot(curve_index, curve_error)
    plt.show()

    line = plt.figure(2)
    plt.plot(line_index, line_error)
    plt.show()


if __name__ == '__main__':
    main()
