from django.shortcuts import render, redirect, get_object_or_404
from .models import Essay, Category
from .forms import EssayForm

def essay_list(request):
    essays = Essay.objects.all()
    return render(request, 'archiveapp/essay_list.html', {'essays': essays})

def upload_essay(request):
    if request.method == 'POST':
        form = EssayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('essay_list')
    else:
        form = EssayForm()
    return render(request, 'archiveapp/upload_essay.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'archiveapp/category_list.html', {'categories': categories})

def essays_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    essays = Essay.objects.filter(category=category)
    return render(request, 'archiveapp/essays_by_category.html', {'category': category, 'essays': essays})
