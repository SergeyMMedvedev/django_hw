from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    
    name = models.CharField(max_length=30, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank = True)
    image = models.ImageField(null = True, blank = True)
    release_date = models.DateField(null = True, blank = True)
    lte_exists  = models.BooleanField(null = True, blank = True)
    slug = models.SlugField(default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
