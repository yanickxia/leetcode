from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        companies_map = {}
        orders = 1
        new_favoriteCompanies = []
        for i in range(len(favoriteCompanies)):
            new_favoriteCompany = []
            favoriteCompany = favoriteCompanies[i]
            for company in favoriteCompany:
                if company not in companies_map:
                    companies_map[company] = orders
                    orders += 1
                new_favoriteCompany.append(companies_map[company])
            new_favoriteCompanies.append(set(new_favoriteCompany))

        return new_favoriteCompanies


if __name__ == '__main__':
    s = Solution()
    print(s.peopleIndexes(
        [
            ["leetcode", "google", "facebook"],
            ["google", "microsoft"],
            ["google", "facebook"],
            ["google"],
            ["amazon"]]))
