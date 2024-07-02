import tkinter as tk
from tkinter import messagebox

class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Initialize ContactBook instance
        self.contact_book = ContactBookGUI()

        # Create GUI elements
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        # Labels and Entries
        tk.Label(self.frame, text="Name:").grid(row=0, column=0, sticky='w')
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Phone Number:").grid(row=1, column=0, sticky='w')
        self.phone_entry = tk.Entry(self.frame)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Email:").grid(row=2, column=0, sticky='w')
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Address:").grid(row=3, column=0, sticky='w')
        self.address_entry = tk.Entry(self.frame)
        self.address_entry.grid(row=3, column=1)

        # Buttons
        self.add_button = tk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, pady=10)

        self.view_button = tk.Button(self.frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=4, column=1, pady=10)

        self.search_button = tk.Button(self.frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=5, column=0, pady=10)

        self.update_button = tk.Button(self.frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=5, column=1, pady=10)

        self.delete_button = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=6, column=0, pady=10)

        # Text Area for displaying contacts
        self.text_area = tk.Text(self.frame, height=10, width=50)
        self.text_area.grid(row=7, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone_number:
            self.contact_book.add_contact(name, phone_number, email, address)
            self.update_text_area()
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Name and Phone Number are required.")

    def view_contacts(self):
        self.text_area.delete('1.0', tk.END)
        contacts = self.contact_book.view_contacts()
        if contacts:
            for contact in contacts:
                self.text_area.insert(tk.END, f"Name: {contact['name']}, Phone: {contact['phone_number']}\n")
        else:
            self.text_area.insert(tk.END, "No contacts found.")

    def search_contact(self):
        query = self.name_entry.get() or self.phone_entry.get()
        self.text_area.delete('1.0', tk.END)
        contacts = self.contact_book.search_contact(query)
        if contacts:
            for contact in contacts:
                self.text_area.insert(tk.END, f"Name: {contact['name']}, Phone: {contact['phone_number']}\n")
        else:
            self.text_area.insert(tk.END, f"No contacts found matching '{query}'.")

    def update_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name:
            self.contact_book.update_contact(name, phone_number, email, address)
            self.update_text_area()
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Name is required for updating contact.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name:
            self.contact_book.delete_contact(name)
            self.update_text_area()
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Name is required for deleting contact.")

    def update_text_area(self):
        self.text_area.delete('1.0', tk.END)
        self.view_contacts()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
