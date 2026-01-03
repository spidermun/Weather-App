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
           if temp > 10:
               emotka = "☀️"
           else:
               emotka = "️🌥️"

           desc = report['weather'][0]['description']



           print(f"-------- POGODA DLA: {miasto.upper()} --------")
           print(f"Temperatura: {temp}°C")
           print(f"Opis: {emotka} {desc}")
           print("------------------------------------------")



        else:
            print("nie znaleziono miasta")


if __name__ == '__main__':
    print(main())
