

from django.http import HttpResponse
def hello_world(request, variant_number):
    """
    A simple view that returns a 'Hello World' response with the
    variant number included in the URL.
    """
    # The HttpResponse object is created with the desired string
    # and a status code of 200 is returned explicitly.
    return HttpResponse(f'Hello World {variant_number}', status=200)
