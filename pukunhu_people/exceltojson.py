
import xlrd
from collections import OrderedDict
import json
import codecs
import personData
import familyData
import datetime
import xlsxwriter

 



def save_as_json(object,file_path): #第三步
    with open(file_path,"w",encoding='utf-8',errors='ignore') as f:
        json.dump(object,f,ensure_ascii=False)


def file_to_json_fomat(path1,path2,personDatas,list_poor_family):  #第二步
    with open(path1,'r',encoding ="utf-8")as f:#加载json文件
        personDatas =json.load(f)#将加载的json文件转换成字典列表

    for person in personDatas:
        list_poor_family.append({'ID':person['ID'],'o1':person['o1'],'o2':person['o2'],'o3':person['o3'],'o4':person['o4'],'o5':person['o5'],'o6':person['o6'],'b1':person['b1'],'b2':person['b2'],'b3':person['b3'],'b4':person['b4'],'b5':person['b5'],'b6':person['b6'],'b7':person['b7'],'b8':person['b8'],'b9':person['b9'],'b10':person['b10'],'b11':person['b11'],'b12':person['b12'],'b13':person['b13'],'b14':person['b14'],'b15':person['b15'],'b16':person['b16'],'b17':person['b17'],'b18':person['b18'],'b19':person['b19'],'b20':person['b20'],'b21':person['b21'],'error':False,'state':False,'log':person['log']})

    save_as_json(list_poor_family,path2)



def json_to_personDatalist(path,list_js,list,error,start,end,n):  #初始化数据
    with open('002.json','r',encoding ="utf-8")as f:#加载json文件
        list_js =json.load(f)#将加载的json文件转换成字典列表
#input()

    for person in list_js:#将加载的json数据添加到familyData列表中
        list.append(personData.personData(person['ID'],person['o1'],person['o2'],person['o3'],person['o4'],person['o5'],person['o6'],person['b1'],person['b2'],person['b3'],person['b4'],person['b5'],person['b6'],person['b7'],person['b8'],person['b9'],person['b10'],person['b11'],person['b12'],person['b13'],person['b14'],person['b15'],person['b16'],person['b17'],person['b18'],person['b19'],person['b20'],person['b21'],person['error'],person['state'],person['log']))
        if not(person['state']):
            if person['error']:
                error+=1
            start+=1
        else:
            end+=1
        n+=1
        print("已添加%s"% n)
    print("总共添加%s项,%s项已完成，%s项待完成(其中%s项出错，待手工处理)"% (n,end,start,error))
    print('''
待录入数据准备完成，准备登陆系统...... GOGOGOGOGO

''')
    
#    print('''gogogo！！！按任意键开始启动Chrome浏览器......
#''')
#    input()

def error_json_to_xlsx(path,xlsxpath,list_js,list,error,start,end,n):
    with open('002.json','r',encoding ="utf-8")as f:#加载json文件
        list_js =json.load(f)#将加载的json文件转换成字典列表
#input()

    for person in list_js:#将加载的json数据添加到personData列表中
        list.append(personData.personData(person['ID'],person['o1'],person['o2'],person['o3'],person['o4'],person['o5'],person['o6'],person['b1'],person['b2'],person['b3'],person['b4'],person['b5'],person['b6'],person['b7'],person['b8'],person['b9'],person['b10'],person['b11'],person['b12'],person['b13'],person['b14'],person['b15'],person['b16'],person['b17'],person['b18'],person['b19'],person['b20'],person['b21'],person['error'],person['state'],person['log']))
        if not(person['state']):
            if person['error']:
                error+=1
            start+=1
        else:
            end+=1
        n+=1
        
    print("总共%s项,%s项已完成，%s项待完成,其中%s项出错,按任意键导出到excel文件"% (n,end,start,error))
    input()

    for person in list_js:
        if not(person['state']):
            if person['error']:
                list.append(person)
                error+=1
            start+=1
        else:
            end+=1
        n+=1
    print("总共%s项,%s项已完成，%s项待完成,其中%s项出错,按任意键退出"% (n,end,start,error))
    input()




def personDatalist_to_json(personDatalist,path):
    temp=[]

    with open('002.json','r',encoding ="utf-8")as f:#加载json文件
        list_js =json.load(f)#将加载的json文件转换成字典列表
#input()

    for person in personDatalist:
        temp.append({'ID':person.ID,'o1':person.o1,'o2':person.o2,'o3':person.o3,'o4':person.o4,'o5':person.o5,'o6':person.o6,'b1':person.b1,'b2':person.b2,'b3':person.b3,'b4':person.b4,'b5':person.b5,'b6':person.b6,'b7':person.b7,'b8':person.b8,'b9':person.b9,'b10':person.b10,'b11':person.b11,'b12':person.b12,'b13':person.b13,'b14':person.b14,'b15':person.b15,'b16':person.b16,'b17':person.b17,'b18':person.b18,'b19':person.b19,'b20':person.b20,'b21':person.b21,'error':person.error,'state':person.state,'log':person.log})
    save_as_json(temp,path)
    print("已将处理后的情况保存到002.json文件中，下次运行将直接读取进度")
    
def js_to_xlsx(js_path,xlsxpath):
    '''将缓存的json文件中错误的值'''
    with open(js_path,'r',encoding ="utf-8")as f:#加载json文件
        rec_data = json.load(f)#将加载的json文件转换成字典列表

    workbook = xlsxwriter.Workbook(xlsxpath)

    worksheet = workbook.add_worksheet()
    # 设定格式，等号左边格式名称自定义，字典中格式为指定选项

    # bold：加粗，num_format:数字格式

    bold_format = workbook.add_format({'bold': True})
    money_format = workbook.add_format({'num_format': '$#,##0'})
    date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})
    # 将二行二列设置宽度为15(从0开始)
    worksheet.set_column(1, 1, 15) 
    # 用符号标记位置，例如：A列1行
    n = 0
    for key,value in rec_data[1].items():        
        worksheet.write(0,n, key, bold_format)
        n+=1
    
    row = 1
    countall = 0
    for item in rec_data:
        countall+=1
        # 使用write_string方法，指定数据格式写入数据
        if item['error']:
            col = 0               
            for key,value in item.items():
                worksheet.write_string(row, col, str(value))
                col+=1
            row += 1
    workbook.close()
    print("总条数%d条，提取错误条数%d,文件保存在 %s 中。" % (countall , (row - 1), xlsxpath))



def excel_json(path,path_two):  #第一步
    ###将excel文件数据转换为json并保存到本地
    wb = xlrd.open_workbook(path) 

    convert_list = []
    sh = wb.sheet_by_index(0)
    title = sh.row_values(0)
    for rownum in range(1, sh.nrows):
        rowvalue = sh.row_values(rownum)
        single = OrderedDict()
        for colnum in range(0, len(rowvalue)):
            print(title[colnum], rowvalue[colnum])
            single[title[colnum]] = rowvalue[colnum]
        convert_list.append(single)
    j = str(json.dumps(convert_list,ensure_ascii=False))

    with codecs.open(path_two,"w",encoding='utf-8',errors='ignore') as f:
        f.write(j)
    print("excel转换json完成")





