class GroupSizeExceededException(Exception):
    def __init__(self, message="Group size exceeds the maximum limit"):
        self.message = message
        super().__init__(self.message)