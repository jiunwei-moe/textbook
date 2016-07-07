import sys
import os.path

def render_table(table, indent_level):
    """ Returns a Pandoc grid table representation of the given table. """
    result = ""
    num_columns = max(len(row) for row in table)
    column_max_widths = [0] * num_columns
    for row in table:
        for column_index in range(len(row)):
            column_width = max(len(l) for l in row[column_index].splitlines())
            if column_width > column_max_widths[column_index]:
                column_max_widths[column_index] = column_width
    for row_index in range(len(table)):
        row = table[row_index]
        result += ("    " * indent_level) + "+" + "+".join(("=" if row_index == 1 else "-") * (width + 2) for width in column_max_widths) + "+\n"
        split_row = [cell.splitlines() for cell in row]
        max_lines = max(len(split_cell) for split_cell in split_row)
        for line_index in range(max_lines):
            result += ("    " * indent_level)
            for column_index in range(num_columns):
                fmt = "{0:" + str(column_max_widths[column_index]) + "}"
                value_to_print = ""
                if column_index < len(row) and line_index < len(split_row[column_index]):
                    value_to_print = split_row[column_index][line_index]
                result += "| " + fmt.format(value_to_print) + " "
            result += "|\n"
    result += ("    " * indent_level) + "+" + "+".join("-" * (width + 2) for width in column_max_widths) + "+\n"
    return result

lines = open(sys.argv[1], "r", encoding="utf-8").readlines()

# Transform HTML-style tables to Pandoc-compatible multi-line grid tables
code_mode = False
table_mode = False
current_cell = ""
current_row = []
current_table = []
table_indent = 0

while len(lines) > 0:

    line = lines[0]
    lines = lines[1:]

    if line.strip().startswith("```"):
        # Code block delimiter
        code_mode = not code_mode
        if table_mode:
            continue

    elif line.startswith("^"):
        # Processing command
        args = line[1:].split()
        command = args[0]
        args = args[1:]

        if command == "table":
            table_mode = True
            current_row = []
            current_table = []
            if len(args) > 0 and args[0].isdigit():
                table_indent = int(args[0])
            else:
                table_indent = 0
        if command == "/table" or command == "tr" or command == "td":
            if current_cell != "":
                current_row += [current_cell]
                current_cell = ""
        if command == "/table" or command == "tr":
            if len(current_row) != 0:
                current_table += [current_row]
                current_row = []
        if command == "/table":
            if len(current_table) != 0:
                sys.stdout.buffer.write(render_table(current_table, table_indent).encode("utf-8"))
            table_mode = False
        if command == "include":
            lines = open(os.path.join(os.path.dirname(sys.argv[1]),
                args[0]), "r", encoding="utf-8").readlines() + lines
        if command == "program":
            if len(args) > 1 and args[1].isdigit():
                program_indent = int(args[1])
            else:
                program_indent = 0
            source = open(os.path.join(os.path.dirname(sys.argv[1]),
                "programs", args[0]), "r", encoding="utf-8").readlines()
            lines_to_add = [
                "<div class=\"program\">\n",
                "\n",
                "##### Program: `" + args[0] + "`\n",
                "\n",
                "<div class=\"numbers\">\n",
                "```\n"
            ]
            lines_to_add += [ str(i) + "\n" for i in range(1, len(source)+1) ]
            lines_to_add += [
                "```\n",
                "</div>\n",
                "```python\n"
            ]
            lines_to_add += source
            lines_to_add += [
                "```\n",
                "\n",
                "</div>\n"
            ]
            lines = [ ("    " * program_indent) + l for l in lines_to_add ] + lines
        continue

    else:
        # Normal Markdown
        if table_mode:
            if code_mode:
                line = "`" + line.rstrip("\n") + "`\\\n"
            current_cell += line
            continue

    sys.stdout.buffer.write(line.encode("utf-8"))

