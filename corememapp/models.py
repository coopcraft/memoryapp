from django.db import models

class Memory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    bodytext = models.TextField('Memory Content', blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    # def get_absolute_url(self):
    #     """Returns the url to access a particular author instance."""
    #     # E.g. url = "/audios/author/3"
    #     url = reverse('author-detail', args=[str(self.id)])
    #     return url

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'