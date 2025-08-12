from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # all walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # keep taking steps until the walk reaches the desired steps
        while len(self.x_values) < self.num_points:

            # decide which direction to go and how far to go
            x_direction = choice([1, -1]) # 1 is right, -1 is left
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance # pos. is right, neg.is left and 0 is vertical movement

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance # pos. is up, neg.is down and 0 is horizontal movement

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)