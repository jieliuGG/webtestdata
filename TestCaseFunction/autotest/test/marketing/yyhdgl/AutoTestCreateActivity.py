import unittest

from webtestdata.settings import WEB_URL_TITLE,MANAGER_LOGIN_ACCOUNT,MANAGER_LOGIN_PASSWORD,MARKETING_CREATE_ACTIVITYID
from webtestdata.settings import ISONLINE    #导入是否现网配置标识
from webtestdata.settings import TEST_WEB_URL_TITLE,TEST_MANAGER_LOGIN_ACCOUNT,TEST_MANAGER_LOGIN_PASSWORD   #导入测试环境参数
from webtestdata.settings import ONLINE_WEB_URL_TITLE,ONLINE_MANAGER_LOGIN_ACCOUNT,ONLINE_MANAGER_LOGIN_PASSWORD  #导入现网环境参数

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
from TestCaseFunction.autotest.config.page.marketing.yyhdgl.activityCreatePage import ActivityCreatePage   #导入创建活动页
from TestCaseFunction.autotest.config.page.marketing.yyhdgl.ticketCreatePage import TicketCreatePage   #导入创建优惠券页
from TestCaseFunction.autotest.config.page.marketing.yyhdgl.activityListPage import ActivityListPage   #导入活动列表页
from TestCaseFunction.autotest.config.page.marketing.yyhdgl.activityDetailsPage import ActivityDetialsPage #导入活动详情页




