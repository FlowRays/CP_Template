import os

def escape_double_quotes(text: str) -> str:
    return text.replace('\\', '\\\\').replace('"', '\\"')

def parse_vscode(description: str, tabtrigger: str, snippet: str) -> str:
    # Escape \" and split lines by line-break
    separated_snippet = escape_double_quotes(snippet).split("\n")
    separated_snippet_length = len(separated_snippet)

    # Add double quotes around each line apart from the last one
    new_snippet = ['            "{}"'.format(line) if i == separated_snippet_length - 1 else '            "{}"'.format(line) for i, line in enumerate(separated_snippet)]

    # Format the output as a JSON-like string (similar to the JavaScript template literal)
    formatted_output = """    "{description}": {{
        "prefix": "{tabtrigger}",
        "body": [
{snippet}
        ],
        "description": "{description}"
    }}""".format(
        description=description,
        tabtrigger=tabtrigger,
        snippet=',\n'.join(new_snippet),
    )

    return formatted_output

def parse_file(file_path: str):
    flag_description = False
    flag_tabtrigger = False
    flag_snippet_begin = False
    description = ""
    tabtrigger = ""
    snippet = ""
    with open(file_path,'r',encoding='utf-8') as fp:
        for line in fp.readlines():
            line = line.strip('\n')
            if line == "```": 
                break
            if flag_description:
                description = line
                flag_description = False
            elif flag_tabtrigger:
                tabtrigger = line
                flag_tabtrigger = False
            elif flag_snippet_begin:
                snippet += line + "\n"
            if line == "# description":
                flag_description = True
            elif line == "# tabtrigger":
                flag_tabtrigger = True
            elif line == "```cpp":
                flag_snippet_begin = True
    return parse_vscode(description,tabtrigger,snippet)

with open('cpp.json','w',encoding='utf-8') as fp:
    fp.write('{\n')
    for root, dirs, files in os.walk('template'):
        for file in files:
            if file.endswith('.md'):
                fp.write(parse_file(os.path.join(root, file))+',\n')
    fp.write('}')

