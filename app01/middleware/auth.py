from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect

class AuthMiddleware(MiddlewareMixin):
    def process_request(self,request):
        #0. 排除不需要登录就能访问的页面
        #request.path_info 获取当前用户请求的url
        if request.path_info in ["/login/","/image/code/"]:
            return
        #1.读取当前访问用户的session信息，如果等读到，说明已经登录过，就可以继续向后走
        info_dict=request.session.get("info")
        #print(info_dict)
        if info_dict:
            return
        #2. 没有登录过
        return redirect('/login/')


        #如果没有返回值，继续往前走
        #如果有返回值直接就回溯/往其他地方跳 render redirect
        print("M1.process_request")
        return HttpResponse("Cannot access")

    def process_response(self,request,response):
        #print("M1.process_response")
        return response





