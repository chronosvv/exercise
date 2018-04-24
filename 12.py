def max_root(data, root, size):
    while root <= (size-2)/2:
        left = root * 2 + 1
        right = root * 2 + 2
        larger = root
        if left < size and data[left] > data[larger]:
            larger = left
        if right < size and data[right] > data[larger]:
            larger = right
        if larger != root:
            change = data[larger]
            data[larger] = data[root]
            data[root] = change
            root = larger
        else:
            root = size

def get_heap(data):
    for i in range((len(data)-2)//2, -1, -1):
        max_root(data, i, len(data))

def get_sorted_heap(data):
    get_heap(data)
    for i in range(len(data)-1, -1, -1):
        change = data[i]
        data[i] = data[0]
        data[0] = change
        max_root(data, 0, i)

if __name__ == "__main__":
    data = [2, 3, 5, 1, 22, 25, 10]
    get_sorted_heap(data)
    print(data)