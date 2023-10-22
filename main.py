def read_system(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        A = []
        b = []
        for _ in range(n):
            row = list(map(float, file.readline().split()))
            A.append(row[:-1])
            b.append(row[-1])
        epsilon = float(file.readline())
    return A, b, epsilon


def diagonal_dominance(A):
    n = len(A)
    for i in range(n):
        diag_element = abs(A[i][i])
        sum_of_row = sum([abs(A[i][j]) for j in range(n)]) - diag_element
        if diag_element <= sum_of_row:
            return False
    return True


def swap_rows(A, b, i, j):
    A[i], A[j] = A[j], A[i]
    b[i], b[j] = b[j], b[i]


def seidel_method(A, b, epsilon):
    n = len(A)
    x = [0] * n
    convergence = False
    while not convergence:
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        convergence = all(abs(x_new[i] - x[i]) < epsilon for i in range(n))
        x = x_new
    return x


def main():
    A, b, epsilon = read_system("data.txt")


    # Забезпечення діагональної переваги
    if not diagonal_dominance(A):
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if abs(A[j][i]) > abs(A[i][i]):
                    swap_rows(A, b, i, j)

    # Розв'язання методом Зейделя
    result = seidel_method(A, b, epsilon)

    # Запис результату у файл
    with open("result.txt", "w") as f:
        for value in result:
            f.write(str(value) + "\n")


if __name__ == "__main__":
    main()
