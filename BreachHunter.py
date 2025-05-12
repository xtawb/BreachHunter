import csv
import subprocess
import tempfile
import os
import time

SUPPORTED_HASH_PREFIXES = ["$2y$", "$2a$", "$2b$", "$1$", "$6$", "$5$", "$argon2i$", "$argon2id$"]

def is_supported_hash(password_hash):
    return any(password_hash.startswith(prefix) for prefix in SUPPORTED_HASH_PREFIXES)

def load_hashes_from_csv(csv_path):
    hashes = []
    user_data_map = {}
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            password_hash = row.get("password", "")
            username = row.get("username", "")
            if is_supported_hash(password_hash):
                hashes.append(f"{username}:{password_hash}")
                user_data_map[username] = row
    return hashes, user_data_map

def run_john(hashfile_path, wordlist_path):
    print("🕵️ Running John the Ripper...")
    subprocess.run(["john", "--wordlist=" + wordlist_path, hashfile_path])

def get_cracked_passwords(hashfile_path):
    print("📥 Retrieving cracked passwords...")
    result = subprocess.run(["john", "--show", hashfile_path], capture_output=True, text=True)
    lines = result.stdout.strip().splitlines()
    cracked = {}
    for line in lines:
        if ":" in line:
            username, password = line.split(":", 1)
            cracked[username] = password
    return cracked

def save_results(found, output_file="cracked_passwords.csv"):
    with open(output_file, "w", encoding="utf-8", newline="") as f:
        fieldnames = list(found[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(found)
    print(f"\n📁 Results saved to {output_file}")

def main():
    print("🔐 Password Cracking Tool using John the Ripper")

    csv_path = input("📄 Enter the path to your CSV database file: ").strip()
    wordlist_path = input("🗂️ Enter the path to your password wordlist: ").strip()

    if not os.path.exists(csv_path) or not os.path.exists(wordlist_path):
        print("❌ One or both files do not exist. Please check your paths.")
        return

    start_time = time.time()

    hashes, user_map = load_hashes_from_csv(csv_path)
    if not hashes:
        print("⚠️ No supported hashes found in the file.")
        return

    with tempfile.NamedTemporaryFile("w+", delete=False) as hashfile:
        hashfile_path = hashfile.name
        hashfile.write("\n".join(hashes))

    run_john(hashfile_path, wordlist_path)
    cracked = get_cracked_passwords(hashfile_path)

    found = []
    for username, password in cracked.items():
        if username in user_map:
            data = user_map[username]
            data["cracked_password"] = password
            found.append(data)

    elapsed = time.time() - start_time
    print(f"\n✅ Finished in {elapsed:.2f} seconds")
    print(f"🔓 {len(found)} out of {len(hashes)} passwords cracked\n")

    for entry in found:
        print(f"[+] User: {entry['username']} | Name: {entry.get('name', 'N/A')} | Password: {entry['cracked_password']}")

    if found:
        save_results(found)

    os.remove(hashfile_path)

if __name__ == "__main__":
    main()
