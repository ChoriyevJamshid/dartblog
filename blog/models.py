from django.db import models
from django.utils import timezone

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
    views        = models.IntegerField(default=0, editable=False)

    published_at = models.DateTimeField(blank=True, null=True, editable=False)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):

        if self.is_published and self.published_at is None:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title