from collections import deque


def run_analysis(rows, limit):
    initial = [next(rows) for _ in range(limit)]
    initial.sort(key=lambda row: row.value)
    q = deque(initial, limit)
    for row in rows:
        if row.value > q[0].value:
            for index in range(1, limit):
                if row.value < q[index].value:
                    q.popleft()
                    q.insert(index-1, row)
                    break
    q.reverse()
    return q
