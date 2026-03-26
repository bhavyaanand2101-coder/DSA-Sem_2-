
# PART A: STACK ADT
class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# PART B: FACTORIAL (RECURSIVE)
def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0:
        return 1
    return n * factorial(n - 1)

# PART B: FIBONACCI
fib_naive_calls = 0
fib_memo_calls = 0

def fib_naive(n):
    global fib_naive_calls
    fib_naive_calls += 1
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo={}):
    global fib_memo_calls
    fib_memo_calls += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# PART C: TOWER OF HANOI
def hanoi(n, source, auxiliary, destination, moves):
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n - 1, source, destination, auxiliary, moves)
    moves.append(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination, moves)


# PART D: BINARY SEARCH
def binary_search(arr, key, low, high, stack):
    if low > high:
        return -1

    mid = (low + high) // 2
    stack.push(mid)

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1, stack)
    else:
        return binary_search(arr, key, mid + 1, high, stack)


# MAIN FUNCTION
def main():
    print("=== AERT TOOLKIT OUTPUT ===\n")

    # Factorial Tests
    print("Factorial Tests:")
    for n in [0, 1, 5, 10]:
        print(f"factorial({n}) =", factorial(n))

    print("\nFibonacci Tests:")
    for n in [5, 10, 20, 30]:
        global fib_naive_calls, fib_memo_calls
        fib_naive_calls = 0
        fib_memo_calls = 0

        naive_result = fib_naive(n)
        naive_calls = fib_naive_calls

        memo_result = fib_memo(n, {})
        memo_calls = fib_memo_calls

        print(f"\nFibonacci({n}):")
        print("Naive Result:", naive_result, "| Calls:", naive_calls)
        print("Memo Result:", memo_result, "| Calls:", memo_calls)

    # Tower of Hanoi
    print("\nTower of Hanoi (N = 3):")
    moves = []
    hanoi(3, "A", "B", "C", moves)
    for move in moves:
        print(move)

    # Binary Search
    print("\nBinary Search Tests:")
    arr = [1, 3, 5, 7, 9, 11, 13]
    tests = [7, 1, 13, 2]

    for key in tests:
        stack = StackADT()
        index = binary_search(arr, key, 0, len(arr) - 1, stack)
        print(f"Search {key} → Index:", index, "| Mid indices:", stack.stack)

    # Empty array test
    stack = StackADT()
    print("Search in empty array →", binary_search([], 5, 0, -1, stack))


if __name__ == "__main__":
    main()

