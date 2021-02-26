# -*- coding utf-8 -*-

#definition une fonction seconde
def main():
    seconde = float(input("enter a time in seconds:" ))
    years = seconde // (12*30*24*3600)
    seconde = seconde % (12*30*24*3600)
    month = seconde // (30*24*3600)
    seconde = seconde % (30*24*3600)
    days = seconde // (24*3600)                 # car une journée correspond à 24hr ou 86400 secondes
    seconde = seconde % (24*3600)
    hour = seconde // 3600             # car 1hr correspond à 3600 secondes
    seconde %= 3600
    minute = seconde // 60
    seconde %=60
    seconds = seconde

    #affiche le resultat
    print('Y:M:D:H:m:s -> %d %d %d %d %d %d' % (years, month, days, hour, minute, seconds))


if __name__ == "__main__":
    main()


