"""Platzigram views."""

# Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json

def hello_world(request):
    """ Return greetings """
    return HttpResponse(datetime.now().strftime('%b %dth, %Y - %H: %M hrs'))


def hi(request):
    """ Hi """
    list_of_numbers = request.GET['numbers'].split(',')
    ans = sorted([int(i) for i in list_of_numbers])

    data = {
        'status': 'ok',
        'numbers': ans,
        'message': 'Integers sorted successfully'
    }

    return HttpResponse(json.dumps(data, ident=4), content_type='application/json')


def params(request, name, age):

    return HttpResponse('Tienes {age}, {name}'.format(age=age, name=name))