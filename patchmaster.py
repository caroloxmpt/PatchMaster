import tkinter as tk
from tkinter import filedialog, messagebox
import os

class PatchMaster:
    def __init__(self, root):
        self.root = root
        self.root.title("PatchMaster - Executable Patcher")

        # File path
        self.file_path = ""

        # GUI Elements
        tk.Label(root, text="Executable Patcher", font=("Arial", 16)).pack(pady=10)

        tk.Button(root, text="Load Executable", command=self.load_executable).pack(pady=5)
        self.file_label = tk.Label(root, text="No file loaded", wraplength=400)
        self.file_label.pack(pady=5)

        tk.Label(root, text="Pattern to Replace (Hex):").pack(pady=5)
        self.pattern_entry = tk.Entry(root, width=50)
        self.pattern_entry.pack(pady=5)

        tk.Label(root, text="Replacement Pattern (Hex):").pack(pady=5)
        self.replacement_entry = tk.Entry(root, width=50)
        self.replacement_entry.pack(pady=5)

        tk.Button(root, text="Apply Patch", command=self.apply_patch).pack(pady=10)

    def load_executable(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe"), ("All Files", "*.*")])
        if self.file_path:
            self.file_label.config(text=f"Loaded: {os.path.basename(self.file_path)}")
        else:
            self.file_label.config(text="No file loaded")

    def apply_patch(self):
        if not self.file_path:
            messagebox.showerror("Error", "No executable file loaded!")
            return

        pattern = self.pattern_entry.get()
        replacement = self.replacement_entry.get()

        if not pattern or not replacement:
            messagebox.showerror("Error", "Pattern and replacement must not be empty!")
            return

        try:
            # Convert patterns to bytes
            pattern_bytes = bytes.fromhex(pattern)
            replacement_bytes = bytes.fromhex(replacement)

            if len(pattern_bytes) != len(replacement_bytes):
                messagebox.showerror("Error", "Pattern and replacement must have the same length!")
                return

            with open(self.file_path, "rb") as f:
                data = f.read()

            if pattern_bytes not in data:
                messagebox.showerror("Error", "Pattern not found in the executable!")
                return

            # Replace pattern
            patched_data = data.replace(pattern_bytes, replacement_bytes)

            # Save patched executable
            save_path = filedialog.asksaveasfilename(defaultextension=".exe", filetypes=[("Executable Files", "*.exe")])
            if save_path:
                with open(save_path, "wb") as f:
                    f.write(patched_data)
                messagebox.showinfo("Success", f"Patched executable saved to: {save_path}")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid hex input: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = PatchMaster(root)
    root.mainloop()
