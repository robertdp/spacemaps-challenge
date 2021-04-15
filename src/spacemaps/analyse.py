from heapq import heappop, heappush, heappushpop


# O(limit*log(limit) + rows*log(limit) + limit*log(limit)) => O((2*limit + rows)*log(limit))
def run_analysis(rows, limit):
    heap = []
    while len(heap) < limit:  # O(limit*log(limit))
        try:
            row = next(rows)
            heappush(heap, (row.value, row))  # O(log(limit))
        except StopIteration:
            break
    for row in rows:  # O(rows*log(limit))
        if row.value > heap[0][0]:
            heappushpop(heap, (row.value, row))  # O(log(limit))
    return [heappop(heap)[1] for _ in range(len(heap))]  # O(limit*log(limit))
