import regex as rex
_not_allowed_chars_db = "^[\w_]"

def _ValidateJson(input):
    if rex.findall(input)