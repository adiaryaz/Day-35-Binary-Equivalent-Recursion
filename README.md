# Day-35-Binary-Equivalent-Recursion
Day 35/100 - Python Program to Print Binary Equivalent of an Integer using Recursion

# Print Binary Equivalent of an Integer (Recursive)
A program to convert a given integer from base-10 (decimal) to base-2 (binary) representation using a recursive algorithmic approach.

## 📝 Description

This program takes a user-inputted integer and calculates its exact binary equivalent without relying on Python's built-in `bin()` function.

It achieves this through a pure **recursive function**. The algorithm continuously divides the number by 2 using integer floor division (`// 2`) and calculates the remainder using the modulo operator (`% 2`). Because binary strings are built from right to left, the recursive call delays the string concatenation until it reaches the base case, naturally reversing the sequence of 0s and 1s into the correct binary order. The script also includes dedicated logic to handle zero and negative numbers flawlessly.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A single integer value (can be positive, negative, or zero).

### Output:

* A formatted string stating: "The binary equivalent of [number] is [binary_representation]."

### Rules:

1. The program must accept an integer input from the user.
2. The program must utilize a **recursive function** (`binary_equivalent`) to perform the core calculation.
3. **Base Case:** If `number == 0` within the recursive function, it must return an empty string `""` to terminate the recursion loop.
4. **Recursive Step:** The function must return the recursive call of `number // 2` concatenated with the string representation of `number % 2`.
5. The driver code must explicitly handle an initial input of `0`, as the recursive function would simply return an empty string.
6. The driver code must handle negative inputs by passing the absolute value (`abs(number)`) to the function and manually prepending a minus sign (`-`) to the output.

---

## 💡 Examples

### Example 1 (Positive Integer)

**Input:**

```
10


```

**Output:**

```
The binary equivalent of 10 is 1010.


```

**Explanation:** * `binary_equivalent(10)` calls `binary_equivalent(5) + "0"`

* `binary_equivalent(5)` calls `binary_equivalent(2) + "1"`
* `binary_equivalent(2)` calls `binary_equivalent(1) + "0"`
* `binary_equivalent(1)` calls `binary_equivalent(0) + "1"`
* `binary_equivalent(0)` hits the base case and returns `""`.
* The stack unwinds and concatenates the string: `"" + "1" + "0" + "1" + "0" = "1010"`.

### Example 2 (Negative Integer)

**Input:**

```
-5


```

**Output:**

```
The binary equivalent of -5 is -101.


```

**Explanation:** The driver code detects the number is less than 0. It calculates the binary for the absolute value (5), which is `"101"`, and formats the final print statement to include the minus sign, resulting in `"-101"`.

### Example 3 (The Zero Edge Case)

**Input:**

```
0


```

**Output:**

```
The binary equivalent of 0 is 0.


```

**Explanation:** The first `if number == 0:` condition in the main code block catches this specific input and prints the hardcoded sentence, bypassing the recursive function entirely to prevent an empty string output.

### Example 4 (Large Power of Two)

**Input:**

```
16


```

**Output:**

```
The binary equivalent of 16 is 10000.


```

**Explanation:** 16 is a perfect power of two ($2^4$), so the algorithm systematically returns a single `1` followed by four `0`s.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script)

```bash
git clone https://github.com/adiaryaz/Day-35-Binary-Equivalent-Recursion.git
cd binary-equivalent-recursion


```

2. **Run the program**:

```bash
python main.py


```

Enter an integer when prompted to see its mathematical binary equivalent generated recursively.
