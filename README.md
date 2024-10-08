# 🔐 Password Strength Checker

This is a simple **Password Strength Checker** built using Python's **Tkinter** library. The program evaluates the strength of a password based on certain criteria and provides immediate feedback on the password's security level.

## 📝 Features

- **Password Strength Evaluation**: Checks the password length, presence of uppercase and lowercase letters, digits, and special characters.
- **Strength Levels**:
  - Password too short
  - Very Weak
  - Weak
  - Moderate
  - Strong
  - Very Strong
- **Toggle Password Visibility**: Option to show or hide the password while typing.

## 💻 How It Works

The strength of the password is determined based on the following criteria:
1. Password must be at least 8 characters long.
2. Contains at least one uppercase letter (A-Z).
3. Contains at least one lowercase letter (a-z).
4. Contains at least one digit (0-9).
5. Contains at least one special character (!@#$%^&*(),.?":{}|<>).

## 🛠️ Tech Stack

- **Python**: Programming language
- **Tkinter**: Library for creating graphical user interfaces
- **re**: Module for regular expressions used in password validation

## 💡 How to Run

1. Clone the repository:
   git clone https://github.com/sakshinkn007/Password_Checker
2.Navigate to the project directory:
cd password-strength-checker

3. Run the Python script:
python password_checker.py

4.A GUI window will open where you can enter a password and check its strength.
