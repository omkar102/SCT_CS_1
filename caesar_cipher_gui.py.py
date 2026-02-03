import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class CaesarCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher - Encryption & Decryption Tool")
        self.root.geometry("700x600")
        self.root.configure(bg='#2C3E50')
        # This is for title.
        title_label = tk.Label(
            root, 
            text="🔐 Caesar Cipher Tool", 
            font=("Arial", 24, "bold"),
            bg='#2C3E50',
            fg='#ECF0F1'
        )
        title_label.pack(pady=20)
        # This is for Main Frame.
        main_frame = tk.Frame(root, bg='#34495E', padx=20, pady=20)
        main_frame.pack(padx=20, pady=10, fill='both', expand=True)
        # For Input Text
        tk.Label(
            main_frame, 
            text="Enter Your Message:", 
            font=("Arial", 12, "bold"),
            bg='#34495E',
            fg='#ECF0F1'
        ).grid(row=0, column=0, sticky='w', pady=5)
        
        self.input_text = scrolledtext.ScrolledText(
            main_frame, 
            height=6, 
            width=60,
            font=("Arial", 11),
            wrap=tk.WORD
        )
        self.input_text.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Shift Value
        shift_frame = tk.Frame(main_frame, bg='#34495E')
        shift_frame.grid(row=2, column=0, columnspan=2, pady=15)
        tk.Label(
            shift_frame, 
            text="Shift Value:", 
            font=("Arial", 12, "bold"),
            bg='#34495E',
            fg='#ECF0F1'
        ).pack(side=tk.LEFT, padx=5)
        
        self.shift_var = tk.IntVar(value=3)
        self.shift_spinbox = tk.Spinbox(
            shift_frame,
            from_=1,
            to=25,
            textvariable=self.shift_var,
            font=("Arial", 12),
            width=10
        )
        self.shift_spinbox.pack(side=tk.LEFT, padx=5)
        
        # Buttons Frame
        button_frame = tk.Frame(main_frame, bg='#34495E')
        button_frame.grid(row=3, column=0, columnspan=2, pady=15)
        
        encrypt_btn = tk.Button(
            button_frame,
            text="🔒 ENCRYPT",
            command=self.encrypt_message,
            font=("Arial", 12, "bold"),
            bg='#27AE60',
            fg='white',
            padx=30,
            pady=10,
            cursor='hand2'
        )
        encrypt_btn.pack(side=tk.LEFT, padx=10)
        decrypt_btn = tk.Button(
            button_frame,
            text="🔓 DECRYPT",
            command=self.decrypt_message,
            font=("Arial", 12, "bold"),
            bg='#E74C3C',
            fg='white',
            padx=30,
            pady=10,
            cursor='hand2'
        )
        decrypt_btn.pack(side=tk.LEFT, padx=10)
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ CLEAR",
            command=self.clear_all,
            font=("Arial", 12, "bold"),
            bg='#95A5A6',
            fg='white',
            padx=30,
            pady=10,
            cursor='hand2'
        )
        clear_btn.pack(side=tk.LEFT, padx=10)
        # Outputting Text
        tk.Label(
            main_frame, 
            text="Result:", 
            font=("Arial", 12, "bold"),
            bg='#34495E',
            fg='#ECF0F1'
        ).grid(row=4, column=0, sticky='w', pady=5)
        
        self.output_text = scrolledtext.ScrolledText(
            main_frame, 
            height=6, 
            width=60,
            font=("Arial", 11),
            wrap=tk.WORD,
            bg='#ECF0F1'
        )
        self.output_text.grid(row=5, column=0, columnspan=2, pady=5)
        
        # Footer
        footer = tk.Label(
            root,
            text="SkillCraft Technology - Cybersecurity Internship Task 01",
            font=("Arial", 9),
            bg='#2C3E50',
            fg='#95A5A6'
        )
        footer.pack(side=tk.BOTTOM, pady=10)
    
    def caesar_cipher(self, text, shift, mode='encrypt'):
        """Perform Caesar Cipher encryption or decryption"""
        if mode == 'decrypt':
            shift = -shift
        
        result = ""
        for char in text:
            if char.isalpha():
                # Determine if uppercase or lowercase
                ascii_offset = 65 if char.isupper() else 97
                # Shift the character
                shifted = (ord(char) - ascii_offset + shift) % 26
                result += chr(shifted + ascii_offset)
            else:
                # Keep non-alphabetic characters as is
                result += char
        
        return result
    
    def encrypt_message(self):
        """Encrypt the input message"""
        message = self.input_text.get("1.0", tk.END).strip()
        
        if not message:
            messagebox.showwarning("Input Error", "Please enter a message to encrypt!")
            return
        
        try:
            shift = self.shift_var.get()
            encrypted = self.caesar_cipher(message, shift, mode='encrypt')
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", encrypted)
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")
    
    def decrypt_message(self):
        """Decrypt the input message"""
        message = self.input_text.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Input Error", "Please enter a message to decrypt!")
            return
        try:
            shift = self.shift_var.get()
            decrypted = self.caesar_cipher(message, shift, mode='decrypt')
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", decrypted)
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")
    
    def clear_all(self):
        """Clear all text fields"""
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        self.shift_var.set(3)

def main():
    root = tk.Tk()
    app = CaesarCipherGUI(root)
    root.mainloop()

if __name__=="__main__":
    main()
