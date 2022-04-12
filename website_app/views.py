from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from website_app.models import Category, Subcategory, Post
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

def index(request):
    return redirect('/categories')

def error(request, err):
    error_data = {'err' : err}
    return render(request, 'pages/error.html', error_data)

def categories(request):
    categories = { 'categories' : Category.objects.all()}
    return render(request, 'pages/index.html', categories)

def category(request, category_pk):
    category = { 'category' : Category.objects.get(id=category_pk)}
    return render(request, 'pages/category.html', category)

def subcategory(request, category_pk, subcategory_pk):
    subcategory = { 'subcategory' : Subcategory.objects.get(id=subcategory_pk)}
    return render(request, 'pages/subcategory.html', subcategory)

def post(request, category_pk, subcategory_pk, post_pk):
    post = { 'post' : Post.objects.get(id=post_pk)}
    return render(request, 'pages/post.html', post)

def category_new(request):
    if request.method == "POST": 
        try:
            new_name = request.POST['name'].lower()
            new_description = request.POST['description'].lower()
            new_record = Category(name=new_name, description=new_description)
            new_record.full_clean()
            new_record.save()
            return redirect('category', new_record.id)
        except ValidationError as e:
            return redirect('error_page', e)
    else:
        category_name = {
            'fieldname' : 'name',
        }
        category_desc = {
            'fieldname' : 'description',
        }
        data = { 
            'action'    : 'create',
            'required_fields' : [category_name, category_desc]
        }
    return render(request, 'pages/category_form.html', data)

def post_new(request, category_pk, subcategory_pk):
    if request.method == "POST": 
        try:
            post_subcategory = Subcategory.objects.get(id=subcategory_pk)
            post_description = request.POST['post'].lower()
            post_form = Post(description=post_description, subcategory=post_subcategory)
            post_form.full_clean()
            post_form.save()
            return redirect('post', category_pk, subcategory_pk, post_form.id)
        except ValidationError as e:
            return redirect('error_page', e)
    else:
        subcategory_dict = {
            'name' : 'subcategory',
            'value' : Subcategory.objects.get(id=subcategory_pk).name 
        }
        category_dict = {
            'name' : 'category',
            'value' : Category.objects.get(id=category_pk).name
        }
        post_dict = {
            'name'  : 'post',
            'value' : ''
        }
        data = {
            'action'          : 'create',
            'required_fields' : [category_dict, subcategory_dict, post_dict],
            }
        return render(request, 'pages/post_form.html', data)

def post_edit(request, category_pk, subcategory_pk, post_pk):
    if request.method == "POST":
        try:
            edited_post = Post.objects.get(id = post_pk)
            edited_post.description = request.POST['post'].lower()
            edited_post.full_clean()
            edited_post.save()
            return redirect('post', category_pk, subcategory_pk, edited_post.id)
        except ValidationError as e:
            return redirect('error_page', e)
    else:
        subcategory_dict = {
            'name' : 'subcategory',
            'value' : Subcategory.objects.get(id=subcategory_pk).name 
        }
        category_dict = {
            'name' : 'category',
            'value' : Category.objects.get(id=category_pk).name
        }
        post = {
            'name'  : 'post',
            'value' : Post.objects.get(id=post_pk).description
        }
        data = {
            'action'          : 'edit',
            'required_fields' : [category_dict, subcategory_dict, post],
            }
        return render(request, 'pages/post_form.html', data)

def category_edit(request, category_pk):
    if request.method == "POST":
        try:
            edited_category = Category.objects.get(id = category_pk)
            edited_category.description = request.POST['description'].lower()
            edited_category.name = request.POST['name'].lower()
            edited_category.full_clean()
            edited_category.save()
            print(f'\n\n\n\n\n------{edited_category.name}------\n\n\n\n\n')
            return redirect('category', category_pk)
        except ValidationError as e:
            return redirect('error_page', e)
    else:
        category_record = Category.objects.get(id=category_pk)
        category_name = {
            'fieldname' : 'name',
            'value'     : category_record.name
        }
        category_desc = {
            'fieldname' : 'description',
            'value'     : category_record.description 
        }
        data = { 
            'action'    : 'edit',
            'required_fields' : [category_name, category_desc]
        }
        return render(request, 'pages/category_form.html', data )

@csrf_exempt
def delete_record(request, model_name, model_pk):
    if request.method == "POST":
        if model_name == 'post':
            Post.objects.get(id=model_pk).delete()
            return HttpResponse('200')
        elif model_name == 'category':
            Category.objects.get(id=model_pk).delete()
            return HttpResponse('200')
        elif model_name == 'subcategory':
            Subcategory.objects.get(id=model_pk).delete()
            return HttpResponse('200')   