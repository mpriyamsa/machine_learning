import matplotlib.pyplot as plt

SAMPLE_SIZE = 4
ALPHA = 0.1
TOTAL_ITER = 350


def get_data():
    data = {}
    count = 0
    while count < SAMPLE_SIZE:
        x = input("Enter x value:")
        data[count] = [int(x)]
        y = input("Enter y value:")
        data[count].append(int(y))
        count = count + 1
    return data


def gradient_descent(theta0, theta1, data):
    count = 0
    while count <= TOTAL_ITER:
        temp0 = theta0 - ALPHA * error_average(theta0, theta1, data)
        temp1 = theta1 - ALPHA * x_error_average(theta0, theta1, data)
        theta0 = temp0
        theta1 = temp1
        count = count + 1
    x = [-1, 0, 1, 2, 3, 4, 5, 6]
    y = []
    for item in x:
        y.append(theta0 + theta1 * item)
    plt.plot(x, y)
    x = []
    y = []
    for i in data:
        x.append(data[i][0])
        y.append(data[i][1])
    plt.scatter(x, y, color="red", marker="o", s=30)
    plt.show()


def x_error_average(theta0, theta1, data):
    sum_error = 0
    for i in data:
        sum_error = sum_error + ((theta0 + theta1 * data[i][0]) - data[i][1]) * data[i][0]
    return sum_error / SAMPLE_SIZE


def error_average(theta0, theta1, data):
    sum_error = 0
    for i in data:
        sum_error = sum_error + (theta0 + theta1 * data[i][0]) - data[i][1]
    return sum_error/SAMPLE_SIZE


def rms(theta0, theta1, data):
    sum_error = 0
    for i in data:
        sum_error = sum_error + ((theta0 + theta1 * data[i][0]) - data[i][1]) ** 2
    return sum_error/2*SAMPLE_SIZE


def main():
    theta0 = 0
    theta1 = 1
    gradient_descent(theta0, theta1, get_data())


if __name__ == '__main__':
    main()
