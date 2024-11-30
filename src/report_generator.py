import json
import matplotlib.pyplot as plt

def visualize_issues(issues):
    """
    Visualize issues by severity.
    """
    severity_counts = {"low": 0, "medium": 0, "high": 0}
    for issue in issues:
        severity_counts["medium"] += 1  # Example: categorize all as medium

    plt.bar(severity_counts.keys(), severity_counts.values())
    plt.title("Issue Severity")
    plt.show()

if __name__ == "__main__":
    sample_issues = [{"issue": "Avoid eval()", "severity": "medium"}]
    visualize_issues(sample_issues)


def generate_report(issues, output_file):
    """
    Generates a simple JSON report of the issues.
    """
    with open(output_file, 'w') as report:
        json.dump({"issues": issues}, report, indent=4)
    print(f"Report saved to {output_file}")

if __name__ == "__main__":
    sample_issues = [
        {"line": 5, "issue": "Avoid eval()", "remediation": "Use safer alternatives."}
    ]
    generate_report(sample_issues, "report.json")


