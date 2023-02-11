import matplotlib.pyplot as plt


def create_subplot(x_values, y_values, scalar, start_percent, end_percent):
    value_interval = (x_values[-1] - x_values[0]) / len(x_values)  # distance between two values

    distance_x_values = x_values[-1] - x_values[0]  # span of the function's domain

    step01 = round((distance_x_values * start_percent) / value_interval)
    step02 = round((distance_x_values * end_percent) / value_interval)

    y_values_update = [i * scalar for i in y_values[step01:step02+1]]

    plt.plot(x_values[step01:step02+1], y_values_update, label='function: f(x)', color='red')

    plt.xlabel('x_axis: x')
    plt.ylabel('y_axis: f(x)')
    plt.title('function_graph')
    plt.legend()
    plt.grid(True)

    plt.savefig('plot.pdf', format='pdf')
    plt.show()
