from spyder.beleza_na_web import BelezaNaWeb


def main():
    beleza = BelezaNaWeb()
    for response in beleza.start_request():
        beleza.parse(response)


if __name__ == "__main__":
    main()
