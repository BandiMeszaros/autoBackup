class DirectoryInitError(Exception):
    def __init__(self, loc):
        self.message = f"Couldn't create directory {loc}"
        super().__init__(self.message)


class FileCreationError(Exception):
    def __init__(self, loc):
        self.message = f"Couldn't create file at {loc}"
        super().__init__(self.message)


class LocationNotFoundError(Exception):
    def __init__(self, loc):
        self.message = f" Backup location {loc} not found"
        super().__init__(self.message)
