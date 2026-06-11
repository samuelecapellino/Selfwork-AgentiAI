from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, nome: str, cognome: str, eta: int):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

   
    @abstractmethod
    def mostra_dettagli(self):
        pass




class Studente(Person):
    
    def __init__(self, nome: str, cognome: str, eta: int, matricola: str, corso_di_studi: str):
        super().__init__(nome, cognome, eta) # Eredita nome, cognome, eta
        self.matricola = matricola
        self.corso_di_studi = corso_di_studi

    def mostra_dettagli(self):
        return f"Studente: {self.nome} {self.cognome} | Matricola: {self.matricola} | Corso: {self.corso_di_studi}"


class Dipendente(Person):
   
    def __init__(self, nome: str, cognome: str, eta: int, id_azienda: str):
        super().__init__(nome, cognome, eta)
        self.id_azienda = id_azienda

    
    def mostra_dettagli(self):
        return f"Dipendente Aziendale ID: {self.id_azienda} | Nome: {self.nome} {self.cognome}"



class Docente(Dipendente):
   
    def __init__(self, nome: str, cognome: str, eta: int, id_azienda: str, materia: str):
        super().__init__(nome, cognome, eta, id_azienda) # Eredita tutto da Dipendente
        self.materia = materia

    def mostra_dettagli(self):
        return f"Docente di {self.materia}: Prof. {self.nome} {self.cognome} (ID: {self.id_azienda})"


class Freelance(Dipendente):
    def __init__(self, nome: str, cognome: str, eta: int, id_azienda: str, partita_iva: str, tariffa_oraria: float):
        super().__init__(nome, cognome, eta, id_azienda)
        self.partita_iva = partita_iva
        self.tariffa_oraria = tariffa_oraria

    def mostra_dettagli(self):
        return f"Freelance: {self.nome} {self.cognome} | P.IVA: {self.partita_iva} | Tariffa: €{self.tariffa_oraria}/h"



if __name__ == "__main__":
    print("--- Test del sistema OOP --- \n")

    
    studente1 = Studente("Marco", "Rossi", 21, "Uni12345", "Informatica")
    print(studente1.mostra_dettagli())

   
    docente1 = Docente("Laura", "Bianchi", 45, "DOC99", "Programmazione Python")
    print(docente1.mostra_dettagli())


    freelance1 = Freelance("Andrea", "Verdi", 33, "FREE44", "IT12345678901", 50.0)
    print(freelance1.mostra_dettagli())
