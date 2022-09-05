from .views import AnimalViews, AnimalFamilyViews, AnimalclassViews, AnimalsViews, FamilyViews
from . import views
from rest_framework import routers
from django.urls import include, path


router = routers.DefaultRouter()
router.register(r'animal-get', AnimalViews)
router.register(r'animalfamily-get', AnimalFamilyViews)
router.register(r'animalclass-get', AnimalclassViews)
router.register(r'animals-get', AnimalsViews)
router.register(r'family-get', FamilyViews)

# specify URL Path for rest_framework

urlpatterns = [
    path('animal_add', views.Animal_add),
    path('my_animals', views.MyAnimals),
    path('', include(router.urls)),
]
