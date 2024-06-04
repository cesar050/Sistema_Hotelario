from django.shortcuts import render

def example_view(request):
    return render(request, 'adminHotel/example_template.html')
