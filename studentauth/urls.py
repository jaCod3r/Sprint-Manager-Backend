urlpatterns = [
    url(r'^api/', include(endpoints)),
    url(r'^api/auth/', include('studentauth.urls')),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]
