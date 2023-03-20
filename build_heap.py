# python3
# Aleksandra Petrovska 221RDB253


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    def heap_sort(i):
        m_index = i
        l = 2 * i + 1
        if l < len(data) and data[l] < data[m_index]:
            m_index = l
        r = 2 * i + 2
        if r < len(data) and data[r] < data[m_index]:
            m_index = r
        if i != m_index:
            swaps.append((i, m_index))
            data[i], data[m_index] = data[m_index], data[i]
            heap_sort(m_index)

    n = len(data)
    for i in range(n // 2, -1, -1):
        heap_sort(i)

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    text = input()

    # input from keyboard
    if "I" in text:
     n = int(input())
     data = list(map(int, input().split()))
    
    if "F" in text:
        file = input()
        with open("tests/" + file, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= 4 * n


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
