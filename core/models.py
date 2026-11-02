from django.db import models

SERVICES = [
    ("standard", "Standard home cleaning"), ("deep", "Deep cleaning"),
    ("move", "Move-in / move-out cleaning"), ("office", "Office & commercial cleaning"),
    ("post", "Post-construction cleaning"), ("recurring", "Recurring plans"),
    ("other", "Something else"),
]

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    service = models.CharField(max_length=20, choices=SERVICES, default="standard")
    message = models.TextField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} - {self.get_service_display()} ({self.created:%Y-%m-%d})"
