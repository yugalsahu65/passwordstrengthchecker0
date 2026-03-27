import re
def check_strength(password):
    score = 0
    tips = []

    checks = [
        (len(password) >= 8,                       "At least 8 characters"),
        (len(password) >= 12,                      "At least 12 characters"),
        (bool(re.search(r"[A-Z]", password)),      "Uppercase letter (A-Z)"),
        (bool(re.search(r"[a-z]", password)),      "Lowercase letter (a-z)"),
        (bool(re.search(r"\d", password)),         "Digit (0-9)"),
        (bool(re.search(r"[!@#$%^&*]", password)),"Special character (!@#$%^&*)"),
        (not re.search(r"(.)\1{2,}", password),    "No repeated chars (aaa)"),
    ]

    print("\n--- Checklist ---")
    for passed, desc in checks:
        print(f"  {'✔' if passed else '✘'}  {desc}")
        if passed:
            score += 1
        else:
            tips.append(desc)

    percent = round(score / len(checks) * 100)

    if percent >= 85:   label = "Very Strong 💪"
    elif percent >= 65: label = "Strong 👍"
    elif percent >= 45: label = "Moderate ⚠️"
    elif percent >= 25: label = "Weak 😟"
    else:               label = "Very Weak 🚨"

    bar = "█" * (percent // 5) + "░" * (20 - percent // 5)
    print(f"\nScore : {percent}/100  [{bar}]")
    print(f"Level : {label}")

    if tips:
        print("\nTips to improve:")
        for tip in tips:
            print(f"  → Add: {tip}")

print("=== Password Strength Checker ===")
while True:
    pwd = input("\nEnter password (or 'q' to quit): ")
    if pwd.lower() == 'q':
        break
    check_strength(pwd)