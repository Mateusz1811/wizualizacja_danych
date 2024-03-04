import sys as system


def main():
    def zad1():
        x = input("Podaj zdanie: ")
        print(len(x))



    zad1()

    def zad2():
        system.stdout.write("Podaj 1 liczbę cąłkowitą: ")
        a = int(system.stdin.readline())
        system.stdout.write("Podaj 2 liczbe calkowita: ")
        b = int(system.stdin.readline())
        system.stdout.write("Podaj 3 liczbe calkowita: ")
        c = int(system.stdin.readline())
        wynik = (a**b) + c
        system.stdout.write(f"{wynik}")

    zad2()
    def zad3():
        napis = input("Podaj napis do sprawdzenia: ").lower()
        if napis == napis[::-1]:
            print("Ten napis jest palindromem")
        else:
            print("Ten napis nie jest palindromem")

    zad3()
    def zad4():
        liczba = int(input("Podaj liczbę do sprawdzenia: "))
        if liczba <= 1:
            print("Ta liczba nie jest liczba pierwsza")
        for i in range(2, liczba):
            if liczba % i == 0:
                print("To nie jest liczba pierwsza")
                break
        else:
            print("To jest liczba pierwsza")

    zad4()


if __name__ == "__main__":
    main()
