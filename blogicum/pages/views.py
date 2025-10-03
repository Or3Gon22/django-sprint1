from django.shortcuts import render


def about(request):
    """Render the About page."""
    template_name = 'pages/about.html'
    return render(request, template_name)


def rules(request):
    """Render the Rules page."""
    template_name = 'pages/rules.html'
    return render(request, template_name)
