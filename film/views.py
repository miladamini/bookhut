from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import FilmModel, zerfilm, Comments_film


# Create your views here.


class FilmView(View):
    def get(self, request):
        film = FilmModel.objects.all()
        page_number = request.GET.get('page')
        page = Paginator(film, 3)
        object_list = page.get_page(page_number)
        return render(request, 'categorefilm.html', {'film': object_list})


class DitaylFilm(View):
    def get(self, request, slug):
        Film = get_object_or_404(FilmModel, slug=slug)
        rom = zerfilm.objects.order_by('a_id').filter(father=Film)
        po = Comments_film.objects.filter(articel=Film).count()
        po2 = Comments_film.objects.filter(articel=Film)

        return render(request, 'ditileFilm.html', {'film': Film, 'rom': rom, 'po': po, 'po2': po2})

    def post(self, request, slug):
        Film = get_object_or_404(FilmModel, slug=slug)
        text = request.POST.get('text')
        name = request.POST.get('name')
        parent = request.POST.get('parent')
        if request.user.is_admin == True:
            Comments_film.objects.create(articel=Film, user=request.user, name=name, parent_id=parent, text=text,
                                         user_admin=True)
        else:
            Comments_film.objects.create(articel=Film, user=request.user, name=name, parent_id=parent, text=text)

        return redirect(request.path_info)
