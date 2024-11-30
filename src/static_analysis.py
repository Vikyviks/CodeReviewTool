import subprocess

def analyze_code(file_path):
    """
    Run static analysis using Bandit and return the results.
    """
    try:
        result = subprocess.run(
            ['bandit', '-r', file_path, '-f', 'json'], 
            capture_output=True, 
            text=True
        )
        return result.stdout
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    file_to_scan = "sample_code.py"  # Replace with your test file
    print(analyze_code(file_to_scan))

