VALID_SEVERITIES = ["Low", "Medium", "High", "Critical"]

VALID_STATUS = ["Open", "In Progress", "Resolved"]


def validate_vulnerability(data):
    errors = []

    title = data.get("title", "").strip()
    if not title:
        errors.append("Title is required.")

    description = data.get("description", "").strip()
    if not description:
        errors.append("Description is required.")

    severity = data.get("severity", "")
    if severity not in VALID_SEVERITIES:
        errors.append(
            f"Severity must be one of {', '.join(VALID_SEVERITIES)}."
        )

    status = data.get("status", "")
    if status not in VALID_STATUS:
        errors.append(
            f"Status must be one of {', '.join(VALID_STATUS)}."
        )

    reported_by = data.get("reported_by", "").strip()
    if not reported_by:
        errors.append("Reported By is required.")

    return errors