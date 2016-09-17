#coding=utf-8
#coding=gbk
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import Firstgroup
from models import Secondgroup
from models import Knowledgepoint
import json
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Q
# Create your views here.
class JsonClass:
    def __init__(self,body,state,code,info):
        self.body = body
        self.state = state
        self.code = code
        self.info = info
def object2dict(obj):
    #convert object to a dict
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d
 
def dict2object(d):
    #convert dict to object
    if'__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module,class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args
        inst = class_(**args) #create new instance
    else:
        inst = d
    return inst

def addfirstgroup(req):
    name = req.POST.get('firstgroupname')
   # Firstgroup.objects.create(name=name)
    group = Firstgroup.objects.filter(name__exact=name)
    if group:
       Firstgroup.objects.create(name=name)
       jsonclass = JsonClass(None,1,200,"添加成功")
    #json_data = serializers.serialize("json",jsonclass.object)
       dump = json.dumps(jsonclass,default=object2dict)
       return HttpResponse(dump)
    else:
       jsonclass = JsonClass(None,0,200,"添加失败，已存在")
       dump = json.dumps(jsonclass,default=object2dict)
       return HttpResponse(dump)
def addsecondgroup(req):
    name1 = req.POST.get("firstname")
    name2 = req.POST.get("secondname")
    secondgroup = Secondgroup.objects.filter(name__exact=name2)
    if secondgroup:
       jsonclass=JsonClass(None,0,200,"已存在")
       return HttpResponse(json.dumps(jsonclass,default=object2dict))
    else:
       firstgroup1=Firstgroup.objects.filter(name__exact=name1)
       if firstgroup1:
          Secondgroup.objects.create(firstgroup_id=firstgroup1.id,name = name2);
          jsonclass=JsonClass(None,0,200,"添加成功")
          return HttpResponse(json.dumps(jsonclass,default=object2dict))
       else:
          Firstgroup.objects.create(name=name1)
          firstgroup1=Firstgroup.objects.get(name__exact=name1)
          Secondgroup.objects.create(firstgroup_id=firstgroup1.id,name = name2);
          jsonclass=JsonClass(None,0,200,"添加成功")
          return HttpResponse(json.dumps(jsonclass,default=object2dict))
       
           
 
    #return HttpResponse(json_data,content_type="application/json")
# Create your views here.
