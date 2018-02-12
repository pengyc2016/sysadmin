#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class TongJi(models.Model):
    tongjitype = models.CharField(max_length=50, unique=True, db_index=True, verbose_name=u'统计类型')
    count = models.IntegerField(blank=True, null=True, verbose_name=u'统计数量')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'备注')

    def __unicode__(self):
        return self.tongjitype

    class Meta:
        db_table = 'tongji'
        ordering = ['-id']
