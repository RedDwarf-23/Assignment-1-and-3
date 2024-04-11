print("Input: ")

def athlete_sort():
    # initiailzing map function
    N, M = map(int, input().split())

    # taking for rows
    rows = [input() for _ in range(N)]


    # taking input from user

    K = int(input())

    print("\nOutput: \n")


    # sorting using sorted function
    for row in sorted(rows, key=lambda row: int(row.split()[K])):
        print(row)

# Calling the function
athlete_sort()