from weather_api import Weather


def main():
    w = Weather()
    while True:
        miasto = str(input("Podaj miasto(q aby wyjsc) : "))
        if miasto == "q":
            break
        report = w.get_weather(miasto)

        if report is not None:
           temp = report['main']['temp']
           desc = report['weather'][0]['description']

           print(f"-------- POGODA DLA: {miasto.upper()} --------")
           print(f"Temperatura: {temp}°C")
           print(f"Opis: {desc}")
           print("------------------------------------------")



        else:
            print("nie znaleziono miasta")


if __name__ == '__main__':
    print(main())
