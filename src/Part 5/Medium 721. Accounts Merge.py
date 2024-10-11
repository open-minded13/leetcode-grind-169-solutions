from typing import List

# Date of Last Practice: Dec 27, 2023 -> Feb 7, 2024 -> Feb 15, 2024
#
# Time Complexity: O(A * E) + O(N * log N), where A is the number of accounts,
#                  E is the average number of emails per account, and
#                  N is the total number of unique email addresses across all accounts.
#
#                  In step 1, iterating over each account and then over each email in the account
#                  results in A * E time, where A is the number of accounts and
#                  E is the average number of emails per account.
#
#                  For each email, a union operation is performed within the nested loop.
#                  The time complexity of union and find operations in a DSU is O(α(N)),
#                  where α(N) is the Inverse Ackermann function, which grows very slowly.
#                  So, for A * E emails, this step takes O(A * E * α(N)).
#                  Since α(N) is practically a constant for reasonably large input,
#                  we can approximate this to O(A * E).
#
#                  In step 2, iterating over all unique emails and finding parents in DSU is
#                  O(N * α(N)), which is approximately O(N).
#
#                  In step 3, the sorting of emails in each group dominates this step.
#                  In the worst case, all unique emails could belong to a single group,
#                  resulting in a sorting time of O(N log N).
#
#                  So, the overall time complexity is O(A * E) + O(N) + O(N log N) =
#                  O(A * E) + O(N * log N).
#
#                  In the worst-case scenario, all emails are unique and there are
#                  no duplicate emails across any accounts, resulting N = A * E.
#                  Therefore, O(N * log N).
#
# Space Complexity: O(N), where N is the total number of unique emails across all accounts.
#
#                   1) The DSU class uses a dictionary for parents,
#                      which can have at most N entries (one per email), so O(N).
#
#                   2) Both email_to_name and email_to_id dictionaries
#                      will have an entry per email, requiring O(N) space.
#
#                   3) The result dictionary and the list used for the final result
#                      will also use O(N) space.


class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            # Note it is self.parent[px], not self.parent[x]!
            self.parent[px] = py


class Solution:
    def accountsMerge(self, accounts):
        dsu = DSU()
        email_to_name = {}
        email_to_id = {}
        id = 0

        # Step 1: Map each email to its owner and give each email a unique ID
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                if email not in email_to_id:
                    email_to_id[email] = id
                    id += 1
                dsu.union(email_to_id[account[1]], email_to_id[email])

        # Step 2: Use Union-Find to group emails
        result = {}
        for email in email_to_name:
            parent_id = dsu.find(email_to_id[email])
            result.setdefault(parent_id, []).append(email)

        # Step 3: Collect and sort emails for each account
        return [
            [email_to_name[emails[0]]] + sorted(emails) for emails in result.values()
        ]


class First_Inefficient_Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        i = 0
        while i < len(accounts):
            j = 0
            is_merged = False
            while j < len(accounts):
                if j == i:
                    j += 1
                    continue
                name = accounts[i][0]
                account_set = set(accounts[i][1:])
                if accounts[j][0] == name:
                    check_set = set(accounts[j][1:])
                    if account_set.intersection(check_set):
                        accounts[i] = [name] + list(account_set.union(check_set))
                        del accounts[j]
                        j -= 1
                        is_merged = True
                j += 1

            accounts[i][1:] = list(set(accounts[i][1:]))

            # accounts[i][1:].sort()
            accounts[i][1:] = sorted(accounts[i][1:])
            if not is_merged:
                i += 1

        return accounts


# Test cases
def main():
    solution = Solution()

    # Test Case 1: Basic Case
    accounts1 = [["Alice", "alice@mail.com"], ["Bob", "bob@mail.com"]]
    print("Test Case 1:", solution.accountsMerge(accounts1))

    # Test Case 2: Single User Multiple Accounts
    accounts2 = [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ]
    print("Test Case 2:", solution.accountsMerge(accounts2))

    # Test Case 3: Multiple Users with Same Name
    accounts3 = [["John", "johnsmith@mail.com"], ["John", "johnnybravo@mail.com"]]
    print("Test Case 3:", solution.accountsMerge(accounts3))

    # Test Case 4: Complex Case with Multiple Merges
    accounts4 = [
        ["John", "john00@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["Mary", "marynewyork@mail.com", "mary@mail.com"],
    ]
    print("Test Case 4:", solution.accountsMerge(accounts4))

    # Test Case 5: No Accounts
    accounts5 = []
    print("Test Case 5:", solution.accountsMerge(accounts5))

    # Test Case 6: Single Account with Multiple Emails
    accounts6 = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com", "john00@mail.com"]
    ]
    print("Test Case 6:", solution.accountsMerge(accounts6))


if __name__ == "__main__":
    main()
