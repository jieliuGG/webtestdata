import unittest

from webtestdata.settings import WEB_URL_TITLE,AGENT_LOGIN_ACCOUNT,AGENT_LOGIN_PASSWORD


# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webtestdata.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App


from TestCaseFunction.base.activebase import ActiveWeb
from TestCaseFunction.util.operation_json import OperationJson
from TestCaseFunction.util.gettimestr import GetTimeStr

from TestCaseFunction.autotest.config.page.manager.loginPage import LoginPage   #导入登录页
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.activityCreatePage import ActivityCreatePage   #导入创建活动页
from TestCaseFunction.autotest.config.page.marketing.rwhdgl.ticketCreatePage import TicketCreatePage   #导入创建优惠券页

class TestCreateTicketClass(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        # from base.getcookie import GetCookie
        # outjsonfile = "../../../cookiejson/cookiemanager.json"
        # outloginurl = LoginPage().pageurl
        # outloginaccountxpath = LoginPage().account
        # outloginaccounttext = "81122336666"
        # outloginppasswordxpath = LoginPage().password
        # outloginpasswordtext = "abc123456"
        # outloginbuttonxpath = LoginPage().loginbutton
        #
        # getcookie = GetCookie(outjsonfile=outjsonfile, outloginurl=outloginurl,
        #                       outloginaccountxpath=outloginaccountxpath,
        #                       outloginaccounttext=outloginaccounttext, outloginppasswordxpath=outloginppasswordxpath,
        #                       outloginpasswordtext=outloginpasswordtext,
        #                       outloginbuttonxpath=outloginbuttonxpath)  # 实例化
        # getcookie.writerCookieToJson()

        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        # self.jsonfile = '../../../cookiejson/cookieagent.json'
        # self.operationjson = OperationJson(file_path=self.jsonfile)   #实例化
        # self.cookie = self.operationjson.get_all_data()
        # print("self.cookie:%s" % self.cookie)
        self.activeweb = ActiveWeb()  # 实例化
        self.loginurl = LoginPage().pageurl
        self.activeweb.getUrl(self.loginurl)  # 打开网址
        self.activeweb.findElementByXpathAndInput(LoginPage().account,AGENT_LOGIN_ACCOUNT)
        self.activeweb.findElementByXpathAndInput(LoginPage().password,AGENT_LOGIN_PASSWORD)
        self.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        self.activeweb.delayTime(3)

        self.testpage = TicketCreatePage()
        self.testpageurl =self.testpage.pageurl   #测试页面url
        self.testpagekcslinput  = self.testpage.kcsl_input   #第一部分# 库存数量输入框路径
        self.testpageqyxqselect = self.testpage.qyxq_select   #第一部分# 券有效期选择框路径
        self.testpageyhqsmareatext  = self.testpage.yhqsm_areatext    #第一部分# 优惠券说明多行输入框路径
        self.testpageyhqmcinput = self.testpage.yhqmc_input    #第二部分# 优惠券名称输入框路径
        self.testpageyhlxselect = self.testpage.yhlx_select    #第二部分# 优惠类型选择框路径
        self.testpageyhmsselect = self.testpage.yhms_select    #第二部分# 优惠模式选择框路径
        self.testpagezdxfinput = self.testpage.zdxf_input    #第二部分# 最低消费输入框路径
        self.testpagezfqdxzselect  = self.testpage.zfqdxz_select     #第二部分# 支付渠道限制选择框路径
        self.testpagesyfwselect   = self.testpage.syfw_select     #第二部分# 使用范围选择框路径

        self.testpagecancelbutton = self.testpage.cancel_button # 页面取消按钮
        self.testpageconfirmbutton = self.testpage.confirm_button  # 页面确定按钮

        ######################创建活动页面###############################
        self.activitycreatepage = ActivityCreatePage()
        self.activitycreatepage_pageurl = self.activitycreatepage.pageurl
        self.activitycreatepage_w_tjlp = self.activitycreatepage.w_tjlp    # ---活动奖励---# 未添加礼品时，“添加礼品”文字链接路径

        #pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()
        # pass

    def writexunicookie(self):
        addcookie = {'name': '.nereus.manager.settle.banks', 'value': 'QCK9GvKG8OEOh6lRUyyLlmKnHl8i3w'}
        self.activeweb.driver.add_cookie(addcookie)
        self.activeweb.driver.refresh()
        self.activeweb.delayTime(5)
        self.activeweb.outPutMyLog("写入虚拟银行cookie完成")

    #定义创建活动,
    #发放状态为1表示开启，否则为关闭
    #券有效期为1表示相对时间，否则为绝对时间
    #营销成本承担方为1表示平台，否则为商户
    #优惠类型为1表示代金券
    #优惠模式为1表示固定金额，否则为随机金额
    #支付渠道限制为1表示不限，为2表示钱包余额，为3表示银行卡支付
    #使用平台为1表示QRindo，为2表示PaySDK
    #使用范围为1表示不限，为2表示指定行业，为3表示指定商户
    #是否支持退券为1表示可退，为2表示不可退

    def definecreateticket(self,num,ffzt,kcslinputtext,qyxq,
                           xdsjtsinputtext,jdsjstarttimexpath,jdsjendtimexpath,
                           yxcbcdf,yhqmcinputtext,yhlx,
                           yhms,gdjemzinputtext,sjjemzmiminputtext,sjjemzmimaxinputtext,
                           zdxfinputtext,zfqdxz,sypt,
                           syfw,zdhyoptionxpath,zdshinputtext,isplsh,plfilepath,
                           sfzctq):
        self.activeweb.getUrl(self.activitycreatepage_pageurl)
        self.activeweb.delayTime(3)

        #创建活动页，点击“添加礼品”文字链接
        self.activeweb.findElementByXpathAndClickNum(num, self.activitycreatepage_w_tjlp)  # 点击添加礼品文字链接(还未添加礼品)

        #进入创建优惠券页，新建优惠券
        #第一部分
        if ffzt == "1":
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.ffzt_kq_checkbox)  # 点击发放状态开始对应的选项框
        else:
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.ffzt_gb_checkbox)  # 点击发放状态关闭对应的选项框
        self.activeweb.findElementByXpathAndInputNum(num, self.testpagekcslinput,kcslinputtext) # 输入库存数量
        if qyxq == "1":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpageqyxqselect,self.testpage.qyxq_select_option_xdsj)  # 选择券有效期选项为相对时间
            self.activeweb.findElementByXpathAndInputNum(num, self.testpage.qyxq_select_option_xdsj_ts_input, xdsjtsinputtext)  # 输入相对时间
        else:
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpageqyxqselect,self.testpage.qyxq_select_option_jdsj)  # 选择券有效期选项为绝对时间
            self.activeweb.findElementByXpathAndClickAbountData(num, self.testpage.qyxq_select_option_jdsj_starttime,jdsjstarttimexpath)  # 点选活动时间开始时间
            self.activeweb.findElementByXpathAndClickAbountData(num, self.testpage.qyxq_select_option_jdsj_endtime,jdsjendtimexpath)  # 点选活动时间结束时间
        if yxcbcdf == "1":
             self.activeweb.findElementByXpathAndClickNum(num, self.testpage.yxcbcdf_pt_checkbox)  # 点击营销成本承担方中的平台前的选项框
        else:
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.yxcbcdf_sh_checkbox)  # 点击营销成本承担方中的商户前的选项框

        self.activeweb.findElementByXpathAndInputNum(num, self.testpageyhqsmareatext,
        "%s（发放状态为1表示开启，否则为关闭）- 库存数量：【%s】-%s(券有效期为1表示相对时间(相对天数：【%s】)，否则为绝对时间)-%s（营销成本承担方为1表示平台，否则为商户）-%s（优惠类型为1表示代金券）-%s（优惠模式为1表示固定金额，否则为随机金额）-（1-面值:【%s】;2-面值最小值为：【%s】,最大值为：【%s】）-最低消费：【%s】-%s（使用平台为1表示QRindo，为2表示PaySDK）-%s（使用范围为1表示不限，为2表示指定行业，为3表示指定商户）-%s(是否支持退券为1表示可退，为2表示不可退)"
                                                     % (ffzt,kcslinputtext,qyxq,xdsjtsinputtext,yxcbcdf,yhlx,yhms,gdjemzinputtext,sjjemzmiminputtext,
                                                        sjjemzmimaxinputtext,zdxfinputtext,sypt,syfw,sfzctq))  # 输入优惠券说明
        #第二部分
        self.activeweb.findElementByXpathAndInputNum(num, self.testpageyhqmcinput,yhqmcinputtext)  # 添加优惠券名称
        if yhlx == "1":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpageyhlxselect,self.testpage.yhlx_option_djq)   #优惠类型选择代金券

        if yhms == "1":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpageyhmsselect,self.testpage.yhms_select_option_gdje)   #优惠模式选择固定金额
            self.activeweb.findElementByXpathAndInputNum(num, self.testpage.yhms_select_option_gdje_mz_input,gdjemzinputtext)  # 面值输入
        else:
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpageyhmsselect,self.testpage.yhms_select_option_sjje)  # 优惠模式选择随机金额
            self.activeweb.findElementByXpathAndInputNum(num, self.testpage.yhms_select_option_sjje_mz_min_input,sjjemzmiminputtext)  # 面值最小值输入
            self.activeweb.findElementByXpathAndInputNum(num, self.testpage.yhms_select_option_sjje_mz_max_input,sjjemzmimaxinputtext)  # 面值最大值输入

        self.activeweb.findElementByXpathAndInputNum(num, self.testpage.zdxf_input,zdxfinputtext) # 输入最低消费金额

        if sypt == "1":
            self.activeweb.findElementByXpathAndClickNum(num,self.testpage.sypt_QRindo_checkbox)  # 使用平台点选QRindo
        elif sypt == "2":
            self.activeweb.findElementByXpathAndClickNum(num,self.testpage.sypt_PaySDK_checkbox)  # 使用平台点选PaySDK

        if syfw == "1":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpagesyfwselect,self.testpage.syfw_select_option_bx)   #使用范围选择不限
        elif syfw == "2":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpagesyfwselect,self.testpage.syfw_select_option_zdhy)   #使用范围选择指定行业
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpage.syfw_select_option_zdhy_select,zdhyoptionxpath) # 指定行业选择一个行业
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.syfw_select_option_zdhy_tjhy_button)  # 点击添加行业按钮
        elif syfw == "3":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpagesyfwselect,self.testpage.syfw_select_option_zdsh)   #使用范围选择指定商户
            if isplsh:
                self.activeweb.findElementByXpathAndAndFileNumVue(num,
                                                             self.testpage.syfw_select_option_zdsh_pltjsh_button,plfilepath)  # 点击批量添加商户批量导入文件
            else:
                self.activeweb.findElementByXpathAndInputNum(num, self.testpage.syfw_select_option_zdsh_input,zdshinputtext)  # 输入商户
                self.activeweb.findElementByXpathAndClickNum(num, self.testpage.syfw_select_option_zdsh_tjsh_button)  # 点击添加商户按钮


        if sfzctq == "1":
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.sfzctq_kt_checkbox)  # 是否支持退券点选可退
        elif sfzctq == "2":
            self.activeweb.findElementByXpathAndClickNum(num, self.testpage.sfzctq_bkt_checkbox)  # 是否支持退券点选不可退

        self.activeweb.findElementByXpathAndClickNum(num, self.testpageconfirmbutton)   #点击确定按钮
        ################################优惠券创建完成#########################################




    def defineasserttextnum(self,num,testelexpath,expecttext):
        #断言是否存在某个文本
        testtext = self.activeweb.findElementByXpathAndReturnText(num,testelexpath)
        self.assertEqual(expecttext,testtext)
        self.activeweb.outPutMyLog("存在text:%s"%testtext)

    def defineisintable(self,num,testtablexpath,expecttext,tablecolnum):
        notexsitflag = True
        tabledic = self.activeweb.findElementByXpathAndReturnTableNum(num, testtablexpath)
        for value in tabledic.values():
            # self.activeweb.outPutMyLog("%s"% value[int(tablecolnum)])
            if str(expecttext).lower() in value[int(tablecolnum)].lower():
                self.assertTrue(True)
                self.activeweb.outPutMyLog("在%s中存在text:%s"% (value[int(tablecolnum)],expecttext))
                notexsitflag = False
                break
        if notexsitflag:
            self.activeweb.outPutMyLog("在%s不存在：%s"% (tabledic,expecttext))
            self.assertTrue(False)



    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,tfqd,rwlx,jllx,ishaspresent,
                             hdmcinputtext,hdsjstarttimedataxpath,hdsjstarttimesecondsxpath,
                             hdsjendtimedataxpath,hdsjendtimesecondsxpath,
                             hdysinputtext,tfqdselectoptionxpath,hdbztextareainputtext,
                             rwlxselectoptionxpath,jllxselectoptionxpath):
        def func(self):
            self.defineaddmerchantindividu(num,tfqd,rwlx,jllx,ishaspresent,
                             hdmcinputtext,hdsjstarttimedataxpath,hdsjstarttimesecondsxpath,
                             hdsjendtimedataxpath,hdsjendtimesecondsxpath,
                             hdysinputtext,tfqdselectoptionxpath,hdbztextareainputtext,
                             rwlxselectoptionxpath,jllxselectoptionxpath)
        return func

