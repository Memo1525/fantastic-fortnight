# Python program to create a basic form
# GUI application using the customtkinter module
import customtkinter as ctk
import tkinter as tk

# Sets the appearance of the window
# Supported modes : Light, Dark, System
# "System" sets the appearance mode to
# the appearance mode of the system
ctk.set_appearance_mode("System")

# Sets the color of the widgets in the window
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("green")

# Dimensions of the window
appWidth, appHeight = 600, 700


# App Class
class App(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets the title of the window to "App"
        self.title("Proyecto 2 Parcial")
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{appWidth}x{appHeight}")

        # Name Label
        self.nameLabel = ctk.CTkLabel(self,
                                text="Name")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self,
                        placeholder_text="Memo")
        self.nameEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")

        # Last name Label
        self.lnameLabel = ctk.CTkLabel(self,
                                text="Last Name")
        self.lnameLabel.grid(row=1, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        # Last name Entry Field
        self.lnameEntry = ctk.CTkEntry(self,
                        placeholder_text="Rodriguez")
        self.lnameEntry.grid(row=1, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")


        # Age Label
        self.ageLabel = ctk.CTkLabel(self, text="Age")
        self.ageLabel.grid(row=2, column=0,
                        padx=20, pady=20,
                        sticky="ew")

        # Age Entry Field
        self.ageEntry = ctk.CTkEntry(self,
                            placeholder_text="18")
        self.ageEntry.grid(row=2, column=1,
                        columnspan=3, padx=20,
                        pady=20, sticky="ew")

        # Operation Label
        self.operationLabel = ctk.CTkLabel(self,
                                text="Operation")
        self.operationLabel.grid(row=3, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        # Gender Radio Buttons
        self.operationVar = tk.StringVar(value="Alta")

        self.addRadioButton = ctk.CTkRadioButton(self,
                            text="Alta",
                                variable=self.operationVar,
                                        value="Alta")
        self.addRadioButton.grid(row=3, column=1,
                                padx=20, pady=20,
                                sticky="ew")

        self.deleteRadioButton = ctk.CTkRadioButton(self,
                                    text="Baja",
                                    variable=self.operationVar,
                                    value="Baja")
        self.deleteRadioButton.grid(row=3, column=2,
                                    padx=20, pady=20,
                                    sticky="ew")
        
        self.changeRadioButton = ctk.CTkRadioButton(self,
                                    text="Cambio",
                                    variable=self.operationVar,
                                    value="Cambio")
        self.changeRadioButton.grid(row=3, column=3, padx=20,
                                pady=20, sticky="ew")

        # Select Label
        self.selectLabel = ctk.CTkLabel(self,
                                        text="Select")
        self.selectLabel.grid(row=4, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        # Choice Check boxes
        self.checkboxVar = tk.StringVar(value="Choice 1")
        
        self.choice1 = ctk.CTkCheckBox(self,
                            text="Usuario Ingresado",
                            variable=self.checkboxVar,
                            onvalue="choice1", offvalue="c1")
        self.choice1.grid(row=4, column=1,
                        padx=20, pady=20,
                        sticky="ew")

        self.choice2 = ctk.CTkCheckBox(self,
                            text="Todos los usuarios",
                            variable=self.checkboxVar,
                            onvalue="choice2",
                            offvalue="c2")							
        self.choice2.grid(row=4, column=2,
                        padx=20, pady=20,
                        sticky="ew")

        # Kind of File Label
        self.fileLabel = ctk.CTkLabel(self,
                                    text="Kind File")
        self.fileLabel.grid(row=5, column=0,
                                padx=20, pady=20,
                                sticky="ew")

        # Occupation combo box
        self.fileOptionMenu = ctk.CTkOptionMenu(self,
                                    values=["Generate Power Point",
                                    "Generate Txt",
                                    "Generate PDF"])
        self.fileOptionMenu.grid(row=5, column=1,
                                    padx=20, pady=20,
                                    columnspan=2, sticky="ew")

        # Generate Changes
        self.changesResultsButton = ctk.CTkButton(self,
                                        text="Generate Changes",
                                        command=self.generateResults)
        self.changesResultsButton.grid(row=6, column=1,
                                        columnspan=2, padx=20,
                                        pady=20, sticky="ew")


        # Generate Files
        self.generateResultsButton = ctk.CTkButton(self,
                                        text="Generate File",
                                        command=self.generateResults)
        self.generateResultsButton.grid(row=7, column=1,
                                        columnspan=2, padx=20,
                                        pady=20, sticky="ew")

        # Text Box
        self.displayBox = ctk.CTkTextbox(self,
                                        width=200,
                                        height=100)
        self.displayBox.grid(row=8, column=0,
                            columnspan=4, padx=20,
                            pady=20, sticky="nsew")
        self.registry = []
        self.next_id = 1


    # This function is used to insert the
    # details entered by users into the textbox
    def generateResults(self):
        text = self.createText()
        #self.displayBox.insert("0.0", text)
        people_data = self.storeText(text)
        self.displayBox.insert("end","\n")
        self.displayBox.insert("end", people_data)

    # This function is used to get the selected
    # options and text from the available entry
    # fields and boxes and then generates
    # a prompt using them
    def createText(self):
        if self.operationVar.get() == "Alta":
            self.registry.append(self.add_entry(self.nameEntry.get(), self.lnameEntry.get(), self.ageEntry.get()))
        if self.operationVar.get() == "Baja":
            self.registry.de

        checkboxValue = ""

        # .get() is used to get the value of the checkboxes and entryfields

        if self.choice1._check_state and self.choice2._check_state:
            checkboxValue += self.choice1.get() + " and " + self.choice2.get()
        elif self.choice1._check_state:
            checkboxValue += self.choice1.get()
        elif self.choice2._check_state:
            checkboxValue += self.choice2.get()
        else:
            checkboxValue = "none of the available options"

        # Constructing the text variable
        #text = f"{self.nameEntry.get()} {self.lnameEntry.get()} : \n{self.genderVar.get()} {self.ageEntry.get()} years old and prefers {checkboxValue}\n"
        text = self.registry[-1]
        #text += f"{self.genderVar.get()} currently a {self.occupationOptionMenu.get()}"

        return text
    
    def storeText(self, text):
        people_data = []
        people_data.append(text)
        return people_data
    
    def add_entry(self,name, last_name, age):
        entry = {
            'name': name,
            'last_name': last_name,
            'age': age,
            'id': self.next_id  # generate id based on the number of entries
        } 
        self.next_id += 1
        return entry

    def update_entry(self,entry_id, name, last_name, age):
        for entry in self.registry:
            if entry['id'] == entry_id:
                entry['name'] = name
                entry['last_name'] = last_name
                entry['age'] = age
                break
            else:
                print("something fails")

    def delete_entry(self,entry_id):
        for entry in self.registry:
            if entry['id'] == entry_id:
                self.registry.remove(entry)

if __name__ == "__main__":
    app = App()
    # Used to run the application
    app.mainloop()
