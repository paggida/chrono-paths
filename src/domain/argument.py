import os


class Argument(object):
    def __init__(self, arguments):
        self.argument_list: list[str] = arguments[1:]
        self.errors: str = ""
        self.is_cut_request: bool = False
        self.path: str = ""
        self._validate()
        self.is_valid: bool = self.errors == ""

    def _is_valid_arguments(self):
        if not 0 < len(self.argument_list) < 3:
            self.errors = "Invalid number of arguments."
            return False

        for currentArgument in self.argument_list:
            if currentArgument.upper() in ["-M", "--MOVE_FILES"]:
                self.is_cut_request = True
            else:
                if self.path != "":
                    self.errors = "Invalid arguments."
                    return False
                self.path = currentArgument

        return True

    def _is_valid_path(self):
        if not os.path.isdir(self.path):
            self.errors = "Path not found."

    def _validate(self):
        is_valid_arguments = self._is_valid_arguments()

        if is_valid_arguments:
            self._is_valid_path()
