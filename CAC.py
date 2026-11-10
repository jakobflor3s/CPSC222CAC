"""A minimal role-based access-control example.

Question: which resources can each user access through assigned roles?
"""


def compose_relations(user_role, role_resource):
    """Compose relations using Boolean matrix multiplication (OR of ANDs)."""
    if not user_role or not role_resource:
        raise ValueError("Relation matrices must not be empty")
    if len(user_role[0]) != len(role_resource):
        raise ValueError("The number of roles must match in both relations")
    if any(len(row) != len(user_role[0]) for row in user_role):
        raise ValueError("User-role matrix must be rectangular")
    if any(len(row) != len(role_resource[0]) for row in role_resource):
        raise ValueError("Role-resource matrix must be rectangular")

    return [
        [int(any(user_role[u][r] and role_resource[r][item]
                 for r in range(len(role_resource))))
         for item in range(len(role_resource[0]))]
        for u in range(len(user_role))
    ]


def display_case(title, users, resources, user_role, role_resource):
    print(f"\n{title}")
    user_resource = compose_relations(user_role, role_resource)
    for user, access_row in zip(users, user_resource):
        permitted = [resource for resource, bit in zip(resources, access_row) if bit]
        print(f"  {user}: {', '.join(permitted) or 'none'}")

    target = resources[-1]
    target_column = resources.index(target)
    readers = [user for user, row in zip(users, user_resource) if row[target_column]]
    print(f"Who can access {target}? {', '.join(readers) or 'no one'}")


def first_case():
    users = ["Ava", "Ben", "Crystal"]
    roles = ["Analyst", "Operator", "Admin"]
    resources = ["Reports", "Servers", "Audit Logs"]
    user_role = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    role_resource = [
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 1],
    ]
    display_case("First case", users, resources, user_role, role_resource)


def second_case():
    users = ["Darius", "Equon", "Fabian", "Geoffrey"]
    roles = ["Viewer", "Editor", "Manager"]
    resources = ["Blog Posts", "Analytics", "Customer Data", "Billing"]
    user_role = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 0],
    ]
    role_resource = [
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
    ]
    display_case("Second case", users, resources, user_role, role_resource)


while True:
    print("Choose a test case: 1 for the first case, 2 for the second case, 3 to exit")
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        first_case()
    elif choice == "2":
        second_case()
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


