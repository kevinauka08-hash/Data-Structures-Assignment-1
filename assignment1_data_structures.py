"""
Assignment 1 – Task 1
Data Structure Classification
Student Example Version

This program demonstrates:
1. Primitive Data Structures
2. Linear Data Structures
3. Non-Linear Data Structures

All examples are personalized using student-life scenarios.
"""

# =====================================================
# 1️⃣ PRIMITIVE DATA STRUCTURES
# =====================================================

print("----- PRIMITIVE DATA STRUCTURES -----")

# Integer
student_age = 19

# Float
assignment_mark = 88.5

# String
student_name = "Thabo Mokoena"

# Boolean
is_assignment_submitted = True

print("Name:", student_name)
print("Age:", student_age)
print("Mark:", assignment_mark)
print("Submitted:", is_assignment_submitted)


# =====================================================
# 2️⃣ NON-PRIMITIVE DATA STRUCTURES
# =====================================================

# -----------------------------------------------------
# A. LINEAR DATA STRUCTURES
# -----------------------------------------------------

print("\n----- LINEAR DATA STRUCTURES -----")

# 1. Array (Python List)
# Example: List of registered modules

modules = ["Data Structures", "Mathematics", "Programming", "Networking"]

print("\nModules Registered:")
for module in modules:
    print("-", module)

# 2. Linked List
# Example: Study topics connected in order

class Topic:
    def __init__(self, topic_name):
        self.topic_name = topic_name
        self.next = None

print("\nLinked List of Study Topics:")

topic1 = Topic("Arrays")
topic2 = Topic("Stacks")
topic3 = Topic("Queues")

topic1.next = topic2
topic2.next = topic3

current = topic1
while current:
    print("-", current.topic_name)
    current = current.next

# 3. Stack (LIFO)
# Example: Recently opened study materials

print("\nStack Example (Recently Opened Notes):")

study_stack = []

study_stack.append("Chapter 1 Notes")
study_stack.append("Chapter 2 Notes")
study_stack.append("Chapter 3 Notes")

study_stack.pop()  # Last opened removed first

print("Remaining Notes:", study_stack)

# 4. Queue (FIFO)
# Example: Students waiting to present

from collections import deque

print("\nQueue Example (Presentation Order):")

presentation_queue = deque()

presentation_queue.append("Thabo")
presentation_queue.append("Lerato")
presentation_queue.append("Sipho")

presentation_queue.popleft()  # First student presents first

print("Next Students:", list(presentation_queue))


# -----------------------------------------------------
# B. NON-LINEAR DATA STRUCTURES
# -----------------------------------------------------

print("\n----- NON-LINEAR DATA STRUCTURES -----")

# 1. Tree (Binary Tree)
# Example: Course prerequisite structure

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.left = None
        self.right = None

print("\nTree Example (Course Structure):")

root = Course("Programming Fundamentals")
root.left = Course("Data Structures")
root.right = Course("Web Development")

print("Main Course:", root.course_name)
print("Next Level Courses:", root.left.course_name, "and", root.right.course_name)

# 2. Graph
# Example: Study group friendships

print("\nGraph Example (Study Group Connections):")

study_group = {
    "Thabo": ["Lerato", "Sipho"],
    "Lerato": ["Thabo", "Aisha"],
    "Sipho": ["Thabo"],
    "Aisha": ["Lerato"]
}

for student, friends in study_group.items():
    print(student, "is connected to", friends)
