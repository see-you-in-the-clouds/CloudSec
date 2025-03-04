import json
import re

# Load security rules from JSON file
def load_rules():
    """Load security rules from JSON file."""
    try:
        with open("rules.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
# "Lineup" the rules and the user JSON
def validate_json(json_data):
    """Check JSON against security rules and return violations."""
    violations = []
    rules = load_rules()
    search_json(json_data, rules, violations, [])
    return violations

def search_json(data, rules, violations, path):
    """Recursively check JSON fields against rules."""
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = path + [key]
            field_path = ".".join(new_path)

            for rule in rules:
                if re.match(rule["field"], field_path) and rule_applies(value, rule):
                    violations.append(build_violation(field_path, rule, value))

                if "nested_field" in rule and rule["field"] == key:
                    if isinstance(data, dict) and rule["nested_field"] in data:
                        nested_value = data[rule["nested_field"]]
                        if not re.match(rule["nested_value"], str(nested_value)):
                            violations.append(build_violation(field_path + "." + rule["nested_field"], rule, nested_value))

            search_json(value, rules, violations, new_path)
# Comparision elements logic to compare the rules and the user JSON
    elif isinstance(data, list):  
        for i, item in enumerate(data):
            search_json(item, rules, violations, path + [str(i)])

# gathering values to append
def build_violation(field_path, rule, value):
    """Create a violation entry with strict path enforcement."""
    return {
        "field": field_path,
        "problem_value": str(value),
        "category": rule["category"],
        "message": rule["message"],
        "reference": rule["reference"],
        "next_steps": rule["next_steps"]
    }
# operator logic to compare the rules and the user JSON
def rule_applies(value, rule):
    """Check if a rule applies to a given value."""
    if rule["condition"] == "equals":
        return value == rule["value"]
    if rule["condition"] == "contains":
        return isinstance(value, (str, list)) and rule["value"] in value
    if rule["condition"] == "not_matches":
        return isinstance(value, str) and not re.match(rule["value"], value)
    if rule["condition"] == "matches":
        return isinstance(value, str) and re.match(rule["value"], value)
    if rule["condition"] == "type":
        return isinstance(value, rule["value"])
    return False
