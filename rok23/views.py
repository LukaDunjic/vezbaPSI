from django.shortcuts import render, redirect

from Vezba.models import Agencija, Termin


# Create your views here.

def uradiPrvo(request):
    return render(request, 'nesto/nesto.html')

def index(request):
    if request.method=='POST':
        print('usao')
        tablice=request.POST.get('tablice', '')
        datum=request.POST.get('datum', '')
        if tablice=='' and datum=='':
            poruka='Niste uneli ni tablice ni datum'
            context={
                'poruka':poruka
            }
            return render(request, 'index/index.html', context=context)
        if tablice=='' :
            poruka='Niste uneli tablice'
            context={
                'poruka':poruka
            }
            return render(request, 'index/index.html', context=context)
        if datum=='':
            poruka='Niste uneli datum'
            context={
                'poruka':poruka
            }
            return render(request, 'index/index.html', context=context)
        agencije=Agencija.objects.all()
        agencija=request.POST.get('agencija', '')
        # for i in range(len(agencije)):
        #     agencija=request.POST.get(agencije[i].ida, '')
        #     if agencija!='':
        #         break
        print(agencija)
        print(datum)
        print(tablice)
        return redirect ('termini', tablice=tablice, datum=datum,agencija=agencija )
    agencije = Agencija.objects.all()
    context={
        'agencije':agencije
    }
    for i in range(len(agencije)):
        print(agencije[i].naziv)
    return render(request, 'index/index.html', context)

def recervaija(request, tablice, datum, agencija, vreme):
    agencija1=Agencija.objects.get(ida=int(agencija))
    print(agencija1)
    agencija1=agencija1.naziv
    print(agencija1)
    context={
        'datum':datum,
        'vreme':vreme,
        'tablice':tablice,
        'agencija':agencija1
    }
    return render(request, 'recervaija/recervacija.html', context)

def termini(request, tablice, datum, agencija):

    termini=Termin.objects.all()
    termini1=[]
    if agencija != '':

        for i in termini:
            if i.ida.ida==int(agencija) and i.datum==datum:
                print('usao da ubacim')
                termini1.append(i)
    else:
        for i in termini:
            if i.datum==datum:
                termini1.append(i)
    poruka=''
    if len(termini1)==0:
        poruka='Nema termina'
    context={
        'poruka':poruka,
        'termini':termini1
    }

    return render(request, 'termini/termini.html', context)