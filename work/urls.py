# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkExperienceViewSet
from . import views

router = DefaultRouter()
router.register(r'work_experience', WorkExperienceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.work_experience_view, name='work-experience'),
]
