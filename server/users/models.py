import hashlib
import urllib
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from core.models import BaseModel

# Create your models here.


class User(BaseModel, AbstractUser):
    uuid = models.UUIDField(_("UUID"), editable=False, default=uuid.uuid4)
    jwt = models.TextField(unique=True, null=True, blank=True)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "users"

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"uuid": self.uuid})

    def get_gravatar_url(self, size=150):
        default = (
            "https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y"
        )
        return "https://www.gravatar.com/avatar/%s?%s" % (
            hashlib.md5(self.email.lower().encode("utf-8")).hexdigest(),
            urllib.parse.urlencode({"d": default, "s": str(size)}),
        )
