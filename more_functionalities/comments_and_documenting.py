import os
import comments_and_documenting
import imp
r"""
This script create a new empty object
"""


print(comments_and_documenting.__doc__)

imp.reload(comments_and_documenting)

filename = "sample.txt"

# Create empty file


def create_file():
    """This function create a new empty object"""


with open(filename, "w") as file:
    file.write("")  # writing empty string
