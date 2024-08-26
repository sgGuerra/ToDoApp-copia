class Todo:
    def __init__(self, code_id: int, title: str, description: str, completed: False, tags: list[str]):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: False = completed
        self.tags: list[str] = tags

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag) -> str | list:
        if tag in self.tags:
            return f"el elemteno {tag} ya esta exite en la lista"

        else:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self.code_id}-{self.title}"



