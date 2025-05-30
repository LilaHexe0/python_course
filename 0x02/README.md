[© 2025, A.Voß, FH Aachen, codebasedlearning.dev](mailto:info@codebasedlearning.dev)

# Unit `0x02` – First Steps


## Topics covered

- Primitives
- Collections
- Control-flow
- Function calling


## General Comments

---

### Primitives

- The topic of this folder is 'primitives', like in other languages, so here `int`, `bool`, `float` and `string`. We have omitted some standard types here and will deal with them later, e.g. `complex` or special types such as `NoneType`. 
- Actually there are no 'primitives' in Python, only objects. You can see this by looking at the definition in builtins.py, e.g. via the 'PyCharm' context menu on `int`, then 'Go To Declaration'. 
- `int` and `float` are so-called 'numeric types'.
- Primitive types are immutable. This means that once a variable of a primitive type is assigned a value, the value itself cannot be changed. Instead, operations result in new objects being created.

---

### Collections

- Standard 'collections' are: `list`, `tuple`, `dict`, `set`, `frozenset`, `range`. In fact, `range` does not __contain__ all the numbers but behaves like a read-only-collection. We have omitted some standard types here and will deal with them later, e.g. binary types such as `bytes`, `bytearray`, and `memoryview`.
- Some of the containers are mutable, others are not. For each container or collection, we first consider the operations that do not modify the data (e.g. read, find, contains, traverse, construction) and then the operations that modify the data (e.g. write, add/insert, delete). So, these are the operations that should always be on a cheat sheet if you are making one:
  - access or search a specific element (all cases)
  - add and remove an element (if mutable)


## Tasks

---

### 👉 Task 'Self-Study'

- Review all snippets from the lecture. Ask if there are any outstanding questions.
- Run and understand all content from scripts that start with `self_`. Ask if you miss an idea.

---

### 👉 Task 'Recap'

- Review any outstanding tasks from previous units. Is there any task that you should definitely do or have questions about?

---

### 👉 Task 'Coral Cove' (Graph)

You are given a weighted, undirected graph. It is represented as a dictionary where the keys are node numbers, and the values are dictionaries. These nested dictionaries denote the neighbors of the given node and the weight of the edges that connect the node to its neighbors.

Graph Representation

```
GRAPH = {
    1: {2: 5, 3: 1},
    2: {1: 5, 3: 3},
    3: {1: 1, 2: 3, 4: 2},
    4: {3: 2}
}
```

- Node `1` connects to node `2` with weight `5` and node `3` with weight `1`.
- Node `2` connects back to node `1` (weight `5`) and node `3` (weight `3`).
- Node `3` connects to nodes `1`, `2`, and `4` with weights `1`, `3`, and `2`, respectively, and so on.

Task

- Write a function `find_min_weight_neighbor` working on `GRAPH` to find the neighbor of a given node with the lowest edge weight in the graph. If there are multiple neighbors with the same lowest weight, return any one of them.
  - For start node `3`, the solver would look for node `3`'s neighbors `{1: 1, 2: 3, 4: 2}` and return the minimum weight neighbor `(1, 1)` (neighbor = `1`, weight = `1`).

- Print the result for all nodes in `GRAPH`.

- Bonus: Write a function to calculate the shortest path from a given starting node to all other nodes in the graph.
  - Hint: 'Dijkstra', `heapq`.

Check
- Compare your solution with `coral_cove_one_solution.py` in `solutions`. 
  - Is your solution correct and complete? 
  - Do you have any ideas on how to improve your solution?
  - Is there a detail where your solution is better or different? Tell us.

---

### 👉 Task 'Buxrose Edge' (Students)

You are tasked with analyzing student performance data stored in the dictionary `GRADES` (below, grade 100.0 is best, below 40.0 fail). Each student has scores across different subjects.

```
MATH = "Math"
ENGLISH = "English"
PHYSICS = "Physics"

SUBJECTS = [MATH, ENGLISH, PHYSICS]

GRADES = {
    "Alice": {MATH: 85, ENGLISH: 78, PHYSICS: 92},
    "Bob": {MATH: 56, ENGLISH: 33, PHYSICS: 52},
    "Charlie": {MATH: 97, ENGLISH: 88, PHYSICS: 91},
    "Diana": {MATH: 42, ENGLISH: 30, PHYSICS: 36},
    "Eve": {MATH: 67, ENGLISH: 80, PHYSICS: 45},
}
```

Questions can be found in the main solver:

```
def solve():
    average_grades = calc_average_grades()
    print(f" 1| {average_grades=}")

    top_student, highest_average = determine_top_performer(average_grades)
    print(f" 2| {top_student=} with {highest_average:.2f}")

    students_below_40 = determine_all_students_with_a_fail()
    print(f" 3| {students_below_40=}")

    passed_subjects = determine_subjects_everyone_passed()
    print(f" 4| {passed_subjects=}")

    student_names_sorted = sort_students_by_average_grade(average_grades)
    print(f" 5| {student_names_sorted=}")
```

> Each task should be solved in two ways: First, use only basic Python constructs such as loops, conditionals, and basic list/dictionary operations. Second, if you like, follow the hint (see Python docs!) and solve it in a shorter way. If it does not work right now - no problem. We will come back to this particular approach in future lectures.

- `calc_average_grades`: Compute the average grade for each student and store these averages in a separate dictionary.
  - Result: `{'Alice': 85.0, 'Bob': 47.0, 'Charlie': 92.0, 'Diana': 36.0, 'Eve': 64.0}`
  - Hint: Use a 'dictionary comprehension', `sum` and `len`.

- `determine_top_performer`: Determine the name of the student with the highest average grade and the value of that average.
  - Result: `'Charlie', 92.00`
  - Hint: Use `max` with a `key` using `average_grades`.

- `determine_all_students_with_a_fail`: Identify all students who scored below 40 in at least one subject.
  - Result: `['Bob', 'Diana']`
  - Hint: Use a 'conditional list comprehension' and `any`.
- `determine_subjects_everyone_passed`: Find all the subjects in which every student scored at least 40.
  - Result: `['Math']`
  - Hint: Use a 'conditional dictionary comprehension' and `all`. 

- `sort_students_by_average_grade`: Produce a list of student names sorted by their average grades in descending order. Do not use predefined sorting functions in the basic version.
  - Result: `['Charlie', 'Alice', 'Eve', 'Bob', 'Diana']`
  - Hint: Use `sorted` on `average_grades` with a clever `key` and a 'list comprehension' to extract only the students.

Check
- Compare your solution with `buxrose_edge_one_solution.py` in `solutions`. 
  - Is your solution correct and complete? 
  - Do you have any ideas on how to improve your solution?
  - Is there a detail where your solution is better or different? Tell us.

---

### 👉 Task 'Couch Potato' - Recurring homework

- If you did not finish the essential tasks in the exercise, finish them at home.

---

### 👉 Comprehension Check - Talk with your Neighbor

- What are the known primitive data types and containers?
- What are some important differences between containers?
- What is the difference between '==' and 'is'?
- What does 'short-circuiting' mean?
- What is the difference between python-int and ints in other languages?
- What does 'slicing' mean?
- Is copying a list a shallow copy or a deep copy?
- What is the difference between a list and a tuple?
- What are 'frozensets' for?
- What do I need to be aware of with a function's default arguments?

---

### 👉 Lecture Check - Online Questionare

- Please participate in the survey: [Slido](https://wall.sli.do)

---

End of `Unit 0x02`
