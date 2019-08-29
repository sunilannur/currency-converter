
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

def currency_converter(request):
    curr_req = requests.get("http://data.fixer.io/api/latest?access_key=40eac7a32ba84e0369830d99248246b7")
    currency_json = json.loads(curr_req.text)
    currency_rate_dict = currency_json['rates']
    list_of_country_currency_code = [x for x in currency_rate_dict.keys()]

    output = ""
    if request.method == "POST":
        source_currency_code = request.POST['source_currency']
        target_currency_code = request.POST['target_currency']

        input_currency_value = request.POST['amount']

        base_key = currency_json['base']
        base_value = currency_rate_dict[base_key]

        source_currency_base_value = currency_rate_dict[source_currency_code]
        target_currency_base_value = currency_rate_dict[target_currency_code]

        output = (target_currency_base_value / source_currency_base_value) * float(input_currency_value)


    context = {
        'list_of_country_currency_code': list_of_country_currency_code,
        'output':output
    }
    return render(request, 'money/currency-converter.html', context)