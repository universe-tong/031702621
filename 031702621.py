# -*- coding: utf-8 -*- 
import json
import re
def Provincelist(): 
    list=[]
#四个直辖市
    list.append("北京")
    list.append("上海")
    list.append("天津")
    list.append("重庆")
#少数名族自治区
    list.append("西藏自治区")
    list.append("新疆维吾尔族自治区")
    list.append("广西壮族自治区")
    list.append("宁夏回族自治区")
    list.append("内蒙古自治区")
  
    list.append("河北")
    list.append("河南")
    list.append("山东")
    list.append("山西")
    list.append("江苏")
    list.append("安徽")
    list.append("陕西")
    list.append("甘肃")
    list.append("青海")
    list.append("湖北")
    list.append("湖南")
    list.append("浙江")
    list.append("江西")
    list.append("福建")
    list.append("贵州")
    list.append("四川")
    list.append("广东")
    list.append("云南")
    list.append("海南")
    list.append("黑龙江")
    list.append("吉林")
    list.append("辽宁")
    return list
def Citylist(): 
    List2=[]
    List2.append(["北京"])
    List2.append(["上海"])
    List2.append(["天津"])
    List2.append(["重庆"])
    List2.append(["拉萨","昌都地区","山南地区","阿里地区","那曲地区","林芝地区","日喀则地区"])
    List2.append(["乌鲁木齐", "阿勒泰", "阿克苏", "昌吉", "哈密", "和田", "喀什", "克拉玛依", "石河子", "塔城", "库尔勒", "吐鲁番", "伊宁"])
    List2.append(["南宁", "桂林", "阳朔", "柳州", "梧州", "玉林", "桂平", "贺州", "钦州", "贵港", "防城港", "百色", "北海", "河池", "来宾", "崇左"])
    List2.append(["银川", "固原", "中卫", "石嘴山", "吴忠"])#7
    List2.append(["呼和浩特", "呼伦贝尔", "锡林浩特", "包头", "赤峰", "海拉尔", "乌海", "鄂尔多斯", "通辽"])
    List2.append(["石家庄", "唐山", "张家口", "廊坊", "邢台", "邯郸", "沧州", "衡水", "承德", "保定", "秦皇岛"])
    List2.append(["郑州", "开封", "洛阳", "平顶山", "焦作", "鹤壁", "新乡", "安阳", "濮阳", "许昌", "漯河", "三门峡", "南阳", "商丘", "信阳", "周口", "驻马店"])
    List2.append(["济南", "青岛", "淄博", "威海", "曲阜", "临沂", "烟台", "枣庄", "聊城", "济宁", "菏泽", "泰安", "日照", "东营", "德州", "滨州", "莱芜", "潍坊"])
    List2.append(["太原", "阳泉", "晋城", "晋中", "临汾", "运城", "长治", "朔州", "忻州", "大同", "吕梁"])
    List2.append(["南京", "苏州", "昆山", "南通", "太仓", "吴县", "徐州", "宜兴", "镇江", "淮安", "常熟", "盐城", "泰州", "无锡", "连云港", "扬州", "常州", "宿迁"])
    List2.append(["合肥", "巢湖", "蚌埠", "安庆", "六安", "滁州", "马鞍山", "阜阳", "宣城", "铜陵", "淮北", "芜湖", "毫州", "宿州", "淮南", "池州"])
    List2.append(["西安", "韩城", "安康", "汉中", "宝鸡", "咸阳", "榆林", "渭南", "商洛", "铜川", "延安"])
    List2.append(["兰州", "白银", "庆阳", "酒泉", "天水", "武威", "张掖", "甘南", "临夏", "平凉", "定西", "金昌"])
    List2.append(["西宁", "海北", "海西", "黄南", "果洛", "玉树", "海东", "海南"])
    List2.append(["武汉", "宜昌", "黄冈", "恩施", "荆州", "神农架", "十堰", "咸宁", "襄樊", "孝感", "随州", "黄石", "荆门", "鄂州"])
    List2.append(["长沙", "邵阳", "常德", "郴州", "吉首", "株洲", "娄底", "湘潭", "益阳", "永州", "岳阳", "衡阳", "怀化", "韶山", "张家界"])
    List2.append(["杭州", "湖州", "金华", "宁波", "丽水", "绍兴", "雁荡山", "衢州", "嘉兴", "台州", "舟山", "温州"])
    List2.append(["南昌", "萍乡", "九江", "上饶", "抚州", "吉安", "鹰潭", "宜春", "新余", "景德镇", "赣州"])
    List2.append(["福州", "厦门", "龙岩", "南平", "宁德", "莆田", "泉州", "三明", "漳州"])
    List2.append(["贵阳", "安顺", "赤水", "遵义", "铜仁", "六盘水", "毕节", "凯里", "都匀"])
    List2.append(["成都", "泸州", "内江", "凉山", "阿坝", "巴中", "广元", "乐山", "绵阳", "德阳", "攀枝花", "雅安", "宜宾", "自贡", "甘孜州", "达州", "资阳", "广安", "遂宁", "眉山", "南充"] )
    List2.append(["广州", "深圳", "潮州", "韶关", "湛江", "惠州", "清远", "东莞", "江门", "茂名", "肇庆", "汕尾", "河源", "揭阳", "梅州", "中山", "德庆", "阳江", "云浮", "珠海", "汕头", "佛山"])
    List2.append(["昆明", "保山", "楚雄", "德宏", "红河", "临沧", "怒江", "曲靖", "思茅", "文山", "玉溪", "昭通", "丽江", "大理"])
    List2.append(["海口", "三亚", "儋州", "琼山", "通什", "文昌"])
    List2.append(["哈尔滨", "齐齐哈尔", "牡丹江", "大庆", "伊春", "双鸭山", "鹤岗", "鸡西", "佳木斯", "七台河", "黑河", "绥化", "大兴安岭"])
    List2.append(["长春", "延边", "吉林", "白山", "白城", "四平", "松原", "辽源", "大安", "通化"])
    List2.append(["沈阳", "大连", "葫芦岛", "旅顺", "本溪", "抚顺", "铁岭", "辽阳", "营口", "阜新", "朝阳", "锦州", "丹东", "鞍山"])
    return List2
