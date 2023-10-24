def shell_sort(array):
  """Sorts an array using the shell sort algorithm.

  Args:
    array: An array to be sorted.

  Returns:
    A sorted array.
  """

  # Initialize the gap size.
  gap = len(array) // 2

  # While the gap is greater than zero, perform the following steps:
  while gap > 0:

    # Iterate over the array with the given gap size.
    for i in range(gap, len(array)):

      # Compare the current element with the element at the gap distance away.
      current = array[i]
      j = i - gap

      # While the current element is smaller than the element at the gap
      # distance away, swap the two elements.
      while j >= 0 and array[j] > current:
        array[i] = array[j]
        i = j
        j -= gap

      # Assign the current element to the gap distance away.
      array[i] = current

    # Reduce the gap size.
    gap //= 2

  return array


# Example usage:

array = [5, 3, 2, 1, 4]

sorted_array = shell_sort(array)

print(sorted_array)
