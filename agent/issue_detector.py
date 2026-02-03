def detect_issues(row):
    issues = []

    if row["CTR"] < 0.01:
        issues.append("Low CTR")

    if row["CPA"] > 300:
        issues.append("High CPA")

    if row["CPC"] > 30:
        issues.append("High CPC")

    return issues
