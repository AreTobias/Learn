class NewEmployee:
    def __init__(self, first_name, last_name, position, municipality):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.municipality = municipality
        
        self.email = first_name + last_name + municipality + "kommune.no"
        
        # Lager en string med punktum og bruker join på en liste og legger til @kommune som en string etterpå. Litt teit måte
        self.email_alt1 = '.'.join([first_name, last_name, municipality]) + "@kommune.no"
        # Lager en f-string, formaterer den slik som jeg ønsker. Mer ryddig.
        self.email_alt2 = f"{first_name}.{last_name}.{municipality}@kommune.no"

    def PrintEmployee(self):

        print(
              f"Er dette riktig?\n"
              f"Fornavn: {self.first_name}\n"
              f"Etternavn: {self.last_name}\n"
              f"Position: {self.position}\n"
              f"Email: {self.email}\n"
              f"Email Alternativ måte 1: {self.email_alt1}\n"
              f"Email Alternativ måte 2: {self.email_alt2}"
              )

e = NewEmployee("Are", "Olsen", "Apprentice", "Lindesnes")
e.PrintEmployee()