def __generateTestCases():
    from addmerchant.models import AddMerchant

    addmerchant_all = AddMerchant.objects.filter(iscompany=False).order_by('id')
    rows_count = addmerchant_all.count()

    for addmerchant in addmerchant_all:

        if len(str(addmerchant.id)) == 1:
            addmerchantid = '0000%s'% addmerchant.id
        elif len(str(addmerchant.id)) == 2:
            addmerchantid = '000%s' % addmerchant.id
        elif len(str(addmerchant.id)) == 3:
            addmerchantid = '00%s' % addmerchant.id
        elif len(str(addmerchant.id)) == 4:
            addmerchantid = '0%s' % addmerchant.id
        elif len(str(addmerchant.id)) == 5:
            addmerchantid = '%s' % addmerchant.id
        else:
            addmerchantid ='Id已经超过5位数，请重新定义'


        args = []
        args.append(addmerchant.id)
        args.append(addmerchant.isfictitious)
        args.append("%s_%s"%(addmerchant.brandnameinputtext,GetTimeStr().getTimeStr()))
        args.append(addmerchant.emailinputtext)
        args.append(addmerchant.contactnumberinputtext)
        args.append(addmerchant.merchanttypeselectoptionxpath)
        args.append(addmerchant.categoryselectoptionxpath)
        args.append(addmerchant.criteriaselectoptionxpath)
        args.append(addmerchant.siupinputtext)
        args.append(addmerchant.provinceselectoptionxpath)
        args.append(addmerchant.cityselectoptionxpath)
        args.append(addmerchant.districtinputtext)
        args.append(addmerchant.villageinputtext)
        args.append(addmerchant.postcodeinputtext)
        args.append(addmerchant.addressinputtext)
        args.append(addmerchant.photosiupimagefilepath)
        args.append(addmerchant.photonpwpcompanyimagefilepath)
        args.append(addmerchant.phototdpimagefilepath)
        args.append(addmerchant.nameinputtext)
        args.append(addmerchant.npwpinputtext)
        args.append(addmerchant.typeidselectoptionxpath)
        args.append(addmerchant.identitynumberinputtext)
        args.append(addmerchant.address2inputtext)
        args.append(addmerchant.nationalityselectoptionxpath)
        args.append(addmerchant.phoneinputtext)
        args.append(addmerchant.email2inputtext)
        args.append(addmerchant.photofullfacebustimagefilepath)
        args.append(addmerchant.locationphotoimagefilepath)
        args.append(addmerchant.photoofthecashiersdeskimagefilepath)
        args.append(addmerchant.otherphotoimagefilepath)
        args.append(addmerchant.bankselectoptionxpath)
        args.append(addmerchant.accountnameinputtext)
        args.append(addmerchant.accountnumberinputtext)
        args.append(addmerchant.qrindoaccountinputtext)


        setattr(TestCreateTicketClass, 'test_func_%s_%s' % (addmerchantid,addmerchant.testcasetitle),
                TestCreateTicketClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

    # file_name = "D:\\Users\\Administrator\\PycharmProjects\\seleniumweb\\sele\\dataconfig\\assertselectsearchmanager.xls"
    # sheet_id = 0
    # datasheet = GetData(file_name,sheet_id)   #实例化
    # # rows_count = datasheet.get_case_lines()   #获取表的行数
    # for i in range(1, rows_count):  # 循环，但去掉第一
    #     args = []
    #     args.append(i)
    #     args.append(datasheet.is_cookie(i))
    #     args.append(datasheet.get_url(i))
    #     args.append(datasheet.get_selectxpath(i))
    #     args.append(datasheet.get_selectoptiontext(i))
    #     args.append(datasheet.get_selectinputxpath(i))
    #     args.append(datasheet.get_selectinputtext(i))
    #     args.append(datasheet.get_searchbuttonxpath(i))
    #     args.append(datasheet.get_searchtableresultxpath(i))
    #     args.append(datasheet.get_colnum(i))
    #     args.append(datasheet.get_checktext(i))
    #
    #
    #     setattr(TestSearchClass, 'test_func_%s_%s' % (datasheet.get_id(i),datasheet.get_title(i)),
    #             TestSearchClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()









