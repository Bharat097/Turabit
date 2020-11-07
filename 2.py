"""Remove duplicate words from string and sort them alphabetically."""

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    j = start

    while j < end:
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i+1], arr[end] = arr[end], arr[i+1]

    return i+1


def quicksort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quicksort(arr, start, p-1)
        quicksort(arr, p+1, end)


if __name__ == "__main__":
    try:
        freq = {}
        string = input("Enter String: ").split()
        for each in string:
            if not freq.get(each):
                freq[each] = 1
        string = list(freq.keys())
        quicksort(string, 0, len(string)-1)
        print("\n\nString after removing duplicates and sorting alphabetically\n")
        print(" ".join(string))
        print()
    except Exception:
        print("Invalid Input Supplied... Please Try Again...")
