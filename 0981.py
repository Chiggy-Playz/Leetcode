from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.data: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:

        result = ""
        values = self.data[key]

        l = 0
        r = len(values) - 1
        while l <= r:
            mid = (l + r) // 2

            if values[mid][0] <= timestamp:
                l = mid + 1
                result = values[mid][1]
            else:
                r = mid - 1

        return result


timeMap = TimeMap()
print(timeMap.set("foo", "bar", 1))
print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))
print(timeMap.set("foo", "bar2", 4))
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))
