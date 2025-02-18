import os
from datetime import datetime

# File to store memos
MEMO_FILE = "memos.txt"

def load_memos():
    """Load existing memos from the file."""
    if os.path.exists(MEMO_FILE):
        with open(MEMO_FILE, "r") as file:
            return file.readlines()
    return []

def save_memo(memo):
    """Save a new memo to the file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(MEMO_FILE, "a") as file:
        file.write(f"{timestamp}: {memo}\n")

def delete_memo(index):
    """Delete a memo by its index."""
    memos = load_memos()
    if 0 <= index < len(memos):
        memos.pop(index)
        with open(MEMO_FILE, "w") as file:
            file.writelines(memos)
        print("Memo deleted successfully.")
    else:
        print("Invalid index. No memo deleted.")

def show_history():
    """Display all saved memos."""
    memos = load_memos()
    if not memos:
        print("No memos found.")
    else:
        print("\n--- Memo History ---")
        for i, memo in enumerate(memos):
            print(f"{i + 1}. {memo.strip()}")

def main():
    """Main function to run the memo app."""
    while True:
        print("\n--- Memo App ---")
        print("1. Save Memo")
        print("2. Delete Memo")
        print("3. View History")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            memo = input("Enter your memo: ")
            save_memo(memo)
            print("Memo saved successfully.")
        elif choice == "2":
            show_history()
            try:
                index = int(input("Enter the memo number to delete: ")) - 1
                delete_memo(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            show_history()
        elif choice == "4":
            print("Exiting the Memo App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()