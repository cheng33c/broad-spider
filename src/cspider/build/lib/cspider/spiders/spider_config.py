import re

""" 网站链接规律规则
    0. 网站URL基本地址 - baseURL
    1. javascript 过滤
    2. 从开头匹配到'//+url' 去掉'//'
    3. 从开头匹配，如果没有匹配到http，则在url前加入http://
    4. 从开头匹配，类似[/book/jiadian/10056620?mt=12.3273.r83567.2657#sp_topbanner]就直接过滤
    5. 组装好URL后匹配，如果遇到http(s):///的就直接过滤
"""
pattern0 = re.compile('(https?://.*?)/?$')
pattern1 = re.compile('java')
pattern2 = re.compile('^//')
pattern3 = re.compile('^http')
pattern4 = re.compile('^/')
pattern5 = re.compile('https?:///')