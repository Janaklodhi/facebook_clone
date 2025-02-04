
def merge_sorted_arrays(arr1, arr2):
    # we need to merged the
    i, j = 0, 0  # Pointers for both arrays
    merged_array = []

    # Traverse both arrays and merge them in sorted order
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # Add remaining elements (if any) from both arrays
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])

    return merged_array