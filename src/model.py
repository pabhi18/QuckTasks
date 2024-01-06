class Todo:
    def __init__(self, task, category, status=None, position = None):
        self.task = task
        self.category = category
        self.status = status if status is not None else 1
        self.position = position if position is not None else None

    def __str__(self):
        return f"({self.task}, {self.category}, {self.status}, {self.position})"