$(function () {
    // get_current_user_info();
    // get_last_count_number();
    // get_user_menu();
    // send_request();
})

var get_current_user_info = function () {

    $.ajax({
        url: url_get_user_info,
        type: 'GET',
        success: function (result) {
            $(".username").html(result.username);
            $(".user.user-menu a img").attr("src", result.img)
            $(".user-panel div img").attr("src", result.img)
            $(".user-header img").attr("src", result.img)
            $(".userGroup").html(result.group)
        },
        error: function (error_result) {
            console.log(error_result)
            alert("请求错误")
        },
    })
}

//读取未读信息
let get_unread_message = function () {
    let unread_message_list = [
        {
            "href": "#",
            "title": "我想买一个新的皮肤",
            "time_str": "5分钟前",
            "user_send": "5",
        }
    ]

    let str_message = ''
    $.each(unread_message_list, function (index, data) {

        let user_base_data = {
            "username": "张三",
            "img": "/static/dist/img/user2-160x160.jpg",
        }

        str_message += '<li>' +
            ' <a href="' + data.href + '">' +
            '    <div class="pull-left">' +
            '     <img src="' + user_base_data.img + '" class="img-circle" alt="Image">' +
            '   </div>' +
            '  <h4>' + user_base_data.username +
            '    <small><i class="fa fa-clock-o"></i> ' + data.time_str + '</small>' +
            '  </h4><p>' +
            data.title +
            '</p></a> </li>'
    })
    $(".messages-menu ul li ul.menu").html(str_message)


}
//读取未读通知
var get_unread_notification = function () {
    var notification = "请尽早下班！"
    var str_notification = '<li> <a href="#"><i class="fa fa-users text-aqua"></i>' +
        notification + ' </a> <li>'
    str_notification += str_notification
    $(".notifications-menu ul li ul.menu").html(str_notification)
}
//读取任务进度
var get_uncompleted_task = function () {

    var task_title = "UI设计"
    var task_progress = "25%"
    var str_task = '<li><a href="#"><h3>' + task_title +
        '<small class="pull-right">' + task_progress + '</small></h3><div class="progress xs"><div class="progress-bar progress-bar-aqua" style="width: ' + task_progress + '" role="progressbar"aria-valuenow="20" aria-valuemin="0" aria-valuemax="100">' +
        '<span class="sr-only">已完成 ' + task_progress + '</span></div></div></a> </li>'
    str_task += str_task
    str_task = str_task + '<li><a href="#"><h3>' + task_title +
        '<small class="pull-right">' + task_progress + '</small></h3><div class="progress xs"><div class="progress-bar progress-bar-aqua" style="width: ' + task_progress + '" role="progressbar"aria-valuenow="20" aria-valuemin="0" aria-valuemax="100">' +
        '<span class="sr-only">已完成 ' + task_progress + '</span></div></div></a> </li>'

    $(".tasks-menu ul li ul.menu").html(str_task)
}
var get_user_menu = function () {
    $.ajax({
        url: url_get_user_menu + "0/",
        type: 'GET',
        success: function (result) {
            var str_menu = build_menu_str(result);
            $(".sidebar-menu").html($(".sidebar-menu").html() + str_menu)
        },
        error: function (error_result) {
            console.log(error_result)
            alert("请求错误")
        },
    })


}
// 根据数据，返回对应菜单的字符串
var build_menu_str = function (temp_menu_data_json) {
    var temp_menu_str = '';
    $.each(temp_menu_data_json, function (index, data) {
        // console.log(data)
        temp_menu_str += '<li class="treeview"><a href="' + data.href +
            '"><i class="fa ' + data.logo + '">' +
            '</i><span>&nbsp;' + data.menu_span +
            '</span>'
        if (data.label_right != '') {
            temp_menu_str += data.label_right
        }
        temp_menu_str += '</a>'
        if (data.child_menu.length != 0) {
            temp_menu_str += '<ul class="treeview-menu">'
            $.each(data.child_menu, function (child_index, child_data) {
                temp_menu_str += '<li><a href="' + child_data.href + '"><i class="fa fa-circle-o"></i>&nbsp;' + child_data.menu_span
                if (child_data.label_right != '') {
                    temp_menu_str += child_data.label_right
                }
                temp_menu_str += '</a></li>'
            })
            temp_menu_str += '</ul>'
        }
        temp_menu_str += '</li>'
    })
    return temp_menu_str;
}

//根据模块、方法确定选中的菜单
let change_menu_choice = function(model, func){
    // alert(1)
}