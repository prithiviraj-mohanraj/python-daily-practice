# Day 1:
# Practice on second/third max/min tracking logic without built-in functions like max(), min(), sort(), or set()
# These types of problems are often asked in Python rounds for Data Engineering interviews

# ------------------------------
# 1. Second Maximum in a List
# ------------------------------

def second_max(numbers: list[int]) -> int | None:
    """
    Returns the second maximum unique value from the list.
    Time: O(n), Space: O(1)
    """
    if len(numbers) < 2:
        return None

    first = second = float("-inf")
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float("-inf") else None

print("Second max:", second_max([34, 12, 63, 48, 333]))  # 63


# ------------------------------
# 2. Second Minimum in a List
# ------------------------------

def second_min(numbers: list[int]) -> int | None:
    """
    Returns the second smallest unique value from the list.
    Time: O(n), Space: O(1)
    """
    if len(numbers) < 2:
        return None

    first = second = float("inf")
    for num in numbers:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num

    return second if second != float("inf") else None

print("Second min:", second_min([34, 12, 63, 12, 9, 333]))  # 12


# ------------------------------
# 3. Third Maximum in a List
# ------------------------------

def third_max(numbers: list[int]) -> int | None:
    """
    Returns the third maximum unique value from the list.
    Time: O(n), Space: O(1)
    """
    first = second = third = float("-inf")
    for num in numbers:
        if num in (first, second, third):
            continue
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num

    return third if third != float("-inf") else None

print("Third max:", third_max([34, 12, 63, 48, 333, 12, 63]))  # 63


# ------------------------------
# 4. Second Highest Salary in a Dictionary
# ------------------------------

def second_max_salary(employees: dict[str, int]) -> list[str] | None:
    """
    Returns a list of employee names who have the second highest unique salary.
    Time: O(n), Space: O(1)
    """
    first = second = float("-inf")
    for salary in employees.values():
        if salary > first:
            second = first
            first = salary
        elif first > salary > second:
            second = salary

    if second == float("-inf"):
        return None

    return [name for name, sal in employees.items() if sal == second]

employee_data = {
    "Alice": 75000,
    "Bob": 98000,
    "Charlie": 47000,
    "David": 89000,
    "Eve": 98000
}

print("Employees with 2nd highest salary:", second_max_salary(employee_data))  # ['David']
