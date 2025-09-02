from typing import List
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #count frequency of each task
        task_count = Counter(tasks)

        # Find the maximum frequency among all tasks
        max_frequency = max(task_count.values())

        num_max_frequency_tasks = sum(1 for count in task_count.values() if count == max_frequency)

        min_time = max(len(tasks), (max_frequency - 1) * (n + 1) + num_max_frequency_tasks)
      
        return min_time
