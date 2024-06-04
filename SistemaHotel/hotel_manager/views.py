from django.shortcuts import render

def another_example_view(request):
    return render(request, 'hotel_manager/another_template.html')
