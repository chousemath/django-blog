from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def pub_date_formatted(self) -> str:
        return self.pub_date.strftime('%b %e %Y')

    def body_summary(self) -> str:
        return self.body[:100]

    def body_reverse(self) -> str:
        reversed_body = ''
        for c in self.body:
            reversed_body = c + reversed_body
        return reversed_body
