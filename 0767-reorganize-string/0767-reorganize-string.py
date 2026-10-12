class Solution:
    def reorganizeString(self, s: str) -> str:
        
            counts = Counter(s)
            if max(counts.values()) > (len(s) + 1) // 2:
                return ''
            heap = [(-freq, ch) for ch, freq in counts.items()]
            heapq.heapify(heap)
            result = []
            prev = None
            while heap:
                freq, ch = heapq.heappop(heap)
                result.append(ch)
                if prev and prev[0] < 0:
                    heapq.heappush(heap, prev)
                freq += 1
                prev = (freq, ch)
            return ''.join(result)