from tool.runners.python import SubmissionPy


class MaximeSubmission(SubmissionPy):

    def run(self, s):
        lines = s.strip().split("\n")
        seats = set()
        for line in lines:
            seat = 0
            for char in line:
                seat *= 2
                if char in ["B", "R"]:
                    seat += 1
            seats.add(seat)
        return set(range(min(seats), max(seats) + 1)).difference(seats).pop()
