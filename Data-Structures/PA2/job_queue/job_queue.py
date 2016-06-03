# python3
import queue

class JobQueue:
    def __init__(self):
        self.assigned_workers = queue.PriorityQueue()
        self.start_times = queue.PriorityQueue()

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        # self.assigned_workers = [None] * len(self.jobs)
        # self.start_times = [None] * len(self.jobs)
        # next_free_time = [0] * self.num_workers
        # for i in range(len(self.jobs)):
        #   next_worker = 0
        #   for j in range(self.num_workers):
        #     if next_free_time[j] < next_free_time[next_worker]:
        #       next_worker = j
        #   self.assigned_workers[i] = next_worker
        #   self.start_times[i] = next_free_time[next_worker]
        #   next_free_time[next_worker] += self.jobs[i]

        # Fill the PriorityQueue for assigned_workers
        for i in range(self.num_workers):
            self.assigned_workers.put(( 0, i))

        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = self.assigned_workers.get()
          # Faster solution : print it right now (don't use start_times)
          print(next_worker[1], next_worker[0])
          # Put it back on the queue
          endtime = next_worker[0] + self.jobs[i]
          self.assigned_workers.put(( endtime, next_worker[1]))

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()