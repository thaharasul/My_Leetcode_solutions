class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        
      
        graph = defaultdict(list)

        for departure, arrival in sorted(tickets, reverse=True):
            graph[departure].append(arrival)

        st = ["JFK"]
        new_itinerary = []

        while st:
           
            if graph[st[-1]]:
                st.append(graph[st[-1]].pop())
            else:
              
                new_itinerary.append(st.pop())

       
        return new_itinerary[::-1]