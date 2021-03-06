from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Article
from django.urls import reverse_lazy
# Create your views here.

class ArticleListView(ListView):
	model = Article
	template_name = 'home.html'

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'detail.html'
	context_object_name = 'batwomen'

class ArticleCreateView(CreateView):
	model = Article
	template_name = 'article_new.html'
	fields = '__all__'

class ArticleUpdateView(UpdateView):
	model = Article
	template_name = 'article_edit.html'
	fields = ['title', 'text']

class ArticleDeleteView(DeleteView):
	model = Article
	template_name = 'article_delete.html'
	context_object_name = 'batwomen'
	success_url = reverse_lazy('home')



	