class TestCreateActivityClass(unittest.TestCase):  # 创建测试类


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

        if ISONLINE:
            self.activeweb.findElementByXpathAndInput(LoginPage().account,ONLINE_MANAGER_LOGIN_ACCOUNT)
            self.activeweb.findElementByXpathAndInput(LoginPage().password,ONLINE_MANAGER_LOGIN_PASSWORD)
        else:
            self.activeweb.findElementByXpathAndInput(LoginPage().account,TEST_MANAGER_LOGIN_ACCOUNT)
            self.activeweb.findElementByXpathAndInput(LoginPage().password,TEST_MANAGER_LOGIN_PASSWORD)

        self.activeweb.findElementByXpathAndClick(LoginPage().loginbutton)
        self.activeweb.delayTime(3)
        self.testpage = ActivityCreatePage()
        self.testpageurl =self.testpage.pageurl   #测试页面url
        self.testpagehdmcinput = self.testpage.hdmc_input       # ---基础信息---#   活动名称输入框路劲
        self.testpagehdlxselect = self.testpage.hdlx_select       # ---基础信息---#   活动类型选项框路径
        self.testpagehdsjstarttime = self.testpage.hdsj_starttime # ---基础信息---#   活动时间开始时间输入框路径
        self.testpagehdsjendtime = self.testpage.hdsj_endtime  # ---基础信息---#   活动时间结束时间输入框路径
        self.testpagehdysinput  = self.testpage.hdys_input   # ---基础信息---#   活动预算输入框路径

        self.testpagehdbztextarea = self.testpage.hdbz_textarea   # ---基础信息---#  活动备注多行输入框路径

        self.testpagejllxselect = self.testpage.jllx_select     # ---活动奖励---# 奖励类型下拉框路径
        self.testpagewtjlp = self.testpage.w_tjlp    # ---活动奖励---# 未添加礼品时，“添加礼品”文字链接路径

        self.testpagecancelbutton = self.testpage.cancelbutton   #取消按钮
        self.testpagesubmitbutton = self.testpage.submitbutton   #提交按钮

        ######################创建优惠券页面###############################
        self.ticketcreatepage = TicketCreatePage()   #创建优惠券页
        self.ticketcreatepage_kcsl_input  = self.ticketcreatepage.kcsl_input   #第一部分# 库存数量输入框路径
        self.ticketcreatepage_qyxq_select = self.ticketcreatepage.qyxq_select   #第一部分# 券有效期选择框路径
        self.ticketcreatepage_yhqsm_areatext  = self.ticketcreatepage.yhqsm_areatext    #第一部分# 优惠券说明多行输入框路径
        self.ticketcreatepage_yhqmc_input = self.ticketcreatepage.yhqmc_input    #第二部分# 优惠券名称输入框路径
        self.ticketcreatepage_yhlx_select = self.ticketcreatepage.yhlx_select    #第二部分# 优惠类型选择框路径
        self.ticketcreatepage_yhms_select = self.ticketcreatepage.yhms_select    #第二部分# 优惠模式选择框路径
        self.ticketcreatepage_zdxf_input = self.ticketcreatepage.zdxf_input    #第二部分# 最低消费输入框路径
        self.ticketcreatepage_zfqdxz_select  = self.ticketcreatepage.zfqdxz_select     #第二部分# 支付渠道限制选择框路径
        self.ticketcreatepage_syfw_select   = self.ticketcreatepage.syfw_select     #第二部分# 使用范围选择框路径

        self.ticketcreatepage_confirm_button = self.ticketcreatepage.confirm_button   #页面 确定按钮

        ######################活动列表页###############################
        self.activitylistpage = ActivityListPage()   #活动列表页
        self.activitylistpage_searchtableresult = self.activitylistpage.searchtableresult

        ######################待上线活动详情页###############################
        self.activitydetialspage = ActivityDetialsPage()   #活动列表页



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
    #投放渠道一级为1表示内部渠道，为2表示外部渠道
    #投放渠道二级为0表示全选，为1，2，等表示选一项和选多项组合，程序中只有全选和选择一项的情况
    # 任务类型为1表示注册，为2表示交易类型
    #奖励类型1表示固定奖励
    def definecreateactivity(self,num,
                             hdmcinputtext,hdlx,
                             hdysinputtext,
                             tfqdyj, tfqdej,hdbztextareainputtext,
                             rwlx,tjrwxz,
                             jyjylx, jyzffs,
                             jymgyhzdcycsinputtext,jymgyhmrcycsinputtext,
                             jllx,iscancel):
        self.activeweb.getUrl(self.testpageurl)
        self.activeweb.delayTime(3)

        #创建活动
        #填入基础信息部分
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagehdmcinput, hdmcinputtext)   #输入活动名称

        #选择活动类型
        if hdlx == "1":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpagehdlxselect,self.testpage.hdlx_select_lx_option)  # 选择活动类型选择拉新
        elif hdlx == "2":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpagehdlxselect,self.testpage.hdlx_select_ch_option)  # 选择活动类型选择促活
        elif hdlx == "3":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpagehdlxselect,self.testpage.hdlx_select_lc_option)  # 选择活动类型选择留存
        elif hdlx == "4":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpagehdlxselect,self.testpage.hdlx_select_zh_option)  # 选择活动类型选择转化
        elif hdlx == "5":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.testpagehdlxselect,self.testpage.hdlx_select_tsbc_option)  # 选择活动类型选择投诉补偿


        self.activeweb.findElementByXpathAndClickAbountData(num,self.testpagehdsjstarttime,self.testpage.hdsj_starttime_daytime,pathright=self.testpage.hdsj_starttime_rightmove,pathconfirm=self.testpage.hdsj_starttime_queding)   #点选活动时间开始时间
        self.activeweb.findElementByXpathAndClickAbountData(num,self.testpagehdsjendtime ,self.testpage.hdsj_endtime_daytime,pathright=self.testpage.hdsj_endtime_rightmove,pathconfirm=self.testpage.hdsj_endtime_queding)   #点选活动时间结束时间
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagehdysinput, hdysinputtext)   #输入活动预算
        self.activeweb.findElementByXpathAndInputNum(num,self.testpagehdbztextarea, hdbztextareainputtext)   #输入活动备注

        #填入活动奖励部分
        if jllx =="1":
            self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.testpagejllxselect,self.testpage.jllx_select_gdjl_option)  # 选择奖励类型为固定奖励
        self.activeweb.findElementByXpathAndClickNum(num, self.testpagewtjlp)  # 点击添加礼品文字链接(还未添加礼品)

        #进入创建优惠券页，新建优惠券
        #第一部分
        self.activeweb.findElementByXpathAndClickNum(num, self.ticketcreatepage.ffzt_kq_checkbox)  # 点击发放状态开始对应的选项框
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num,self.ticketcreatepage_qyxq_select,self.ticketcreatepage.qyxq_select_option_xdsj)  # 选择券有效期选项为相对时间
        self.activeweb.findElementByXpathAndInputNum(num, self.ticketcreatepage.qyxq_select_option_xdsj_ts_input, "2")  # 输入相对时间为2天
        self.activeweb.findElementByXpathAndClickNum(num, self.ticketcreatepage.yxcbcdf_pt_checkbox)  # 点击营销成本承担方中的平台前的选项框
        self.activeweb.findElementByXpathAndInputNum(num, self.ticketcreatepage_yhqsm_areatext, "开启-不限库存数-相对时间(相对2天)-平台-代金券-固定金额（面值2000）-不限最低消费-使用平台（点选QRindo）-不限使用范围-支持退券")  # 输入优惠券说明
        #第二部分
        self.activeweb.findElementByXpathAndInputNum(num, self.ticketcreatepage_yhqmc_input,"test_优惠券_%s" % GetTimeStr().getTimeStr())  # 添加优惠券名称
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.ticketcreatepage_yhlx_select,self.ticketcreatepage.yhlx_option_djq)   #优惠类型选择代金券
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.ticketcreatepage_yhms_select,self.ticketcreatepage.yhms_select_option_gdje)   #优惠模式选择固定金额
        self.activeweb.findElementByXpathAndInputNum(num, self.ticketcreatepage.yhms_select_option_gdje_mz_input,"2000")  # 面值输入2000
        if ISONLINE:
            #点击使用平台第一个选项
            if not self.activeweb.findElementByXpath(self.ticketcreatepage.sypt_mbmpay_checkbox).is_selected():
                self.activeweb.findElementByXpathAndClickNum(num,self.ticketcreatepage.sypt_mbmpay_checkbox)  # 使用平台点选mbmpay
            if self.activeweb.findElementByXpath(self.ticketcreatepage.sypt_mydisrupto_checkbox).is_selected():
                self.activeweb.findElementByXpathAndClickNum(num,self.ticketcreatepage.sypt_mydisrupto_checkbox)  # 使用平台点选mydisrupto
            if self.activeweb.findElementByXpath(self.ticketcreatepage.sypt_QRindo_checkbox).is_selected():
                self.activeweb.findElementByXpathAndClickNum(num,self.ticketcreatepage.sypt_QRindo_checkbox)  # 使用平台点选QRindo
        else:
            self.activeweb.findElementByXpathAndClickNum(num,self.ticketcreatepage.sypt_mbmpay_checkbox)  # 使用平台点选mbmpay
            self.activeweb.findElementByXpathAndClickNum(num,self.ticketcreatepage.sypt_mydisrupto_checkbox)  # 使用平台点选mydisrupto
            self.activeweb.findElementByXpathAndClickNum(num,self.ticketcreatepage.sypt_QRindo_checkbox)  # 使用平台点选QRindo
            self.activeweb.findElementByXpathAndClickNum(num,self.ticketcreatepage.sypt_qrindomerchantcashier_checkbox)  # 使用平台点选qrindomerchantcashier
            self.activeweb.findElementByXpathAndClickNum(num,self.ticketcreatepage.sypt_PaySDK_checkbox)  # 使用平台点选PaySDK
        self.activeweb.findElementByXpathAndClickOptionXpathNum(num, self.ticketcreatepage_syfw_select,self.ticketcreatepage.syfw_select_option_bx)   #使用范围选择不限
        # self.activeweb.findElementByXpathAndClickNum(num, self.ticketcreatepage.kfyqthddj_bkdjsy_checkbox)  # 可否与其他活动叠加点选不可叠加使用
        self.activeweb.findElementByXpathAndClickNum(num, self.ticketcreatepage.sfzctq_kt_checkbox)  # 是否支持退券点选可退

        self.activeweb.findElementByXpathAndScriptClickNum(num, self.ticketcreatepage.confirm_button)   #点击确定按钮
        ################################优惠券创建完成#########################################

        # self.activeweb.delayTime(1000)


        if iscancel:
            self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpagecancelbutton)  # 点击取消按钮
        else:
            self.activeweb.findElementByXpathAndScriptClickNum(num, self.testpagesubmitbutton)  # 点击提交按钮
            # 断言活动列表中是否有新增加的活动
            self.defineisintable(num, self.activitylistpage_searchtableresult, hdmcinputtext, 1)

            #获取活动ID
            self.activeweb.findElementByXpathAndScriptClickNum(num, self.activitylistpage.table_justone_content_dsx_xq)  # 点击列表中第一行中的"详情"
            getid = self.activeweb.findElementByXpathAndReturnText(num,self.activitydetialspage.hdid)
            self.activeweb.outPutMyLog("新建活动id：%s"% getid)
            #保存活动id
            filename = "createactivityid.txt"
            GetTimeStr().writeText(filename,getid)



            # filename = 'createactivityid.txt'
            # GetTimeStr().writeText(filename,getid)





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
                self.activeweb.outPutMyLog("在【%s】中存在:【%s】"% (value[int(tablecolnum)],expecttext))
                notexsitflag = False
                break
        if notexsitflag:
            self.activeweb.outPutMyLog("在【%s】不存在：【%s】"% (tabledic,expecttext))
            self.assertTrue(False)



    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,hdmcinputtext,hdlx,
                    hdysinputtext,
                    tfqdyj, tfqdej,hdbztextareainputtext,
                    rwlx,tjrwxz,
                    jyjylx, jyzffs,
                    jymgyhzdcycsinputtext,jymgyhmrcycsinputtext,
                    jllx,iscancel):
        def func(self):
            self.definecreateactivity(num,
                             hdmcinputtext,hdlx,
                                      hdysinputtext,
                             tfqdyj, tfqdej,hdbztextareainputtext,
                             rwlx,tjrwxz,
                             jyjylx, jyzffs,
                             jymgyhzdcycsinputtext,jymgyhmrcycsinputtext,
                             jllx,iscancel)
        return func

