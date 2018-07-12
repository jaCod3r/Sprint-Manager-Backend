from .api import NoteViewSet, RegistrationAPI

urlpatterns = [
    url("^", include(router.urls)),
    url("^auth/register/$", RegistrationAPI.as_view()),
]
