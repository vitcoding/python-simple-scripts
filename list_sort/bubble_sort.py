from random import shuffle


def simple_bubble_sort(nums: list) -> list:

    n = len(nums)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def main():
    nums = list(range(-50, 51))
    shuffle(nums)
    print(f"\nUnsorted list:\n{nums}")
    simple_bubble_sort(nums)
    print(f"\nSorted list:\n{nums}")


if __name__ == "__main__":
    main()
