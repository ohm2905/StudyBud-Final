from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Topic

@receiver(post_migrate)
def create_default_topics(sender, **kwargs):
    default_topics = [
        "Python",
        "Django",
        "Machine Learning",
        "AI",
        "JavaScript",
        "C++",
        "Java",
        "Flutter"
    ]

    for t in default_topics:
        Topic.objects.get_or_create(name=t)
