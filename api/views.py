from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
from . import phq9
from django.shortcuts import render

arr_q = [
      {'index' : 1,'q' : 'Little interest or pleasure in doing things?'},
      {'index' : 2,'q' : 'Feeling down, depressed, or hopeless?'},
      {'index' : 3,'q' :'Trouble falling or staying asleep, or sleeping too much?'},
      {'index' : 4,'q' :'Feeling tired or having little energy?'},
      {'index' : 5,'q' :'Poor appetite or overeating?'},
      {'index' : 6,'q' :'Feeling bad about yourself - or that you are a failure or have let yourself or your family down?'},
      {'index' : 7,'q' :'Trouble concentrating on things, such as reading the newspaper or watching television?'},
      {'index' : 8,'q' :'Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual?'},
      {'index' : 9,'q' :'Thoughts that you would be better off dead, or of hurting yourself in some way?'}  
    ]

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.datac)

@api_view(['GET'])
def get_form(request):
    data = {}
    data['content'] = 'Over the last 2 weeks, how often have you been bothered by any of the following problems?'
    data['questions'] = arr_q
    # return Response(data)
    return render(request,'form/form.html',{'data': data})

@api_view(['GET'])
def home(request):
  return render(request,'home.html',{'name':'Sakthi'})

@api_view(['POST'])
def get_form_response(request):
    print(request.data)
    #process the data of the text in django

    #get the result and proceed to display 
    
    return Response('successful')
