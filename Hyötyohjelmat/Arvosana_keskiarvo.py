#!/bin/python3
def laske_keskiarvo():
    """
    Kysyy käyttäjältä arvosanoja kunnes käyttäjä lopettaa (tyhjä syöte tai 'stop').
    Hyväksii desimaalierottimena pisteen tai pilkun.
    Palauttaa (keskiarvo, määrä). Jos arvosanoja ei annettu, palauttaa (None, 0).
    """
    arvot = []
    print("Anna arvosanoja yksi kerrallaan. Lopeta painamalla Enter tyhjällä rivillä tai kirjoittamalla 'stop'.")
    while True:
        kysymys = input(f"Anna arvosana #{len(arvot)+1}: ").strip()
        if kysymys == "" or kysymys.lower() == "stop":
            break
        # Salli pilkku desimaalierottimena
        kysymys = kysymys.replace(",", ".")
        try:
            num = float(s)
        except ValueError:
            print("Virhe: syötä numero (esim. 4, 4.5) tai paina Enter lopettaaksesi.")
            continue
        arvot.append(num)

    if not arvot:
        print("Arvosanoja ei annettu. Keskiarvoa ei voi laskea.")
        return None, 0

    keskiarvo = sum(arvot) / len(arvot)
    # Pyöristetään siististi esimerkiksi kahteen desimaaliin
    print(f"Annettuja arvosanoja: {len(arvot)}")
    print(f"Keskiarvo: {keskiarvo:.2f}")
    return keskiarvo, len(arvot)

if __name__ == "__main__":
    laske_keskiarvo()