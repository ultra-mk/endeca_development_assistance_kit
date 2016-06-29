import os


def check_for_file(file_path):
	return os.path.isfile(file_path)


def open_file_split_into_lines(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
        return lines
