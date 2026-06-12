from django.db import models


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=31, unique=True)
    slug  = models.SlugField(max_length=31, unique_for_date='created_at')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Post(BaseModel):

    category     = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='posts')

    title        = models.CharField(max_length=255)
    slug         = models.SlugField(max_length=255, unique_for_date='created_at')

    content      = models.TextField()
    author       = models.CharField(max_length=255)
    image        = models.ImageField(upload_to='posts/')
    views        = models.IntegerField(default=0)

    published_at = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title