'''
musen库:
ffxw0720主制作，musen其他成员协助制作
现已支持config功能
© 2020 musen
'''
def config(File,Classification,Parameter):
    '''
    获取用户调用信息
    '''
    file = File
    classification = Classification
    parameter = Parameter


    '''
    获取musen格式文件内容
    '''
    f = open(file,"r")
    content = f.read()
    f.close()

    '''
    对内容进行处理
    '''
    content = str(str(str(str(content).replace('\n', '')).replace('\r', '')).replace('\t', '')).replace('   ', '')
    content_list = content.split(";")#取到内容的列表形式

    #声明
    declare = str(content_list[0])
    declare_list = declare.split(" ")
    declare = str(declare_list[0])
    if declare == "declare":
        pass
    else:
        print('''
        Error: syntax error declared
        Please read the document for solutions, link: http://musendocs.musen.team/
        
        错误：声明语法错误
        请阅读文档以获取解决方案，链接：http://musendocs.musen.team/
        ''')
        exit()
    declare = str(declare_list[1])#取到声明内容
    if declare == "config":
        pass
    else:
        print('''
        Error: bad declare entry in Musen format file
        Please read the document for solutions, link: http://musendocs.musen.team/
        
        错误：musen格式文件中的declare项错误
        请阅读文档以获取解决方案，链接：http://musendocs.musen.team/
        ''')
        exit()
    

    #内容
    a = 1
    b = 1
    c = 0
    while a==1:
        musen_c = str(content_list[b])
        
        if musen_c=="" or musen_c==" ":
            a = 2
        else:
            pass
        musen_c_list = musen_c.split(":")
        musen_class = musen_c_list[0]
        musen_class = str(musen_class).replace('class ', '')
        musen_class = str(musen_class).replace(':', '')
        if classification == musen_class:
            musen_class_a = musen_c_list[1]
            musen_class_list = musen_class_a.split(",")
            musen_class_want = musen_class_list[c]
            if musen_class_want == "" or musen_class_want == " ":
                a = 2
            if parameter in musen_class_want:
                musen_class_want = str(str(str(musen_class_want).replace('=', '')).replace(parameter, '')).replace(' ', '')
                a = 2
                return musen_class_want
            else:
                c = c+1
        else:
            b = b+1
