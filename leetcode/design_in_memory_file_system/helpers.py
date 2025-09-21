def run_file_system(solution_class: type, operations: list[str], inputs: list[list]):
    from typing import Any

    fs: Any = None
    results: list[str | list[str] | None] = []
    for i, operation in enumerate(operations):
        if operation == "FileSystem":
            fs = solution_class()
            results.append(None)
        elif operation == "ls":
            assert fs is not None
            result = fs.ls(inputs[i][0])
            results.append(result)
        elif operation == "mkdir":
            assert fs is not None
            fs.mkdir(inputs[i][0])
            results.append(None)
        elif operation == "addContentToFile":
            assert fs is not None
            fs.add_content_to_file(inputs[i][0], inputs[i][1])
            results.append(None)
        elif operation == "readContentFromFile":
            assert fs is not None
            result = fs.read_content_from_file(inputs[i][0])
            results.append(result)
    return results, fs


def assert_file_system(
    result: list[str | list[str] | None], expected: list[str | list[str] | None]
) -> bool:
    assert result == expected
    return True
