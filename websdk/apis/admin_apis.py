#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018年2月5日13:37:54
Desc    ：记录API
"""


class AdminAPIS:
    route_prefix = "/api/mg/"
    get_users = dict(method='GET',
                     url=f'{route_prefix}/v3/accounts/user/',
                     params={
                         'page': 1,
                         'limit': 201
                     },
                     field_help={},
                     description='获取用户信息')

    opt_users = dict(method='POST',
                     url=f'{route_prefix}/v3/accounts/user/',
                     body={
                         'username': None,
                         'nickname': None,
                         'password': None,
                         'department': None,
                         'tel': None,
                         'wechat': None,
                         'no': None,
                         'email': None,
                         'user_state': '20',
                     },
                     field_help={
                         'user_state': '20',
                     },
                     description='操作用户数据，支持增删改，请修改method和body数据')

    get_resource_info_by_user = dict(method='GET',
                                     url='/mg/v2/overall/resource/user/',
                                     params={
                                         'nickname': None,  ## 默认为当前用户有权限的
                                         'expand': None  ## yes 是扩展为目录的 ， no 是可以当全局标签的
                                     },
                                     field_help={
                                         'nickname': None,  ## 默认为当前用户有权限的
                                         'expand': None  ## yes 是扩展为目录的 ， no 是可以当全局标签的，没有则是全部
                                     },
                                     description='获取用户有权限的资源组/目录')

    get_resource_info = dict(method='GET',
                             url='/mg/v2/overall/resource/',
                             params={
                                 'key': None,  ## 筛选字段
                                 'value': None  ## 筛选字段值
                             },
                             field_help={
                                 'key': None,  ## 筛选字段
                                 'value': None  ## 筛选字段值
                             },
                             description='获取资源组/目录')

    get_all_role_user = dict(method='GET',
                             url=f'{route_prefix}/v3/accounts/all_role_user/',
                             params={
                             },
                             field_help={
                                 'page': '分页/第几页',  ### 分页/第几页
                                 'limit': '分页/每页多少个',  ### 分页/每页多少个
                                 'value': '模糊查询'  ### 模糊查询
                             },
                             description='获取用户组和用户组内用户信息')

    get_notice_group = dict(method='GET',
                            url=f'{route_prefix}/v3/notifications/group/',
                            params={
                                'page': 1,
                                'limit': 201,
                                'value': ''
                            },
                            field_help={
                                'page': '分页/第几页',  ### 分页/第几页
                                'limit': '分页/每页多少个',  ### 分页/每页多少个
                                'value': '模糊查询'  ### 模糊查询
                            },
                            description='获取通知组')

    opt_notice_group = dict(method='POST',
                            url=f'{route_prefix}/v3/notifications/group/',
                            body={
                            },
                            field_help={
                            },
                            description='操作通知组')
