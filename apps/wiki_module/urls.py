from django.urls import path

from apps.wiki_module.views import WikiDashboard, BlogDocList, CreateBlogDoc, \
    BlogDetail


urlpatterns = [
    path('dashboard/', WikiDashboard.as_view(), name='wiki_dashaboard'),

    path('blog_docs/list/', BlogDocList.as_view(), name='blog_doc_list'),
    path('blog_docs/new_blogdoc/', CreateBlogDoc.as_view(), name='new_blog_doc'),
    path('blog_docs/detail/<int:pk>/', BlogDetail.as_view(), name='blog_doc_detail'),
    #path('blog_docs/detail/<?P:key^[a-zA-Z0-9!@#$&()\\-`.+,/\"]*$>/', BlogDetail.as_view(), name='blog_doc_detail'),
]