def __generateTestCases():
    from addactivity.models import AddActivity

    addactivity_all = AddActivity.objects.filter(testproject="营销系统").filter(testmodule="运营活动管理").filter(testpage="创建活动").filter(id=16).order_by('id')
    rows_count = addactivity_all.count()

    for addactivity in addactivity_all:

        if len(str(addactivity.id)) == 1:
            addactivityid = '0000%s'% addactivity.id
        elif len(str(addactivity.id)) == 2:
            addactivityid = '000%s' % addactivity.id
        elif len(str(addactivity.id)) == 3:
            addactivityid = '00%s' % addactivity.id
        elif len(str(addactivity.id)) == 4:
            addactivityid = '0%s' % addactivity.id
        elif len(str(addactivity.id)) == 5:
            addactivityid = '%s' % addactivity.id
        else:
            addactivityid ='Id已经超过5位数，请重新定义'


        args = []
        args.append(addactivity.id)
        args.append("%s_%s"%(addactivity.hdmcinputtext,GetTimeStr().getTimeStr()))
        args.append(addactivity.hdlx)
        args.append(addactivity.hdysinputtext)
        args.append(addactivity.tfqdyj)
        args.append(addactivity.tfqdej)
        args.append(addactivity.hdbztextareainputtext)
        args.append(addactivity.rwlx)
        args.append(addactivity.tjrwxz)
        args.append(addactivity.jyjylx)
        args.append(addactivity.jyzffs)
        args.append(addactivity.jymgyhzdcycsinputtext)
        args.append(addactivity.jymgyhmrcycsinputtext)
        args.append(addactivity.jllx)
        args.append(addactivity.iscancel)

        setattr(TestCreateActivityClass, 'test_func_%s_%s' % (addactivityid,addactivity.testcasetitle),
                TestCreateActivityClass.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

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










