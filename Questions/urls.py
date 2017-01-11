from django.conf.urls import url
from .views import LoginPage, RegisterPage, QuestionsPage, ResultPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', LoginPage),

    url(r'^RegisterPage', RegisterPage),

    url(r'^LoginPage', LoginPage),

    url(r'^QuestionsPage', QuestionsPage),

    url(r'^ResultPage', ResultPage)


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)