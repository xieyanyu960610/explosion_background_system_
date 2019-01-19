from django.db import models
from datetime import datetime

from apps.basic.models import *
from apps.evi.models import *
# Create your models here.

class userMessage(models.Model):
    """
    站内消息信息表
    """
    sendUser = models.ForeignKey(userProfile, verbose_name=u"发件人",related_name="sendUser")
    receiveUser = models.ForeignKey(userProfile, verbose_name=u"收件人",related_name="receiveUser")
    title =models.CharField(max_length=50,verbose_name="消息标题")
    message =models.CharField(max_length=500,verbose_name="消息内容")
    exploEviId = models.IntegerField(null=True, blank=True,verbose_name=u"所涉及的炸药物证")
    devEviId = models.IntegerField(null=True, blank=True,verbose_name=u"所涉及的爆炸装置物证")
    hasRead = models.BooleanField(default=False, verbose_name="是否已读")
    hasHandle = models.BooleanField(default=False, verbose_name="是否处理")
    sendDate =models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = "站内消息信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


