from django.apps import AppConfig


class SocialsConfig(AppConfig):
    name = 'socials'

    def ready(self):
        import socials.templatetags.social_tags