from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContentForm
from .models import Content
from .serializers import ContentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

def content_detail(request, content_id):
    content = get_object_or_404(Content, id=content_id)
    return render(request, 'content.html', {'content': content})

def add_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_content')            
    else:
        form = ContentForm()
    return render(request, 'add.html', {'form': form})

def view_content(request):
    search_query = request.GET.get('search', '')  # Get search query from request
    if search_query:
        # Filter by title instead of name
        contents = Content.objects.filter(title__icontains=search_query)  # Filter by title
    else:
        contents = Content.objects.all()
    return render(request, 'view.html', {'contents': contents, 'search_query': search_query})


@api_view(['GET', 'POST'])
def view_content_api(request):
    if request.method == 'GET':
        contents = Content.objects.all()
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        print("Request Data:", request.data)  # Debugging line
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

    



