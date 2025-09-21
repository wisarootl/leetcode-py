class FileSystem:

    # Time: O(1)
    # Space: O(1)
    def __init__(self) -> None:
        self.files: dict[str, str] = {}  # path -> content
        self.dirs: set[str] = set()  # set of directory paths

    # Time: O(N + M + K log K) where N = files, M = dirs, K = items in result
    # Space: O(K) for result set and sorting
    def ls(self, path: str) -> list[str]:
        if path in self.files:
            return [path.split("/")[-1]]

        items = set()
        prefix = path + "/" if path != "/" else "/"

        for file_path in self.files:
            if file_path.startswith(prefix):
                remaining = file_path[len(prefix) :]
                if remaining and "/" not in remaining:
                    items.add(remaining)
                elif remaining and "/" in remaining:
                    items.add(remaining.split("/")[0])

        for dir_path in self.dirs:
            if dir_path.startswith(prefix):
                remaining = dir_path[len(prefix) :]
                if remaining and "/" not in remaining:
                    items.add(remaining)
                elif remaining and "/" in remaining:
                    items.add(remaining.split("/")[0])

        return sorted(items)

    # Time: O(D) where D = depth of path
    # Space: O(D) for path parts and directory storage
    def mkdir(self, path: str) -> None:
        parts = path.split("/")
        for i in range(1, len(parts) + 1):
            dir_path = "/".join(parts[:i])
            if dir_path:
                self.dirs.add(dir_path)

    # Time: O(D + C) where D = depth of path, C = content length
    # Space: O(D + C) for path parts and content storage
    def add_content_to_file(self, file_path: str, content: str) -> None:
        parts = file_path.split("/")
        for i in range(1, len(parts)):
            dir_path = "/".join(parts[:i])
            if dir_path:
                self.dirs.add(dir_path)

        self.files[file_path] = self.files.get(file_path, "") + content

    # Time: O(1)
    # Space: O(1)
    def read_content_from_file(self, file_path: str) -> str:
        return self.files.get(file_path, "")
