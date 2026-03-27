# 🔐 Password Strength Checker

A simple command-line tool built in Python that evaluates the strength of a password based on multiple security rules and gives instant feedback with a score, strength label, progress bar, and improvement tips.

---

## 📌 Project Info

| Field | Details |
|---|---|
| **Language** | Python 3.x |
| **Library Used** | `re` (built-in) |
| **Type** | Command-Line Application |

---

## 🚀 How to Run

**Step 1 — Make sure Python is installed:**
```bash
python --version
```

**Step 2 — Run the program:**
```bash
python password_checker.py
```

**Step 3 — Enter a password when prompted:**
```
=== Password Strength Checker ===

Enter password (or 'q' to quit): MyPass@123
```

Type `q` to exit the program.

> No external libraries or pip installs needed. Works out of the box on any system with Python 3.

---

## 🖥️ Sample Output

```
=== Password Strength Checker ===

Enter password (or 'q' to quit): Hello@12345

--- Checklist ---
  ✔  At least 8 characters
  ✔  At least 12 characters
  ✔  Uppercase letter (A-Z)
  ✔  Lowercase letter (a-z)
  ✔  Digit (0-9)
  ✔  Special character (!@#$%^&*)
  ✘  No repeated chars (aaa)

Score : 86/100  [█████████████████░░░]
Level : Strong 👍

Tips to improve:
  → Add: No repeated chars (aaa)
```

---

## ✅ Password Rules Checked

| # | Rule | Example |
|---|---|---|
| 1 | At least 8 characters | `Hello123` |
| 2 | At least 12 characters | `Hello@123456` |
| 3 | Uppercase letter (A–Z) | `Hello` |
| 4 | Lowercase letter (a–z) | `hello` |
| 5 | Digit (0–9) | `Hello1` |
| 6 | Special character (`!@#$%^&*`) | `Hello@1` |
| 7 | No repeated characters (aaa) | avoid `Helllo` |

---

## 🏷️ Strength Labels

| Score | Label |
|---|---|
| 85 – 100% | Very Strong 💪 |
| 65 – 84% | Strong 👍 |
| 45 – 64% | Moderate ⚠️ |
| 25 – 44% | Weak 😟 |
| 0 – 24% | Very Weak 🚨 |

---

## 📁 Project Structure

```
password-strength-checker/
│
├── password_checker.py   # Main Python program
└── README.md             # Project documentation
```

---

## ⚙️ How It Works

1. User enters a password via `input()`
2. The password is checked against 7 rules using Python's `re` module
3. Each passed rule adds 1 to the score
4. Score is converted to a percentage out of 100
5. A strength label and visual progress bar are displayed
6. Failed rules are shown as tips for improvement
7. Loop continues until user types `q`

---

## 🔮 Future Improvements

- GUI version using Tkinter or Flask
- Check against known breached passwords (Have I Been Pwned API)
- Auto password generator
- Detect keyboard patterns like `qwerty`, `asdf`
- Mobile app version

---

## 📄 License

This project is made for educational purposes as part of a Cyber Security Capstone Project.
