from random import shuffle


def simple_bubble_sort(nums: list) -> list:

    n = len(nums)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def bubble_sort(nums: list) -> list:

    n = len(nums)

    for i in range(n - 1):
        not_permutated = True
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                not_permutated = False
        if not_permutated:
            break

    return nums


def main():

    nums = list(range(-50, 51))
    shuffle(nums)
    print(f"\nUnsorted list:\n{nums}")

    simple_bubble_sort(nums)
    print(f"\nSorted list (simple_bubble_sort):\n{nums}\n")

    bubble_sort(nums)
    print(f"\nSorted list (bubble_sort):\n{nums}\n")


if __name__ == "__main__":
    main()
