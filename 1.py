import random

def fast_search(array, start, end):
    if not array:
        return
    if len(array) == 0:
        return
    if start >= end:
        return

    store_start = start
    store_end = end

    index = random.randint(start, end)
    value = array[index]

    store = array[start]
    array[start] = array[index]
    array[index] = store

    while start < end:
        while(start < end) and (array[end] >= value):
            end -= 1
        while(start < end) and (array[end] < value):
            array[start] = array[end]
            start += 1
            array[end] = array[start]

    array[start] = value
    fast_search(array, store_start, end)
    fast_search(array, end+1, store_end)

import random

def fast_search2(array, start, end):
    if not array:
        return
    if len(array) == 0:
        return
    if start >= end:
        return

    store_start = start
    store_end = end

    index = random.randint(start, end)
    value = array[index]

    store = array[start]
    array[start] = array[index]
    array[index] = store

    while start < end:
        while(start < end) and (array[end] >= value):
            end -= 1
        while(start < end) and (array[end] < value):
            array[start] = array[end]
            start += 1
            array[end] = array[start]
    array[start] = value
    fast_search(array, store_start, end)
    fast_search(array, end+1, store_end)
