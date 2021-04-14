from collections import deque


def run_analysis(rows, limit):
    initial = deque([], limit)
    for _ in range(limit):
        try:
            initial.append(next(rows))
        except StopIteration:
            break
    q = deque(sorted(initial, key=lambda row: row.value), limit)
    for row in rows:
        if row.value > q[0].value:
            q.popleft()
            for index in range(0, limit):
                if index == limit - 1:
                    q.append(row)
                    break
                elif row.value < q[index].value:
                    q.insert(index, row)
                    break
    q.reverse()
    return q
