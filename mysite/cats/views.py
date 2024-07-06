
from cats.models import Breed
from cats.models import Cat
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


class BreedList(LoginRequiredMixin, View):
    def get(self, request):
        breed_list = Breed.objects.all()
        ctx = {"breed_list": breed_list}
        return render(request, "cats/breed_list.html", ctx)


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class CatList(LoginRequiredMixin, View):
    def get(self, request):
        cat_list = Cat.objects.all()
        breed_count = Breed.objects.count()

        ctx = {"cat_list": cat_list, "breed_count": breed_count}
        return render(request, "cats/cat_list.html", ctx)


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")
