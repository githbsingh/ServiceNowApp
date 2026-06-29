import re

SECTION_PATTERN = re.compile(
    r"^\d+\.\s+[A-Z\s]+$"
)
def split_by_section(text):

    sections = {}

    current_section = "GENERAL"

    lines = text.split("\n")

    buffer = []

    for line in lines:

        line = line.strip()

        if SECTION_PATTERN.match(line):

            sections[current_section] = "\n".join(
                buffer
            )

            current_section = line

            buffer = []

        else:
            buffer.append(line)

    sections[current_section] = "\n".join(
        buffer
    )

    return sections