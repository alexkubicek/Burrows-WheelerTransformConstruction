import sys
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def bwt_matrix(genome):
    matrix = []
    for i in range(len(genome)):
        matrix.append(genome[i:] + genome[:i])
    return matrix


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filePath = input()
    inFile = open(filePath)
    text = inFile.readline()
    while text.endswith("\n"):
        text = text[:len(text)-1]
    if not text.endswith("$"):
        text = text + "$"
    index_to_print = len(text)-1
    m = bwt_matrix(text)
    m.sort()
    f = open("output.txt", "w")
    sys.stdout = f
    for line in m:
        print(line[index_to_print], end="")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
