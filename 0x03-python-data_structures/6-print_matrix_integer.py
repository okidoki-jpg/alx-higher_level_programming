#!/usr/bin/python3
if __name__ == "__main__":
    def print_matrix_integer(matrix=[[]]):
        for i in range(len(matrix)):
          for j in range(len(matrix[i])):
              print("{:d}".format(matrix[i][j]), end='')
              if j == len(matrix[i]) - 1:
                  continue
              print(end=" ")
          print()
