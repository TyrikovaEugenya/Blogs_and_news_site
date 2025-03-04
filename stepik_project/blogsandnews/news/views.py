from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from  django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Articles.objects.order_by('-date')[:5] ## Получение объектов модели
    return render(request, 'news/news_home.html', {'news': news})

def create_new(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is invalid'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create_new.html', data)

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create_new.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete_new.html'
    success_url = '/news/'