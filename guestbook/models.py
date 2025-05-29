from django.db import models

class Message(models.Model):
    name = models.CharField("Имя", max_length=20)
    email = models.EmailField("Email address")
    text = models.TextField("Сообщение")
    created_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=False)
    avatar = models.ImageField(verbose_name="Картинка аватара", upload_to="avatars/img_box", blank=True, null=True)
    admin_reply = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'