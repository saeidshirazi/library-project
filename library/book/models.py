from django.db import models
import uuid
# Create your models here.

class Genre(models.Model):
    name = models.CharField( max_length=50, help_text='Enter a book genre')

    def __str__(self):
        return self.name
############################################################################
class Book(models.Model):
    title = models.CharField(max_lenght = 200)  
    summary = models.TextField(max_length=1000, help_text='Enter a brief Descriptions')
    isbn = models.CharField(max_lenght= 13 )
    genre = models.ManyToManyField(Genre,help_text= 'enter genre of this book')
    author = models.ForeignKey('Author',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title
############################################################################
class Author(models.Model):
    first_name = models.CharField(max_lenght=100)
    last_name  = models.CharField(max_lenght=100)
    data_of_birth = models.DateField(null=True,blank=True)
    data_of_death = models.DateField(null=True,blank=True)
    def __str__(self):
        return '{0},{1}'.format(self.last_name,self.first_name)
    class Meta:
        ordering=['last_name','first_name']    
############################################################################
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,
                          help_text='unique id for each book in lib')
    book = models.ForeignKey('Book', null=True, on_delete=models.CASCADE)
    print_detail = models.CharField(max_length=200)
    due_back = models.DateTimeField(null=True,blank=True)
    Book_Status=(
        ('m','Maintenance'),
        ('o','on loan'),
        ('a','Available'),
        ('r','Reserved' ),

    ) 
    status = models.CharField(maxlength=1,
                              choices= Book_Status,
                              blank=True,
                              default='m',
                              help_text='book availibility')

    class Meta:
        ordering =['Book_Status'] 
    def __str__(self):
        return '{0} ({1})'.format(self.id,self.Book.title)
    
    
