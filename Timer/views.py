from django.shortcuts import render
import datetime

def index(request):
    impreza = "21-01-01 17:30"
    impreza = {
        "dzien": 21,
        "godzina": 17,
        "minuta": 30
    }

    teraz = datetime.datetime.now()

    godziny = impreza["godzina"] - teraz.hour + (impreza["dzien"] - teraz.day) * 24
    minuty = impreza["minuta"] - teraz.minute

    if minuty < 0:
        godziny = godziny - 1
        minuty += 60


    return render(request, 'index.html', {'godziny': godziny, 'minuty': minuty})