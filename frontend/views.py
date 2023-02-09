from datetime import datetime

from django.contrib.auth import authenticate, login
from django.shortcuts import render

from core.models import UserLoginRecord


def index(request):
    if request.method == "GET":
        return_data = base_login_check(request)
        return render(request, "index.html", return_data)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return_data = {
                'has_error': 'has-error',
                'label_style': 'display:block',
                'data': '0'
            }
            return render(request, "login.html", return_data)
        else:
            login(request, user)
            # 为Session赋值
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            request.session.set_expiry(14400)

            # 用于登录审计
            login_record = UserLoginRecord()
            login_record.username = user.first_name
            login_record.userID = user.id
            login_record.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            login_record.detail = "登录"
            login_record.save()

            login_user_data = {
                "username": user.first_name,
                "img": "dist/img/user2-160x160.jpg",
                "log_action_name": "退出登录",
                "log_action_url": "/logout",
                "unread_message_count": 10,
                "unread_notification_count": 20,
                "undone_task_count": 30,
                "work": "测试工程师"
            }
            return render(request, "index.html", login_user_data)


def my_login(request):
    default_data = {
        'label_style': 'display:none',
    }
    return render(request, "login.html", default_data)


def my_logout(request):
    first_name = request.session.pop('first_name')
    user_id = request.session.pop('user_id')
    # 用于登录审计
    login_record = UserLoginRecord()
    login_record.username = first_name
    login_record.userID = user_id
    login_record.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    login_record.detail = "注销"
    login_record.save()

    default_data = {
        'label_style': 'display:none',
    }
    return render(request, "login.html", default_data)


def todo(request):
    if request.method == "GET":
        return_data = base_login_check(request)
        return render(request, "index.html", return_data)


def top_command_tool1(request):
    return_data = base_login_check(request)
    return render(request, "toolkit/top_result_tool1.html", return_data)

def top_command_tool2(request):
    return_data = base_login_check(request)
    return render(request, "toolkit/top_result_tool2.html", return_data)

def ocr_api(request):
    return_data = base_login_check(request)
    return render(request, "toolkit/ocr_api.html", return_data)


def base_login_check(request):
    user_id = request.session.get('user_id')
    if user_id:
        login_user_data = {
            "username": request.session.get('first_name'),
            "img": "dist/img/user2-160x160.jpg",
            "log_action_name": "退出登录",
            "log_action_url": "/logout",
            "unread_message_count": 10,
            "unread_notification_count": 20,
            "undone_task_count": 30,
            "work": "测试工程师"
        }
        return login_user_data
    else:
        un_login_user_data = {
            "username": "未登录",
            "img": "dist/img/user2-160x160.jpg",
            "log_action_name": "登录",
            "log_action_url": "/login"
        }
        return un_login_user_data
