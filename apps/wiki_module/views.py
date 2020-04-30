from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.models import User

from django.db import transaction
from django.db.models import Sum

from django.urls import reverse_lazy

from django.utils import timezone

from django.http import HttpResponseRedirect

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView


from apps.wiki_module.models import  BlogDoc, ArticleFile
from apps.wiki_module.forms import BlogDocForm


class WikiDashboard(View):

    def get(self, request):
        context = {}
        context['wiki_dashboard'] = True

        total_blogs = BlogDoc.objects.filter(status='active').count()
        total_articles = ArticleFile.objects.filter(status='active').count()

        context['total_docs'] = total_blogs + total_articles

        context['total_blog_docs'] = total_blogs
        context['total_blog_docs_views'] = BlogDoc.objects.filter(status='active').\
            aggregate(Sum('views'))['views__sum']
        context['total_articles'] = total_articles
        context['total_articles_views'] = ArticleFile.objects.filter(status='active').\
            aggregate(Sum('views'))['views__sum']
        return render(request, 'wiki_dashboard.html', context)


class BlogDocList(ListView):

    model = BlogDoc
    template_name = 'blog_docs/blog_doc_list.html'
    queryset = BlogDoc.objects.filter(status='active')
    paginated_by = 100 #fix

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_doc_list'] = True
        return context


class CreateBlogDoc(CreateView):

    model = BlogDoc
    template_name = 'blog_docs/blog_doc_form.html'
    form_class  = BlogDocForm
    success_url = reverse_lazy('wiki_module:blog_doc_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_blog_doc'] = True
        return context

    def form_valid(self, form):

        cap_title = form.instance.title.capitalize()

        form.instance.created_by = self.request.user
        form.instance.title = cap_title

        if not BlogDoc.objects.filter(status='active', title=cap_title):
            messages.success(self.request, 'Blog '+ cap_title +' created successfully!')
            return super().form_valid(form)
        else:
            messages.warning(self.request, 'Blog '+ cap_title +' already exist, let´s try with another one')

            form = BlogDocForm(data=self.request.POST.copy())
            context = {}
            context['new_blog_doc'] = True
            context['form'] = form
            return render(self.request, 'blogdoc_form.html', context)


class BlogDetail(DetailView):

        model = BlogDoc
        template_name = 'blog_docs/blog_doc_detail.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            blog = BlogDoc.objects.get(id=self.kwargs.get('pk'))

            if blog.views == None:
                blog.views = 1
            else:
                blog.views = blog.views + 1
            blog.save()
            return context
