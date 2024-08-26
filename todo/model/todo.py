class Todo:
    def __init__(self, code: int, title: str, description: str, completed: False, tag: list[str]):
        self.code: int = code
        self.title: str = title
        self.description: str = description
        self.completed: False = completed
        self.tag: list[str] = tag


