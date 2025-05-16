from django.db import models

class Message(models.Model):
    name = models.CharField("Имя", max_length=20)
    email = models.EmailField("Email address", unique=True)
    text = models.TextField("Сообщение")
    created_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'