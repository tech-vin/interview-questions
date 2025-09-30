import json

def get_abbrev_from_json(json_str):
    """
    Interview Question (Wipro):
    --------------------------
    Convert a JSON string into a Python dictionary and extract the value
    of the key "Abbrev".

    Example Input (JSON string):
    {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"]
                        },
                        "GlossSee": "markup"
                    }
                }
            }
        }
    }

    Expected Output:
        "ISO 8879:1986"

    Args:
        json_str (str): JSON formatted string.

    Returns:
        str: Value of the "Abbrev" key, or None if not found.

    Complexity:
        Time: O(n) for parsing JSON (n = size of string).
        Space: O(n) for Python dict representation.
    """
    try:
        # Convert JSON string to dict
        data = json.loads(json_str)

        # Navigate to the nested key
        return data["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["Abbrev"]

    except (KeyError, json.JSONDecodeError):
        # In case "Abbrev" is missing or JSON invalid
        return None


# -------------------
# Demo
# -------------------
if __name__ == "__main__":
    json_str = """
    {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"]
                        },
                        "GlossSee": "markup"
                    }
                }
            }
        }
    }
    """
    print("Abbrev:", get_abbrev_from_json(json_str))