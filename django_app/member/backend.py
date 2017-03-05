from member.models import MyUser


class FacebookBackend():
    def authunticate(self, facebook_id, **extra_fields):
        user = MyUser.objects.get_or_create(
            username=facebook_id
        )
        return user

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(id=user_id)
        except MyUser.DoesNotExist:
            return None
