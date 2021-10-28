#Nick Caravaggio
# main view controller for final project

import tkinter as tk
import model_main
import view_strings
import help_functions
import hundred_records


############ ALL Main Button Window Functions #####################

######### FAKER Function #######################################
def faker_popup():
    # Faker Helpers
    def faker_name():
        faker_output.insert(tk.END,"Fake Name:\n")
        faker_output.insert(tk.END,model_main.fake_choice(1))
        faker_output.insert(tk.END,"\n\n")
        faker_output.see(tk.END)
        
    def faker_address():
        faker_output.insert(tk.END,"Fake Address:\n")
        faker_output.insert(tk.END,model_main.fake_choice(2))
        faker_output.insert(tk.END,"\n\n")
        faker_output.see(tk.END)

    def faker_description():
        faker_output.insert(tk.END,"Fake Description:\n")
        faker_output.insert(tk.END,model_main.fake_choice(3))
        faker_output.insert(tk.END,"\n\n")
        faker_output.see(tk.END)

    def faker_company():
        faker_output.insert(tk.END,"Fake Company:\n")
        faker_output.insert(tk.END,model_main.fake_choice(4))
        faker_output.insert(tk.END,"\n\n")
        faker_output.see(tk.END)
        
    faker_window = tk.Toplevel()
    faker_window.title("Faker Program")
    
    top_label = tk.Label(faker_window, text=view_strings.faker_str)
    top_label.grid(column=1, row=0)
    
    faker_output = tk.Text(faker_window,
                           height=17, width=80, bg="white")
    faker_output.grid(column=1, row=1)

    # Creating two frames on the sides of the text area, for multiple buttons.
    left_frame = tk.Frame(faker_window)
    left_frame.grid(column=0, row=1)
    right_frame = tk.Frame(faker_window)
    right_frame.grid(column=2, row=1)

    # Creating left side buttons (name + address)
    name_button = tk.Button(left_frame, text="Fake Name", fg="blue",height=3,
                            width=10, command=faker_name)
    name_button.pack(side="top", pady=10)
    address_button = tk.Button(left_frame, text="Fake Address", fg="blue",
                               height=3,width=10, command=faker_address)
    address_button.pack(side="top", pady=10)

    # Creating right side buttons (description + company)
    description_button = tk.Button(right_frame, text="Fake\nDescription",
                                   fg="blue",height=3, width=10,
                                   command=faker_description)
    description_button.pack(side="top", pady=10)
    company_button = tk.Button(right_frame, text="Fake Company", fg="blue",
                               height=3,width=10, command=faker_company)
    company_button.pack(side="top", pady=10)
    
    faker_window.mainloop()

################# nmap Function #################################
def nmap_popup():
    help_window = tk.Toplevel()
    help_window.title("nmap Example")
    help_window.geometry("400x160")
    text_box = tk.Label(help_window, text="Coming Soon...")
    text_box.pack(side="top", pady=10)
    close_button = tk.Button(help_window, fg="blue", text="Close",
                      command=help_window.destroy)
    close_button.pack()
    help_window.mainloop()

############# Cryptography Function ############################
def crypt_popup():
    # crypt helpers :)
    def crypt_encrypt(phrase):
        crypt_output.insert(tk.END,"Encrypted:\n")
        crypt_output.insert(tk.END,model_main.crypt_choice(phrase,1))
        crypt_output.insert(tk.END,"\n\n")
        crypt_output.see(tk.END)
        
    def crypt_decrypt(phrase):
        crypt_output.insert(tk.END,"Decrypted:\n")
        crypt_output.insert(tk.END,model_main.crypt_choice(phrase,2))
        crypt_output.insert(tk.END,"\n\n")
        crypt_output.see(tk.END)
        
    # initializes main window
    crypt_window = tk.Toplevel()
    crypt_window.title("Cryptography Program")
    # Sets top label to description
    top_label = tk.Label(crypt_window, text=view_strings.crypt_str)
    top_label.grid(column=1, row=0)
    # Initializes text box which modifies "user_submit"
    name_entry = tk.Entry(crypt_window,width=54)
    name_entry.grid(column=1, row=1)

    # "Encrypt" and "decrypt" buttons that connect to their functions
    encrypt_button = tk.Button(crypt_window, text="Encrypt", fg="blue",height=3,
                                width=10,
                                command=lambda:crypt_encrypt(name_entry.get()))
    encrypt_button.grid(column=1,row=2, pady=5)
    decrypt_button = tk.Button(crypt_window, text="Decrypt", fg="red",
                               height=3,width=10,
                               command=lambda:crypt_decrypt(name_entry.get()))
    decrypt_button.grid(column=1,row=3, pady=5)

    # Large textbox for outputs initialization
    crypt_output = tk.Text(crypt_window, height=17, width=56, bg="white")
    crypt_output.grid(column=1, row=4, pady=10, padx=10)

