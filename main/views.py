from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Zaidan Naufal Ilmi',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
