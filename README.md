<p align="center">
  <img src="https://i.ibb.co/jZV4phsq/Breach-Hunter.png" alt="BreachHunter Logo" width="150">
</p>

<h2 align="center">ＢｒｅａｃｈＨｕｎｔｅｒ</h2>

<p align="center">
  <b>A password cracking tool using John the Ripper with a CSV database and a wordlist.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Version-1.0.0-red" alt="Version">
  <img src="https://img.shields.io/github/issues-closed/xtawb/BreachHunter">
</p>

# 🔐 Password Cracking Tool using John the Ripper

This tool is designed to crack bcrypt hashed passwords from a CSV database using John the Ripper and a provided wordlist.

## 📝 Features
- Extracts bcrypt hashes (`$2y$` format) from a CSV file.
- Uses John the Ripper to crack passwords with a provided wordlist.
- Displays cracked passwords along with user details.
- Saves results to a CSV file for further analysis.

## ⚙️ Prerequisites
- Python 3.x
- John the Ripper installed on your system
- A CSV file containing username and password hashes
- A password wordlist file

## 📂 CSV File Format
The CSV file should include at least the following columns:
- `username`
- `password` (bcrypt hashed, starting with `$2y$`)
- `name` (optional, for display purposes)

Example CSV structure:
```csv
username,password,name
user1,$2y$10$N9qo8uLOickgx2ZMRZoMy...,John Doe
user2,$2y$10$ZAMMv.xKtYlLv6sUX.d2P...,Jane Smith
```

## 🚀 Usage
1. Clone or download the script `breachHunter.py`.
2. Ensure John the Ripper is installed and accessible in your system PATH.
   ```bash
   cd BreachHunter
   ```
3. Run the script:
   ```bash
   python3 breachHunter.py
   ```
4. Follow the prompts to provide:
   - Path to your CSV database file
   - Path to your password wordlist file

## 📊 Output
- The tool will display cracked passwords in the console.
- Results will be saved to `cracked_passwords.csv` in the same directory.

## ⚠️ Legal Disclaimer
This tool is intended for **educational purposes** and **authorized security testing only**. Unauthorized use to crack passwords without explicit permission is illegal and unethical. The developer assumes no liability for misuse of this tool.

## 📄 License
This project is open-source and available under the MIT License.

---

For questions or issues, please open an issue in the repository.
