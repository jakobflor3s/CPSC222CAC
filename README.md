# CPSC222CAC

A small Python program that shows which resources each user can access through their assigned roles. It models role-based access control (RBAC) with 0/1 matrices and combines them with a Boolean matrix product.

**How it works**

Two matrices describe the setup:

user_role: which roles each user holds
role_resource: which resources each role grants

The program combines them so that a user can access a resource if at least one of their roles grants it. It then prints each user's resources and lists who can access the last resource in the list.

Features
Two built-in test cases (a role ladder, and a user with two roles)
Input validation that raises a ValueError for empty, mismatched, or non-rectangular matrices
Interactive menu for choosing a test case
No dependencies beyond the Python standard library
Requirements
Python 3
