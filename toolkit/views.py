import json, re
import ddddocr
from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse

# OCR验证码识别
def ocr_api(request):
    try:
        if request.method == 'POST':
            # 从网页获取json数据
            json_str = request.body
            json_dict = json.loads(json_str)
            picurl=json_dict.get("picurl", "默认值")
            sid=json_dict.get("sid", "默认值")
            # url=''.join(picurl)
            # sid =request.POST.get('sid')
            # session=''.join(sid)
            headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4195.1 Safari/537.36",
    "Cookie": "sid="+sid
}
            #请求验证码图片
            resp = requests.get(picurl, headers=headers, verify=False)
            captcha_img = resp.content
            # 识别
            ocr = ddddocr.DdddOcr()
            r = ocr.classification(captcha_img)
            # 返回
            return HttpResponse(json.dumps({"msg":"识别成功！", "verifyCode":r}))
        else:
            return HttpResponse(json.dumps({'code': '1', 'msg': '请求方法错误，请使用POST！'}))
    except Exception as e:
        return HttpResponse(json.dumps({'code': '1', 'msg': str(e)}))

# 监控对应进程的top结果   top -b -n 600 -d 3 grep|3133 >>result.txt 
def top_result_tool1(request):
    print('1111222')
    file = request.FILES.get("file")
    cpu_list = []
    mem_list = []
    str_result = "["
    count = 0
    for line in file:
        pattern = re.compile(r'(\d\s[S|R]\s+)(\d+\.\d+)(\s+)(\d+\.\d+)', re.MULTILINE)
        ma = pattern.search(str(line))
        if ma:
            count = count + 1
            str_result = str_result + '{"cpu_rate":"' + ma.group(2) + '","mem_rate":"' + ma.group(4) + '"},'
            cpu_list.append(ma.group(2))
            mem_list.append(ma.group(4))
    str_result += "]"
    return_data = {
        'code': 200,
        'msg': count,
        'data': {'cpu_list': cpu_list, 'mem_list': mem_list},
    }
    return JsonResponse(return_data)


# 监控整体资源的top结果  top -b -n 600 -d 3 >>result.txt 
def top_result_tool2(request):
    file = request.FILES.get("file")
    cpu_list = []
    mem_list = []
    # 记录 CPU 和 内存的最大值
    max_cpu = 0
    max_mem = 0
    # 记录数量
    count = 0
    for line in file:
        print('当前行内容为：', str(line))
        # 需要内容CPU 的正则表达式，匹配如下格式：
        # %Cpu(s):  0.0 us,  1.4 sy,  0.0 ni, 98.6 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
        #pattern_cpu = re.compile(r'(%Cpu[(]s[)]:\s*)(.*)(\s*us)', re.MULTILINE)
        pattern_cpu = re.compile(r'(%Cpu[(]s[)]:\s*)(.*)(.*us,\s*)(.*sy,\s*)(.*ni,\s*)(.*)(\s*id)', re.MULTILINE)
        # 正则搜索
        ma_cpu = pattern_cpu.search(str(line))
        # 如果匹配
        if ma_cpu:
            # 结果计数加一
            count = count + 1
            # 匹配结果的保存
            current_cpu =100-float(ma_cpu.group(6))
            # 最大值的记录
            cpu_list.append(current_cpu)
            if current_cpu > max_cpu:
                max_cpu = current_cpu
        # 需要匹配内存的正则表达式，格式如下：
        # KiB Mem : 32753592 total,  7623440 free,  8312512 used, 16817640 buff/cache
        pattern_mem = re.compile(r'(KiB Mem :\s*)(.*)(\s*total)(.*free,\s*)(.*)(\s*used)', re.MULTILINE)
        # 正则搜索
        ma_mem = pattern_mem.search(str(line))
        # 如果匹配
        if ma_mem:
            # 总内存
            mem_total = ma_mem.group(2)
            # 使用的内存
            mem_used = ma_mem.group(5)
            # 计算内存使用率
            mem_total = float(mem_total)
            mem_used = float(mem_used)
            mem_use_rate = mem_used/mem_total*100
            # 结果的保存
            mem_list.append(mem_use_rate)
            # 最大值的记录
            if mem_use_rate > max_mem:
                max_mem = mem_use_rate
    return_data = {
        'code': 200,
        'msg': count,
        'data': {'cpu_list': cpu_list, 'mem_list': mem_list, 'max_cpu':max_cpu, 'max_mem':max_mem},
    }
    return JsonResponse(return_data)
