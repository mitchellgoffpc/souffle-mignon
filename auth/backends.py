from django.contrib.auth.backends import ModelBackend

from auth.models import User


# Custom backend to handle Twitter auth
class TwitterBackend(ModelBackend):
    def authenticate(self, twitter=None):
        if twitter is None:
            return None

        try:
            user = User.objects.get(twitter_id=twitter['id'])
        except User.DoesNotExist:
            user = User(username=twitter['id'], twitter_id=twitter['id'], is_staff=False)

        user.name = twitter['name']
        user.picture = twitter['profile_image_url_https']
        user.save()

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None



# Custom backend to handle Facebook auth
class FacebookBackend(ModelBackend):
    def authenticate(self, facebook=None):
        if facebook is None:
            return None

        try:
            user = User.objects.get(facebook_id=facebook['id'])
        except User.DoesNotExist:
            user = User(username=facebook['id'], facebook_id=facebook['id'], is_staff=False)

        user.name = facebook['name']
        user.picture = facebook['picture']['data']['url']
        user.save()

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
