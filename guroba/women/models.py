from django.db import models

class Women(models.Model):
    title        = models.CharField(max_length=255)
    content      = models.TextField(blank=True)
    photo        = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create  = models.DateTimeField(auto_now_add=True)
    time_update  = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    slug         = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    category     = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['title']

class Category(models.Model):
    name = models.CharField(max_length=1000, db_index=True, verbose_name='Категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']

def addedWomen():
    women = Women(title="Дженифер Энистон", content='Актриса и певицы')
    women.save()
    Women.objects.create(title="Дженифер Энистон", content='Актриса и певицы')