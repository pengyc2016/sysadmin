#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import xlsxwriter
import xlwt
import itertools
from django.http import HttpResponse
import StringIO

headstyle = xlwt.easyxf("""
    font:
        name 'name Times New Roman',
        colour_index 7,
        bold True;
    align:
        wrap on,
        vert center,
        horiz left;
    pattern:
        pattern solid;
    """)

timestyle = xlwt.XFStyle()
timestyle.num_format_str = 'YYYY-MM-DD hh:mm'


def daochucluster(objs, fn):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet(u'集群信息')
    col_width = 256*15
    try:
        for i in itertools.count():
            sheet.col(i).width = col_width
    except ValueError:
        pass
    sheet.write(0, 0, '编号', headstyle)
    sheet.write(0, 1, '集群名', headstyle)
    sheet.write(0, 2, '平台', headstyle)
    sheet.write(0, 3, '管理地址', headstyle)
    sheet.write(0, 4, '总存储', headstyle)
    sheet.write(0, 5, '可用存储', headstyle)
    sheet.write(0, 6, '已用存储', headstyle)
    sheet.write(0, 7, '总核数', headstyle)
    sheet.write(0, 8, '可用核数', headstyle)
    sheet.write(0, 9, '已用核数', headstyle)
    sheet.write(0, 10, '总内存', headstyle)
    sheet.write(0, 11, '可用内存', headstyle)
    sheet.write(0, 12, '已用内存', headstyle)
    sheet.write(0, 13, '所属存储组', headstyle)
    sheet.write(0, 14, '所属网络组', headstyle)
    sheet.write(0, 15, '备注', headstyle)
    row = 1
    for i in objs:
        sheet.write(row, 0, i.id)
        sheet.write(row, 1, i.clustername)
        sheet.write(row, 2, i.platform)
        sheet.write(row, 3, i.vcaddress)
        sheet.write(row, 4, i.ttstorage)
        sheet.write(row, 5, i.systorage)
        sheet.write(row, 6, i.usedstorage)
        sheet.write(row, 7, i.ttcore)
        sheet.write(row, 8, i.sycore)
        sheet.write(row, 9, i.usedcore)
        sheet.write(row, 10, i.ttmem)
        sheet.write(row, 11, i.symem)
        sheet.write(row, 12, i.usedmem)
        sheet.write(row, 13, i.storagegroup_id)
        sheet.write(row, 14, i.vlangroup_id)
        sheet.write(row, 15, i.remark)
        row=row+1
    output = StringIO.StringIO()
    book.save(output)
    output.seek(0)
    response = HttpResponse(output.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=%s' %fn
    return response


def daochuvm(objs, fn):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet(u'虚拟机信息')
    col_width = 256*15
    try:
        for i in itertools.count():
            sheet.col(i).width = col_width
    except ValueError:
        pass
    sheet.write(0, 0, '编号', headstyle)
    sheet.write(0, 1, '虚拟机名称', headstyle)
    sheet.write(0, 2, '所属物理机', headstyle)
    sheet.write(0, 3, '所属集群', headstyle)
    sheet.write(0, 4, '所属项目', headstyle)
    sheet.write(0, 5, '角色', headstyle)
    sheet.write(0, 6, '批次', headstyle)
    sheet.write(0, 7, '环境', headstyle)
    sheet.write(0, 8, '操作系统', headstyle)
    sheet.write(0, 9, '安装软件', headstyle)
    sheet.write(0, 10, 'CPU', headstyle)
    sheet.write(0, 11, '内存', headstyle)
    sheet.write(0, 12, '磁盘', headstyle)
    sheet.write(0, 13, 'IP地址', headstyle)
    sheet.write(0, 14, '子网掩码', headstyle)
    sheet.write(0, 15, '网关', headstyle)
    sheet.write(0, 16, '所属域', headstyle)
    sheet.write(0, 17, '管理员', headstyle)
    sheet.write(0, 18, '应用用户', headstyle)
    sheet.write(0, 19, '备注', headstyle)
    row = 1
    for i in objs:
        sheet.write(row, 0, i.id)
        sheet.write(row, 1, i.vmname)
        sheet.write(row, 2, i.pm_id)
        sheet.write(row, 3, i.cluster_id)
        sheet.write(row, 4, i.project_id)
        sheet.write(row, 5, i.role)
        sheet.write(row, 6, i.batch)
        sheet.write(row, 7, i.env)
        sheet.write(row, 8, i.os)
        sheet.write(row, 9, i.soft_id)
        sheet.write(row, 10, i.cpu)
        sheet.write(row, 11, i.mem)
        sheet.write(row, 12, i.disk)
        sheet.write(row, 13, i.ip)
        sheet.write(row, 14, i.mask)
        sheet.write(row, 15, i.gateway)
        sheet.write(row, 16, i.domain_id)
        sheet.write(row, 17, i.admin)
        sheet.write(row, 18, i.appuser)
        sheet.write(row, 19, i.remark)
        row = row+1
    output = StringIO.StringIO()
    book.save(output)
    output.seek(0)
    response = HttpResponse(output.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=%s' % fn
    return response


def daochupm(objs, fn):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet(u'物理机信息')
    col_width = 256*15
    try:
        for i in itertools.count():
            sheet.col(i).width = col_width
    except ValueError:
        pass
    sheet.write(0, 0, '编号', headstyle)
    sheet.write(0, 1, '物理机名称', headstyle)
    sheet.write(0, 2, '序列号', headstyle)
    sheet.write(0, 3, '功能', headstyle)
    sheet.write(0, 4, '设备类型', headstyle)
    sheet.write(0, 5, 'CPU', headstyle)
    sheet.write(0, 6, '内存', headstyle)
    sheet.write(0, 7, '磁盘', headstyle)
    sheet.write(0, 8, '操作系统', headstyle)
    sheet.write(0, 9, '网卡数', headstyle)
    sheet.write(0, 10, 'HBA卡数', headstyle)
    sheet.write(0, 11, 'IP地址', headstyle)
    sheet.write(0, 12, '管理地址', headstyle)
    sheet.write(0, 13, '子网掩码', headstyle)
    sheet.write(0, 14, '网关', headstyle)
    sheet.write(0, 15, '机柜号', headstyle)
    sheet.write(0, 16, '机柜位', headstyle)
    sheet.write(0, 17, 'HBA卡WWN', headstyle)
    sheet.write(0, 18, '机房', headstyle)
    sheet.write(0, 19, '存储', headstyle)
    sheet.write(0, 20, '剩余存储', headstyle)
    sheet.write(0, 21, '剩余核数', headstyle)
    sheet.write(0, 22, '剩余内存', headstyle)
    sheet.write(0, 23, '所属集群', headstyle)
    sheet.write(0, 24, '所属域', headstyle)
    sheet.write(0, 25, '所属项目', headstyle)
    sheet.write(0, 26, '安装软件', headstyle)
    sheet.write(0, 27, '所属存储组', headstyle)
    sheet.write(0, 28, '所属网络组', headstyle)
    sheet.write(0, 29, '备注', headstyle)
    row = 1
    for i in objs:
        sheet.write(row, 0, i.id)
        sheet.write(row, 1, i.pmname)
        sheet.write(row, 2, i.sn)
        sheet.write(row, 3, i.role)
        sheet.write(row, 4, i.type)
        sheet.write(row, 5, i.cpu)
        sheet.write(row, 6, i.memory)
        sheet.write(row, 7, i.disk)
        sheet.write(row, 8, i.os)
        sheet.write(row, 9, i.eth)
        sheet.write(row, 10, i.hba)
        sheet.write(row, 11, i.ip)
        sheet.write(row, 12, i.ilo_ip)
        sheet.write(row, 13, i.mask)
        sheet.write(row, 14, i.gateway)
        sheet.write(row, 15, i.jiguihao)
        sheet.write(row, 16, i.jiguiwei)
        sheet.write(row, 17, i.hba_wwn)
        sheet.write(row, 18, i.position)
        sheet.write(row, 19, i.ttstorage)
        sheet.write(row, 20, i.systorage)
        sheet.write(row, 21, i.sycore)
        sheet.write(row, 22, i.symem)
        sheet.write(row, 23, i.cluster_id)
        sheet.write(row, 24, i.domain_id)
        sheet.write(row, 25, i.project_id)
        sheet.write(row, 26, i.soft_id)
        sheet.write(row, 27, i.storagegroup_id)
        sheet.write(row, 28, i.vlangroup_id)
        sheet.write(row, 29, i.remark)
        row=row+1
    output = StringIO.StringIO()
    book.save(output)
    output.seek(0)
    response = HttpResponse(output.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=%s' % fn
    return response


def daochuproject(objs, fn):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet(u'项目信息')
    col_width = 256*15
    try:
        for i in itertools.count():
            sheet.col(i).width = col_width
    except ValueError:
        pass
    sheet.write(0, 0, '项目编号', headstyle)
    sheet.write(0, 1, '项目名', headstyle)
    sheet.write(0, 2, '环境', headstyle)
    sheet.write(0, 3, '项目简称', headstyle)
    sheet.write(0, 4, '项目起始时间', headstyle)
    sheet.write(0, 5, '项目截止时间', headstyle)
    sheet.write(0, 6, '项目完成时间', headstyle)
    sheet.write(0, 7, '超时理由', headstyle)
    sheet.write(0, 8, '批次', headstyle)
    sheet.write(0, 9, '搭建人员', headstyle)
    sheet.write(0, 10, '备注', headstyle)
    row = 1
    for i in objs:
        sheet.write(row, 0, i.id)
        sheet.write(row, 1, i.projectname)
        sheet.write(row, 2, i.env)
        sheet.write(row, 3, i.shortname)
        sheet.write(row, 4, i.starttime, timestyle)
        sheet.write(row, 5, i.endtime, timestyle)
        sheet.write(row, 6, i.finishtime, timestyle)
        sheet.write(row, 7, i.reason)
        sheet.write(row, 8, i.batch)
        sheet.write(row, 9, i.createuser_id)
        sheet.write(row, 10, i.remark)
        row = row+1
    output = StringIO.StringIO()
    book.save(output)
    output.seek(0)
    response = HttpResponse(output.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=%s' % fn
    return response

