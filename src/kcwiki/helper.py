import re


def filter_text(text, rules):
    filtered_text = text
    for rule in rules:
        regex, replacement = rule
        filtered_text = re.sub(regex, replacement, filtered_text)
    return filtered_text
