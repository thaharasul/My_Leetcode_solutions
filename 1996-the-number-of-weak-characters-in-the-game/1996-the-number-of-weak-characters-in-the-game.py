class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
            properties.sort(key=lambda p: (-p[0], p[1]))
            max_defense = 0
            count = 0
            for _, defense in properties:
                if defense < max_defense:
                    count += 1
                else:
                    max_defense = defense
            return count