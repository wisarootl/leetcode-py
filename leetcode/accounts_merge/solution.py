class Solution:
    # Time: O(N * M) where N is accounts, M is max emails per account
    # Space: O(N * M)
    def accounts_merge(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_accounts: dict[str, list[int]] = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_to_accounts:
                    email_to_accounts[email] = []
                email_to_accounts[email].append(i)

        visited: set[int] = set()
        result = []

        def dfs(account_idx: int, emails: set[str]) -> None:
            if account_idx in visited:
                return
            visited.add(account_idx)

            for email in accounts[account_idx][1:]:
                emails.add(email)
                for neighbor_idx in email_to_accounts[email]:
                    dfs(neighbor_idx, emails)

        for i in range(len(accounts)):
            if i in visited:
                continue

            emails: set[str] = set()
            dfs(i, emails)
            result.append([accounts[i][0]] + sorted(emails))

        return result
