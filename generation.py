import random as rnd


def matrix_from_file(file_name):
    """"Returns a 2D matrix of integers from file_name"""
    f = open(file_name, 'r')
    matrix = [list(map(int, line.rstrip().split(' '))) for line in f]
    return matrix


def list_from_file(file_name):
    """Returns a list of integers from file_name"""
    f = open(file_name, 'r')
    matrix = list(map(int, f.readline().rstrip().split(' ')))
    return matrix


def make_diagonal_zero(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 0
    return


def symmetrize(graph):
    """Makes square matrix symmetrical"""
    for i in range(len(graph)):
        for j, item in enumerate(graph[i][i:], start=(i)):
            graph[j][i] = item
    return


def generate_gauss2(size):
    matrix = [[rnd.choices([rnd.gauss(-1, 1), rnd.gauss(1, 1)], weights=[1, 1])[0] for j in range(size)] for i in
              range(size)]
    return matrix


def random_bias(size):
    l = [(rnd.random() - 0.5) * 2 for i in range(size)]
    return l

