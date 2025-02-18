import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class MemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Memo App")
        self.root.geometry("400x300")

        # List to store all memos
        self.memos = []

        # GUI Elements
        self.label = tk.Label(root, text="Enter Your Memo:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.memo_entry = tk.Text(root, height=10, width=40)
        self.memo_entry.pack(pady=10)

        self.save_button = tk.Button(root, text="Save", command=self.save_memo)
        self.save_button.pack(pady=5)

        self.details_button = tk.Button(root, text="Details", command=self.show_details)
        self.details_button.pack(pady=5)

        self.history_button = tk.Button(root, text="History", command=self.show_history)
        self.history_button.pack(pady=5)

    def save_memo(self):
        """Save the memo to the list."""
        memo_content = self.memo_entry.get("1.0", tk.END).strip()
        if memo_content:
            # Generate a unique ID and timestamp
            memo_id = len(self.memos) + 1
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Create a memo dictionary
            memo = {
                "id": memo_id,
                "timestamp": timestamp,
                "content": memo_content
            }

            # Add the memo to the list
            self.memos.append(memo)

            # Clear the entry field
            self.memo_entry.delete("1.0", tk.END)

            messagebox.showinfo("Success", "Memo saved successfully!")
        else:
            messagebox.showwarning("Error", "Memo cannot be empty!")

    def show_details(self):
        """Show details of a specific memo."""
        if not self.memos:
            messagebox.showwarning("Error", "No memos available!")
            return

        # Create a new window to display details
        details_window = tk.Toplevel(self.root)
        details_window.title("Memo Details")
        details_window.geometry("300x200")

        # Dropdown to select a memo
        memo_ids = [memo["id"] for memo in self.memos]
        selected_id = tk.IntVar(value=memo_ids[0])

        tk.Label(details_window, text="Select Memo ID:").pack(pady=10)
        memo_dropdown = tk.OptionMenu(details_window, selected_id, *memo_ids)
        memo_dropdown.pack(pady=10)

        def display_details():
            """Display the selected memo's details."""
            selected_memo = next(memo for memo in self.memos if memo["id"] == selected_id.get())
            details_text = f"ID: {selected_memo['id']}\nTimestamp: {selected_memo['timestamp']}\nContent: {selected_memo['content']}"
            messagebox.showinfo("Memo Details", details_text)

        tk.Button(details_window, text="Show Details", command=display_details).pack(pady=10)

    def show_history(self):
        """Show the history of all saved memos."""
        if not self.memos:
            messagebox.showwarning("Error", "No memos available!")
            return

        # Create a new window to display history
        history_window = tk.Toplevel(self.root)
        history_window.title("Memo History")
        history_window.geometry("400x300")

        # Display all memos in a text widget
        history_text = tk.Text(history_window, height=15, width=40)
        history_text.pack(pady=10)

        for memo in self.memos:
            history_text.insert(tk.END, f"ID: {memo['id']}\nTimestamp: {memo['timestamp']}\nContent: {memo['content']}\n\n")

        history_text.config(state=tk.DISABLED)  # Make the text widget read-only

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MemoApp(root)
    root.mainloop()