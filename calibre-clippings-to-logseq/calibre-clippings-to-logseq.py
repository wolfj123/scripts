from datetime import datetime
import sys

class Clipping:
    def __init__(self, book_title, author, page, location_start, location_end, date, text, note):
        self.book_title = book_title
        self.author = author
        self.page = page
        self.location_start = location_start
        self.location_end = location_end
        self.date = date
        self.text = text
        self.note = note

def find_clipping_by_location_end(clippings, location_end):
    """Finds the first clipping in the list with a matching location_end.

    Args:
        clippings: A list of Clipping objects.
        location_end: The location_end value to search for.

    Returns:
        The first Clipping object that has the matching location_end, 
        or None if no clipping is found.
    """
    for clipping in clippings:
            if clipping.location_end == location_end:
                return clipping
    return None

def parse_highlight_file(filename):
    clippings = []
    current_book = None
    current_author = None
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespaces

            # Extract book information (if present)
            if line and not line.startswith("-"):
                parts = line.split("(")
                current_book = parts[0].strip()
                current_author = parts[1].strip()[:-1]  # Remove closing parenthesis

            # Extract highlight data
            elif line.startswith("-"):
                is_note = False
                data_parts = line.split("|")
                page = int(data_parts[0].split()[-1])  # Extract page number
                # print(f"page:\n{page}")
                if line.count('-') > 1:
                    location_data = data_parts[1].split("location ")[1].split("-")
                    location_start = int(location_data[0])
                    location_end = int(location_data[1])
                    # print(f"location_start:\n{location_start}")
                    # print(f"location_end:\n{location_end}")
                else:
                    is_note = True
                    location_data = data_parts[1].split("location ")[1]
                    location_start = int(location_data)
                    location_end = location_start
                    # print(f"note data:\n{location_data}")
                    # print(f"note location:\n{location_start}")
                date_string = data_parts[2].split("Added on ")[-1].strip()
                date = datetime.strptime(date_string, "%A, %d %B %Y %H:%M:%S")

                # Extract text after separator
                text = ""
                next_line = next(file).strip()
                while next_line != "==========":
                    text += next_line + "\n"
                    next_line = next(file).strip()

                # Create clipping object and add to list
                if not is_note:
                    clipping = Clipping(current_book, current_author, page, location_start, location_end, date, text.strip(), "")
                    clippings.append(clipping)
                else:
                    relevant_clipping = find_clipping_by_location_end(clippings, location_end)
                    if relevant_clipping:
                        relevant_clipping.note = text.strip()
                    else:
                         print(location_end)

    return clippings

# MAIN
args = sys.argv.copy()
args.pop(0)

clippings_file_name = "test.txt"
output_file_name = clippings_file_name + 'logseq.md'

clippings = parse_highlight_file(clippings_file_name)

for clipping in clippings:
    print(f"Book: {clipping.book_title} by {clipping.author}")
    print(f"Page: {clipping.page}, Location: {clipping.location_start} - {clipping.location_end}")
    print(f"Date Added: {clipping.date}")
    print(f"Text:\n{clipping.text}")
    print(f"Note:\n{clipping.note}")
    print("----------")