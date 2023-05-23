def mean(V):
    return sum(V) / len(V)


def sum_of_squared_deviations(V_real, V_approximated):
    sum_value = 0
    n = len(V_real)
    for i in range(n):
        sum_value += (V_approximated[i] - V_real[i]) ** 2
    return sum_value


def array_of_deviations_e(V_real, V_approximated):
    e = []
    n = len(V_real)
    for i in range(n):
        e.append(V_approximated[i] - V_real[i])
    return e


def variance(V_real, V_approximated):
    n = len(V_real)
    return sum_of_squared_deviations(V_real, V_approximated) / n


def standard_deviation(V_real, V_approximated):
    return (variance(V_real, V_approximated)) ** 0.5


def covariance(X, Y):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    n = len(X)
    x_mean = mean(X)
    y_mean = mean(Y)

    for i in range(n):
        sum1 += (X[i] - x_mean) * (Y[i] - y_mean)
        sum2 += (X[i] - x_mean) ** 2
        sum3 += (Y[i] - y_mean) ** 2
    r = sum1 / ((sum2 * sum3) ** 0.5)
    return r


def rate_covariance(r):
    if r < 0.3:
        return "connection is weak"
    if 0.3 <= r < 0.5:
        return "connection is moderate"
    if 0.5 <= r < 0.7:
        return "conspicuous connection"
    if 0.7 <= r < 0.9:
        return "connection is strong"
    if 0.9 <= r < 0.99:
        return "connection is very strong"
    if 0.99 <= r <= 1.1:
        return "direct connection"
    else:
        return "WTF?"


def squared_sum(X):
    summary = 0
    n = len(X)
    for i in range(n):
        summary += X[i] ** 2
    return summary


def R2(V_real, V_approximated):
    n = len(V_real)
    return 1 - (sum_of_squared_deviations(V_real, V_approximated)) / (
                squared_sum(V_approximated) - 1 / n * (sum(V_approximated) ** 2))
