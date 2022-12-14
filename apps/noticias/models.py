from django.db import models
from apps.usuarios.models import Usuario
# Create your models here.


class ModeloBase(models.Model):
    id = models.AutoField(primary_key = True)
    estado = models.BooleanField('Estado',default = True)
    fecha_creacion = models.DateField('Fecha de Creación',auto_now = False, auto_now_add = True)
    fecha_modificacion = models.DateField('Fecha de Modificación',auto_now = True, auto_now_add = False)
    fecha_eliminacion = models.DateField('Fecha de Eliminación',auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True

class Categoria(ModeloBase):
    nombre = models.CharField('Nombre de la Categoría', max_length = 100, unique = True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Autor(ModeloBase):
    nombre = models.CharField('Nombres',max_length = 100)
    apellidos = models.CharField('Apellidos',max_length = 120)
    email = models.EmailField('Correo Electrónico', max_length = 200)
    imagen_referencial = models.ImageField('Imagen Referencial', null = True, blank = True,upload_to = 'autores/')
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0},{1}'.format(self.apellidos,self.nombre)

class Post(ModeloBase):
    titulo = models.CharField('Título del Post',max_length = 150, unique = True)
    slug = models.CharField('Slug', max_length = 150, unique = True)
    descripcion = models.TextField('Descripción')
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    contenido = models.TextField()
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to = 'imagenes/', max_length = 255)
    publicado = models.BooleanField('Publicado / No Publicado',default = False)
    fecha_publicacion = models.DateField('Fecha de Publicación')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
    
    def obtener_mis_comentarios(self):
        return self.mis_comentarios.all()

class Comentarios(ModeloBase):
    noticia= models.ForeignKey(Post, related_name='mis_comentarios',on_delete=models.CASCADE)
    texto=models.TextField()
    creado=models.DateTimeField(auto_now_add=True)
    usuario= models.ForeignKey(Usuario, related_name= 'usuario_comentario', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'


    def __str__(self) :
        return self.texto
    


class Web(ModeloBase):
    nosotros = models.TextField('Nosotros')
    telefono = models.CharField('Teléfono', max_length = 10, null = True, blank = True)
    email = models.EmailField('Correo Electrónico', max_length = 200, null = True, blank = True)
    direccion = models.CharField('Dirección', max_length = 200, null = True, blank = True)
    facebook = models.URLField('Facebook',null = True, blank = True)
    twitter = models.URLField('Twitter',null = True, blank = True)
    instagram = models.URLField('Instagram',null = True, blank = True)

    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'

    def __str__(self):
        return self.nosotros
