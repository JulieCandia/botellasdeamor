from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.core.paginator import Paginator
from .models import  Post , Categoria , Web



def obtenerWeb():
    return Web.objects.filter(estado = True).latest('fecha_creacion')

class Noticias(ListView):

    def get(self,request,*args,**kwargs):
        posts=Post.objects.filter(
               estado=True,
               publicado=True,
               )
        paginator = Paginator(posts,3)
        pagina=request.GET.get('page')
        posts=paginator.get_page(pagina)


        try:
            post_recientes = Post.objects.filter(
                                estado = True,
                                publicado = True,
                                ).order_by('-fecha_publicacion')[:6]
        except:
            post_recientes = None
        contexto={
            'posts':posts,
            'post_recientes':post_recientes,
            'web':obtenerWeb

        }

        #posts=list(Post.objects.filter( 
         #     fecha_publicacion__range=['2022-08-2', '2022-08-24']
          #    ).values_list('id',flat=True))
        #print(posts)

        return render(request, 'noticias/listar_noticias.html',contexto)

def generarListado(request,nombre):
    posts=Post.objects.filter(
            estado=True,
            publicado=True,
            categoria=Categoria.objects.get(nombre=nombre)
    )
    try:
        categoria = Categoria.objects.get(nombre = nombre)
    except:
        categoria = None
    paginator = Paginator(posts,3)
    pagina=request.GET.get('page')
    posts=paginator.get_page(pagina)

    try:
        post_recientes = Post.objects.filter(
                            estado = True,
                            publicado = True,
                            ).order_by('-fecha_publicacion')[:6]
    except:
        post_recientes = None

    contexto={
    'posts':posts,
    'categoria':categoria,
    'post_recientes':post_recientes,
    'web':obtenerWeb
        }
    return contexto

class Listado(ListView):
    def get(self,request,nombre,*args,**kwargs):
        contexto=generarListado(request,nombre)
        return render(request,'noticias/categoria.html',contexto)


class DetallePost(DetailView):
    def get(self,request,slug,*args,**kwargs):
        try:
            post=Post.objects.get(slug=slug)
        except:
            post=None
        

        try:
            post_recientes = Post.objects.filter(
                            estado = True,
                            publicado = True
                            ).order_by('-fecha_publicacion')[:6]
        except:
            post_recientes = None

        contexto={
            'post':post,
            'post_recientes':post_recientes,
            'web':obtenerWeb
        }
        return render(request,'noticias/post.html',contexto)

