from django.db import models

class Topic(models.Model):
    text=models.CharField(max_length=147)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic=models.ForeignKey(
        "Topic",
        on_delete=models.DO_NOTHING,
    )
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="entries"
    
    def __str__(self):
        return self.text[:47]+"..."