def GetNameAndNum(str,list,index):
     a=re.search(r'\d!(.*)(\,).*(\d{11}).*',str)
     list.append(a.group(1))
     list.append(a.group(3))
     b=str.replace(a.group(1),"",1)
     b=b.replace(a.group(2),"")
     b=b.replace(a.group(3),"")  
     a=re.match('(\d{1})(!).*',b)
     index.append(a.group(1))
     b=b.replace(a.group(1),"",1)
     b=b.replace(a.group(2),"")
     
     return b
def findprovince(str,list,index):
     for i in range(len(province)):
          a=re.match(province[i],str)
          if(a):
               index.append(i)
               if(i<4):
                    list.append(a.group())
                    b=str
                    break
               if (3<i<=8):
                    list.append(a.group())
                    b=str.replace(a.group(),"",1)
                    break
               if(i>8):
                    list.append(a.group()+"省")
                    b=str.replace(a.group(),"",1)
                    
                    c=re.match("省.*",b)
                    if(c):
                        b=b.replace('省',"",1)
                        
                    break
     return b
def findcity(str,list,index):
     test=1
     for i in range(len(city[index])):
          a=re.match(city[index][i],str)
          if(a):
               list.append(a.group()+"市")
               b=str.replace(a.group(),"",1)
               c=re.match("市.*",b)
               if(c):
                   b=b.replace('市',"",1)
               test=0
               break

     if(test==1):
          list.append("")
          b=str
    
     return b
def findtown(str,list,index):
      a=re.match('([^县]+?县|.*?区|.*?市|.*?旗|.*?海域|.*?岛|"")',str)
      b=str
      if(a):
          list.append(a.group())
          b=str.replace(a.group(),"",1)
      else:
          list.append("")

        
      a=re.match(".*?乡|.*?镇|.*?街道",b)
      if(a):
          list.append(a.group())
          b=b.replace(a.group(),"",1)
      else:
          list.append("")

          
      if(index=='2' or index=='3'):
          a=re.match(".*?路|.*道|.*?街|.*？弄|.*?巷",b)
          if(a):
              list.append(a.group())
              b=b.replace(a.group(),"",1)
          else:
              list.append("")
              
          a=re.match(".+?号",b)
          if(a):
              list.append(a.group())
              b=b.replace(a.group(),"",1)
          else:
              list.append("")
      b=b.replace(".","",1)
      list=list.append(b)
      
      return b
index=[]
addlist=[]
result=[]
province=[]
city=[]
province=Provincelist()
city=Citylist()
address=input()
s=GetNameAndNum(address,result,index)
s=findprovince(s,addlist,index)
s=findcity(s,addlist,index[1])
s=findtown(s,addlist,index[0])
result.append(addlist)
resultaddress={}
resultaddress["姓名"]=result[0]
resultaddress["手机"]=result[1]
resultaddress["地址"]=result[2]
resultjson=json.dumps(resultaddress)
print(resultjson)

