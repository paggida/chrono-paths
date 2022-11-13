import os

import pytest
from faker import Faker

from src.domain.argument import Argument

fake = Faker(locale="pt-BR")


class TestArgument:
    @pytest.fixture
    def valid_path(self):
        return os.path.dirname(os.path.abspath(__file__))

    def test_validates_valid_arguments(self, valid_path):
        test_argument_list = ["", "-m", valid_path]
        test_argument = Argument(test_argument_list)

        assert test_argument.is_valid
        assert test_argument.argument_list == test_argument_list[1:]
        assert test_argument.errors == ""
        assert test_argument.is_cut_request
        assert test_argument.path == valid_path

    def test_sets_the_attribute_when_receiving_the_option_to_move_the_files(
        self, valid_path
    ):
        test_argument_with_option = Argument(["", "-m", valid_path])
        test_argument_with_long_option = Argument(["", "--move_files", valid_path])

        assert test_argument_with_option.is_valid
        assert test_argument_with_long_option.is_valid
        assert test_argument_with_option.is_cut_request
        assert test_argument_with_long_option.is_cut_request

    def test_validates_when_path_exist(self, valid_path):
        test_argument = Argument(["", valid_path])

        assert test_argument.is_valid
        assert test_argument.errors == ""
        assert test_argument.path == valid_path

    def test_invalidates_when_path_not_exist(self):
        invalid_path = os.path.dirname(fake.file_path(depth=3))
        test_argument = Argument(["", invalid_path])

        assert not test_argument.is_valid
        assert test_argument.errors == "Path not found."
        assert test_argument.path == invalid_path

    def test_invalidates_when_the_number_of_arguments_is_invalid(self, valid_path):
        test_argument_with_no_arguments = Argument([""])
        invalid_path = os.path.dirname(fake.file_path(depth=3))
        test_argument_with_three_arguments = Argument(
            ["", "-m", valid_path, invalid_path]
        )

        assert not test_argument_with_no_arguments.is_valid
        assert not test_argument_with_three_arguments.is_valid
        assert test_argument_with_no_arguments.errors == "Invalid number of arguments."
        assert (
            test_argument_with_three_arguments.errors == "Invalid number of arguments."
        )

    def test_invalidates_when_receiving_unknown_option_in_arguments(self, valid_path):
        test_argument_with_wrong_option = Argument(["", "-x", valid_path])
        test_argument_with_wrong_long_option = Argument(["", "--cut_files", valid_path])

        assert not test_argument_with_wrong_option.is_valid
        assert not test_argument_with_wrong_long_option.is_valid
        assert not test_argument_with_wrong_option.is_cut_request
        assert not test_argument_with_wrong_long_option.is_cut_request
        assert test_argument_with_wrong_option.errors == "Invalid arguments."
        assert test_argument_with_wrong_long_option.errors == "Invalid arguments."

    def test_invalidates_when_receiving_two_paths_in_arguments(self, valid_path):
        test_argument_with_two_paths = Argument(["", valid_path, valid_path])

        assert not test_argument_with_two_paths.is_valid
        assert test_argument_with_two_paths.errors == "Invalid arguments."
