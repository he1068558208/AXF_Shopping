from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=64,unique=True)
    sex = models.BooleanField(default=False)
    icon = models.ImageField(upload_to='icons')
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'axf_users'

class UserTicketModel(models.Model):
    user = models.ForeignKey(UserModel) # 关联用户
    ticket = models.CharField(max_length=256) # 密码
    out_time = models.DateTimeField() #过期时间

    class Meta:
        db_table = 'axf_users_ticket'