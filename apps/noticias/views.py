from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import  Post , Categoria, Web , Comentarios


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
            'web':obtenerWeb,

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
        
        #form=SocialCommentForm()
        
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

        
        try:
            publicacion = Comentarios.objects.all().filter(noticia=post)
            contar_comentarios=Comentarios.objects.all().filter(noticia=post).count()
        except:
            publicacion= None

        
        contexto={
            'publicacion':publicacion,
            'post':post,
            'post_recientes':post_recientes,
            'web':obtenerWeb,
            'contar_comentarios':contar_comentarios
            
        }
        return render(request,'noticias/post.html',contexto)

def Agregar_Comentario(request,slug):
        texto_c = request.POST.get('coment')
        noti = Post.objects.get(slug=slug)
        c = Comentarios.objects.create(noticia = noti, texto = texto_c, usuario = request.user)
        print(noti)
        return HttpResponseRedirect(reverse_lazy('noticias:detalle_post',kwargs={'slug':slug}))

