# nick caravaggio

# These are the nav panel help buttons that look like blue question marks
# on the sides.
import tkinter as tk
import view_strings

# Help Button Popup
def help_popup():
    help_window = tk.Tk()
    help_window.title("Help")
    help_window.geometry("400x160")
    text_box = tk.Label(help_window, text=view_strings.help_str)
    text_box.pack(side="top", pady=10)
    close_button = tk.Button(help_window, fg="blue", text="Close",
                      command=help_window.destroy)
    close_button.pack()
    help_window.mainloop()

#### ALL Main HELP function buttons on the nav page ####
def fakerh_popup():
    fakerh_window = tk.Tk()
    fakerh_window.title("Faker Help Pop-Up")
    fakerh_window.geometry("425x100")
    text_box = tk.Label(fakerh_window, text=view_strings.fakerh)
    text_box.pack(side="top", pady=10)
    close_button = tk.Button(fakerh_window, fg="blue", text="Close",
                      command=fakerh_window.destroy)
    close_button.pack()
    fakerh_window.mainloop()

# nmaph help
def nmaph_popup():
    nmaph_window = tk.Tk()
    nmaph_window.title("nmap Help Pop-Up")
    nmaph_window.geometry("425x100")
    text_box = tk.Label(nmaph_window, text=view_strings.nmaph)
    text_box.pack(side="top", pady=10)
    close_button = tk.Button(nmaph_window, fg="blue", text="Close",
                      command=nmaph_window.destroy)
    close_button.pack()
    nmaph_window.mainloop()

# cryptography help
def crypth_popup():
    crypth_window = tk.Tk()
    crypth_window.title("Cryptography Help Pop-Up")
    crypth_window.geometry("425x100")
    text_box = tk.Label(crypth_window, text=view_strings.crypth)
    text_box.pack(side="top", pady=10)
    close_button = tk.Button(crypth_window, fg="blue", text="Close",
                      command=crypth_window.destroy)
    close_button.pack()
    crypth_window.mainloop()

# scapy help
def scapyh_popup():
    scapyh_window = tk.Tk()
    scapyh_window.title("Scapy Help Pop-Up")
    scapyh_window.geometry("425x100")
    text_box = tk.Label(scapyh_window, text=view_strings.scapyh)
    text_box.pack(side="top", pady=10)
    close_button = tk.Button(scapyh_window, fg="blue", text="Close",
                      command=scapyh_window.destroy)
    close_button.pack()
    scapyh_window.mainloop()

# video game organizer help
def vgh_popup():
    vgh_window = tk.Tk()
    vgh_window.title("VG Organizer Help Pop-Up")
    vgh_window.geometry("425x100")
    text_box = tk.Label(vgh_window, text=view_strings.vgh)
    text_box.pack(side="top", pady=10)
    close_button = tk.Button(vgh_window, fg="blue", text="Close",
                      command=vgh_window.destroy)
    close_button.pack()
    vgh_window.mainloop()
