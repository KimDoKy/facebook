from django.contrib.auth.models import AbstractUser


# class MyUserManager(UserManager):
#     def create_facebook_user(
#             self,
#             social_id,
#             user_type,
#             email=None,
#             password=None,
#             **extra_fields):
#         extra_username = get_random_string(10)
#
#         return super().create_user(
#             username='{}{}'.format(social_id, extra_username),
#             social_id=social_id,
#             user_type=user_type,
#             email=email,
#             password=password,
#             **extra_fields
#         )



class MyUser(AbstractUser):
    pass
    # CHOICE_USER_TYPE = (
    #     ('django', 'Django'),
    #     ('facebook', 'Facebook'),
    # )
    # social_id = models.CharField(max_length=100, blank=True)
    # user_type = models.CharField(
    #     max_length=15,
    #     choices=CHOICE_USER_TYPE,
    #     default=CHOICE_USER_TYPE[0][0]
    # )
