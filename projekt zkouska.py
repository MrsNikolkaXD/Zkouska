
seznam_pojisteny = []


def ziskat_informace_pojisteny():
    informace_pojisteny = {}
    informace_pojisteny["jmeno"] = input("Zadejte jméno pojištěného: ")
    informace_pojisteny["prijmeni"] = input("Zadejte příjmení pojištěného: ")
    informace_pojisteny["vek"] = input("Zadejte věk pojištěného: ")
    informace_pojisteny["telefonni_cislo"] = input("Zadejte telefonní číslo pojištěného: ")
    return informace_pojisteny


def najit_pojisteny(seznam, jmeno, prijmeni):
    for i, pojisteny in enumerate(seznam):
        if pojisteny['jmeno'] == jmeno and pojisteny['prijmeni'] == prijmeni:
            return i
    return None


def main():
    print("______________________________")
    print("Evidence pojištěných")
    print("______________________________")
    pokracovat = True
    while pokracovat:
        print("Vyberte si akci: ")
        pokracovat = vyber()


def vyber():
     while True:
        volba = input("\n1. Přidat nového pojištěného\n2. Vypsat všechny pojištěné\n3. Vyhledat pojištěného\n4. Konec\n")
        if volba == "1":
            informace_pojisteny = ziskat_informace_pojisteny()
            seznam_pojisteny.append(informace_pojisteny)
            print("Pojištěný byl úspěšně přidán.")
            seznam_pojisteny.sort(key=lambda x: x['jmeno'])
            input("Pokračujte stisknutím Enter...")
            return True
        elif volba == "2":
            if len(seznam_pojisteny) == 0:
                print("V seznamu nejsou žádní pojištění.")

            else:
                print("Seznam všech pojištěných:")
                for i, pojisteny in enumerate(seznam_pojisteny):
                    print("{:<10} {:<10} {:<10} {:<10}".format(pojisteny['jmeno'], pojisteny['prijmeni'], pojisteny['vek'], pojisteny['telefonni_cislo']))
            input("Pokračujte stisknutím Enter...")
            return True
        elif volba == "3":
            jmeno = input("Zadejte jméno pojištěného: ")
            prijmeni = input("Zadejte příjmení pojištěného: ")
            index = najit_pojisteny(seznam_pojisteny, jmeno, prijmeni)
            if index is not None:
                print("{:<10} {:<10} {:<10} {:<10}".format(seznam_pojisteny[index]['jmeno'], seznam_pojisteny[index]['prijmeni'], seznam_pojisteny[index]['vek'], seznam_pojisteny[index]['telefonni_cislo']))
            else:
                print("Pojištěný se zadaným jménem a příjmením nebyl nalezen.")
            input("Pokračujte stisknutím Enter...")
            return True

        elif volba == "4":
            print("Konec programu.")
            return False
        else:
            print("Neplatná volba, zkuste to znovu.")
            return True

if __name__ == "__main__":
    main()