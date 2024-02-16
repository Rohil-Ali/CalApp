from django.shortcuts import render

#YlE/R8qeFrc8dsFiKSk+SQ==tm1aS030tJ3yauI6
# Create your views here.
def home(request):

    import requests
    import json
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'YlE/R8qeFrc8dsFiKSk+SQ==tm1aS030tJ3yauI6'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = 'There was an error!'
            print(e)
        return render(request, 'home.html', {'api':api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
 
