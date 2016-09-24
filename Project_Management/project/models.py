from django.db import models
from user.models import UserInfo


class ProjectInfo(models.Model):
    team_leader = models.CharField(UserInfo, max_length=50)