import json
from datetime import datetime

from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from core.models import UserLoginRecord


def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return_data = {
                "code": 404,
                "msg": "用户不存在",
                "data": "0"
            }
            return HttpResponse(json.dumps(return_data), content_type='application/json')

        if user is not None:
            login(request, user)
            return_data = {
                "code": 200,
                "msg": user.first_name + "登录成功",
                "data": {"user_id": user.id}
            }
            login_record = UserLoginRecord()
            login_record.username = user.first_name
            login_record.userID = user.id
            login_record.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            login_record.detail = "登录"
            login_record.save()
            return HttpResponse(json.dumps(return_data), content_type='application/json')


def dashboard(request):
    pass


def get_user_info(request, id):
    # user = User.objects.get(id=id)

    user_data = {
        "username": "后台返回测试",
        "img": "dist/img/user1-128x128.jpg",
        "group": "测评工程师"
    }
    return HttpResponse(json.dumps(user_data), content_type='application/json')


def get_user_menu(request, id):
    menu_data_json = [
        {
            'href': '#',
            'logo': 'fa-files-o',
            'menu_span': '软件测评',
            'label_right': '<span class="pull-right-container"><span class="label label-primary pull-right">4</span></span>',
            'child_menu': [
                {
                    'href': '#',
                    'logo': 'fa-circle-o',
                    'menu_span': '登记测试',
                    'label_right': '<span class="pull-right-container"><span class="label label-primary pull-right">0</span></span>'},
                {
                    'href': '#', 'logo': 'fa-circle-o', 'menu_span': '确认测试',
                    'label_right': '<span class="pull-right-container"><span class="label label-primary pull-right">2</span></span>'},
                {'href': '#', 'logo': 'fa-circle-o', 'menu_span': '验收测试',
                 'label_right': '<span class="pull-right-container"><span class="label label-primary pull-right">1</span></span>'},
                {'href': '#', 'logo': 'fa-circle-o', 'menu_span': '其他测试',
                 'label_right': '<span class="pull-right-container"><span class="label label-primary pull-right">1</span></span>'},
            ],
        },
        {
            'href': '#',
            'logo': 'fa-files-o',
            'menu_span': '市场营销',
            'label_right': '<span class="pull-right-container"><span class="label label-primary pull-right">4</span></span>',
            'child_menu': [{'href': '#', ' logo': 'fa-circle-o', 'menu_span': '供方',
                            'label_right': '<span class="pull-right-container"><span class="label label-primary pull-right">0</span></span>'},
                           {'href': '#', 'logo': 'fa-circle-o', 'menu_span': '客户',
                            'label_right': '<span class="pull-right-container"><span class="label label-primary pull-right">2</span></span>'},
                           {'href': '#', 'logo': 'fa-circle-o', 'menu_span': '其它',
                            'label_right': '<span class="pull-right-container"><span class="label label-primary pull-right">1</span></span>'},
                           ],
        },
        {
            'href': '#',
            'logo': 'fa-book',
            'menu_span': '学习提升',
            'label_right': '',
            'child_menu': [
            ],
        },
        {
            'href': '#',
            'logo': 'fa-book',
            'menu_span': '交流沟通',
            'label_right': '',
            'child_menu': [
            ],
        },
        {
            'href': '#',
            'logo': 'fa-book',
            'menu_span': '专业智库',
            'label_right': '<span class="pull-right-container"><i class="fa fa-angle-left pull-right"></i></span>',
            'child_menu': [
                {'href': '#', 'menu_span': '专家库', 'label_right': ''},
                {'href': '#', 'menu_span': '软件测评-用例库', 'label_right': ''},
            ],
        },
    ]
    return HttpResponse(json.dumps(menu_data_json), content_type='application/json')
