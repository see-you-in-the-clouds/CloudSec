import os

REPORT_FOLDER = "uploads"
os.makedirs(REPORT_FOLDER, exist_ok=True)

def generate_report(json_filename, violations):
    """Generate a .txt report with detailed information on detected issues."""
    report_filename = os.path.splitext(os.path.basename(json_filename))[0] + "_report.txt"
    report_path = os.path.join(REPORT_FOLDER, report_filename)

    with open(report_path, "w") as report:
        if not violations:
            report.write("No issues found! The JSON passed all checks.\n")
        else:
            report.write("Security Issues Found:\n\n")
            for v in violations:
                full_json_path = v.get("field", "Unknown Path")  
                problem_value = v.get("problem_value", "Unknown Value")
                category = v.get("category", "Unknown Category")
                message = v.get("message", "No description available.")
                reference = v.get("reference", "No reference available.")
                next_steps = v.get("next_steps", "No suggested fix.")

                report.write(f"🔹 [{category}] \n")
                report.write(f"   Issue: -> {message}\n")
                report.write(f"   Path: -> {full_json_path}\n")  
                report.write(f"   Value: -> {problem_value}\n")
                report.write(f"   Reference: -> {reference}\n")   
                report.write(f"   Next Steps: -> {next_steps}\n")

    return report_path
