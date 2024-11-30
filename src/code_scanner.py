import json

def scan_code(file_path, rules_file):
    """
    Scans the code for custom rules.
    """
    with open(rules_file, 'r') as rules:
        rules_data = json.load(rules)
    
    issues = []
    with open(file_path, 'r') as code_file:
        code = code_file.readlines()
        for i, line in enumerate(code, start=1):
            for rule in rules_data:
                if rule["pattern"] in line:
                    issues.append({
                        "line": i,
                        "issue": rule["description"],
                        "remediation": rule["remediation"]
                    })
    return issues

if __name__ == "__main__":
    file_to_scan = "sample_code.py"
    print(scan_code(file_to_scan, "rules.json"))