################ scapy function ###############################
def scapy_popup():
    help_window = tk.Toplevel()
    help_window.title("Scapy Sample")
    help_window.geometry("400x160")
    text_box = tk.Label(help_window, text="Coming Soon...")
    text_box.pack(side="top", pady=10)
    close_button = tk.Button(help_window, fg="blue", text="Close",
                      command=help_window.destroy)
    close_button.pack()
    help_window.mainloop()

######################## video game helper function #######################
def vg_popup():
    help_window = tk.Toplevel()
    help_window.title("VG Organiser")
    help_window.geometry("400x160")
    text_box = tk.Label(help_window, text="Coming Soon... But click run\n"+\
                        "to use this function in the shell right now!\n"+\
                        "Use !end at any time in the shell to resume.")
    text_box.pack(side="top", pady=10)
    close_button = tk.Button(help_window, fg="blue", text="Close",
                      command=help_window.destroy)
    close_button.pack(pady=10)
    run_button = tk.Button(help_window, fg="green", text="Run",
                      command=hundred_records.main)
    run_button.pack(pady=10)
    help_window.mainloop()

# mysterious function?
def ec_popup():
    help_window = tk.Toplevel()
    help_window.title("?????????????????????")
    help_window.geometry("400x160")
    new_pic = tk.PhotoImage(file="secretpb.png")
    
    close_button = tk.Button(help_window, image=new_pic,
                      command=help_window.destroy)
    close_button.pack()
    help_window.mainloop()

################## Main Program #####################
def main_program():
    # Main window init
    nav_window = tk.Tk()
    nav_window.title("Main Window")

    ec_pic = tk.PhotoImage(file="buttonpic.png")

    # Top main message
    nav_message = tk.Label(text="\nWelcome to Nick's Cyber Examples!"\
                           + "\nPlease select an option below!")
    nav_message.grid(row=0, column=1)

    # Top left credits
    nav_message = tk.Label(text="Nick Caravaggio\n"\
                           + "ncaravaggio\nv1.0")
    nav_message.grid(row=0, column=0)

    # Top right help button (command=help_popup)
    help_button = tk.Button(text="Help?", fg="blue",width=7,height = 2,
                            command=help_functions.help_popup)
    help_button.grid(row=0, column=2)

    # All main command Buttons below:
    faker_button = tk.Button(text="Option 1:\nFaker Example",width=20,height=4,
                             fg="blue", command=faker_popup)
    faker_button.grid(row=1, column=1, pady=10)

    nmap_button = tk.Button(text="Option 2:\nnmap Example",width=20,height=4,
                             fg="red", command=nmap_popup)
    nmap_button.grid(row=2, column=1, pady=10)

    crypt_button = tk.Button(text="Option 3:\nCryptography Example",width=20,
                             fg="blue", height=4, command=crypt_popup)
    crypt_button.grid(row=3, column=1, pady=10)

    scapy_button = tk.Button(text="Option 4:\nScapy Example",width=20,
                             fg="red", height=4, command=scapy_popup)
    scapy_button.grid(row=4, column=1, pady=10)

    vg_button = tk.Button(text="Option 5:\nVideo Game Sales\n"
                              + "Organization Program", width=20,height=4,
                             fg="orange",command=vg_popup)
    vg_button.grid(row=5, column=1, pady=10)
    
    ec_button = tk.Button(image=ec_pic,width=20, height=4,
                             command=ec_popup)
    ec_button.grid(row=5, column=0, pady=10)

    # All main command -HELP- Buttons below:
    fakerh_button = tk.Button(text="?", fg="blue", width=2,height=1,
                              command=help_functions.fakerh_popup)
    fakerh_button.grid(row=1, column=2)

    nmaph_button = tk.Button(text="?", fg="blue", width=2,height=1,
                             command=help_functions.nmaph_popup)
    nmaph_button.grid(row=2, column=2)

    crypth_button = tk.Button(text="?", fg="blue", width=2,height=1,
                              command=help_functions.crypth_popup)
    crypth_button.grid(row=3, column=2)

    scapyh_button = tk.Button(text="?", fg="blue", width=2,height=1,
                              command=help_functions.scapyh_popup)
    scapyh_button.grid(row=4, column=2)

    vgh_button = tk.Button(text="?", fg="blue", width=2,height=1,
                           command=help_functions.vgh_popup)
    vgh_button.grid(row=5, column=2)

    nav_window.mainloop()

if __name__ == "__main__":
    main_program()
