from django.contrib.auth import authenticate,login
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages
from .models import FashionItem, UserProfile
from django.urls import reverse
from .utils.recommendation_engine import contents_based_recommender
import logging
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_POST


def logIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect(('home'))

        else:
            return render(request, '404.html')

    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        myuser = User.objects.create_user(username=username,password=password)

        myuser.save()

        messages.success(request, "New Account Created Successfully!")

        return redirect('logIn')
    return render(request, 'signup.html')



def home(request):
    generated_message = ""
    result = None

    if request.method == 'POST':
        if 'option1' in request.POST and 'option2' in request.POST and 'option3' in request.POST:
            category = request.POST.get('option1')
            item_type = request.POST.get('option2')
            gender = request.POST.get('option3')

            if category and item_type and gender:
                result = FashionItem.objects.filter(
                    category=category,
                    item_type=item_type,
                    gender=gender
                ).order_by('?').first()

                generated_message = "Outfit Generated!"

                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    if result:
                        response_data = {
                            'item_id': result.item_id,
                            'category': result.category,
                            'item_type': result.item_type,
                            'gender': result.gender,
                            'photo_path': result.photo_path,
                            'description': result.description,
                            'likes_count': result.likes_count,
                            'generated_message': generated_message,
                        }
                    else:
                        response_data = {'error': 'No result found'}
                    return JsonResponse(response_data)

    return render(request, 'home.html', {
        'result': result,
        'generated_message': generated_message,
        'email': request.user.email,
        'username': request.user.username,
    })

    
@csrf_exempt
def store_session(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            result_desc = data.get('resultDesc')
            if result_desc:
                request.session['resultDesc'] = result_desc
                return JsonResponse({'message': 'Session data stored successfully'})
            else:
                return JsonResponse({'error': 'No result description provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
def explore(request):

    result_desc = request.session.get('resultDesc')
    if result_desc:
        recommended_descriptions = contents_based_recommender(result_desc, 18)
        recommendations = FashionItem.objects.filter(description__in=recommended_descriptions).order_by('likes_count').reverse()
        return render(request, 'explore.html', {
            'recommendations': recommendations,
            'email': request.user.email,
            'username': request.user.username,})
    else:
        return JsonResponse({'error': 'No description found in session'}, status=400)

def like_item(request, item_id):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        item = get_object_or_404(FashionItem, item_id=item_id)  
        item.likes_count += 1
        item.save()
        return JsonResponse({'likes_count': item.likes_count})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)