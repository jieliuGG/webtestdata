from webtestdata.settings import ISONLINE    #导入是否现网配置标识
from webtestdata.settings import TEST_WEB_URL_TITLE   #导入测试环境参数
from webtestdata.settings import ONLINE_WEB_URL_TITLE  #导入现网环境参数

from TestCaseFunction.util.gettimestr import GetTimeStr

class IndividuDetailsPage:
    filename = "merchantid.txt"
    detailsmerchantid = GetTimeStr().readText(filename)
    if ISONLINE:
        pageurl = "%s/nereus/agent/v/#/merchant/detail/%s" % (ONLINE_WEB_URL_TITLE,detailsmerchantid)
    else:
        pageurl = "%s/nereus/agent/v/#/merchant/detail/%s" % (TEST_WEB_URL_TITLE, detailsmerchantid)

    #---Basic info---#
    basicinfo = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/span"
    basicinfotext = "Basic info"
    # ---key---#
    merchantid  = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[1]/label"
    merchantidtext = "Merchant ID:"
    loginaccount = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[2]/label"
    loginaccounttext = "Login account:"
    agent = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[3]/label"
    agenttext = "Agent:"
    brandname = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[1]/label"
    brandnametext = "Brand name:"
    # ---value---#
    merchantidvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[1]/div/div"
    merchantidvaluetext = AGENT_DETAILS_MERCHANTID
    loginaccountvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[2]/div/div"
    loginaccountvaluetext = "62%s"% AGENT_LOGIN_ACCOUNT
    agentvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/form/div[3]//div/div"
    agentvaluetext = "test"
    brandnamevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div"
    brandnamevaluetext = "test_individu_20190415152327"

    #---Merchant info---#
    merchantinfo = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/span"
    merchantinfotext = "Merchant info"
    # ---key---#
    # email = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[2]/label"
    # emailtext = "Email:"
    # contactnumber = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[3]/label"
    # contactnumbertext = "Contact number:"
    merchanttype = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[4]/label"
    merchanttypetext = "Merchant type:"
    category = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/label"
    categorytext = "Category:"
    criteria = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[6]/label"
    criteriatext = "Criteria:"
    # siup = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[7]/label"
    # siuptext = "SIUP:"
    province = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[8]/label"
    provincetext = "Province:"
    city = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[9]/label"
    citytext = "City:"
    district = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[10]/label"
    districttext = "District:"
    village = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[11]/label"
    villagetext = "Village:"
    postcode = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[12]/label"
    postcodetext = "Postcode:"
    address = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[13]/label"
    addresstext = "Address:"
    # companyname = ""
    # officialwebsite = ""
    # npwptaxid = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[16]/label"
    #
    # photosiup = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[14]/label"
    # photosiuptext = "Photo SIUP:"
    photonpwpcompany = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[15]/label"
    photonpwpcompanytext = "Photo NPWP Company:"
    phototdp = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[16]/label"
    phototdptext = "Photo TDP:"

    # ---value---#
    # emailvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div"
    # emailvaluetext = "xiangkaizheng@iapppay.com"
    # contactnumbervalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[3]/div/div"
    # contactnumbervaluetext = "test_individu"
    merchanttypevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[4]/div/div"
    merchanttypevaluetext = "Individu"
    categoryvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div/div"
    categoryvaluetext = "PASSENGER TRANSPORTATION"
    criteriavalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[6]/div/div"
    criteriavaluetext = "Micro"
    # siupvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[7]/div/div"
    # siupvaluetext = "test_individu"
    provincevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[8]/div/div"
    provincevaluetext = "JAWA BARAT"
    cityvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[9]/div/div"
    cityvaluetext = "Jawa Barat"
    districtvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[10]/div/div"
    districtvaluetext = "test_individu"
    villagevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[11]/div/div"
    villagevaluetext = "test_individu"
    postcodevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[12]/div/div"
    postcodevaluetext = "test_individu"
    addressvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[13]/div/div"
    addressvaluetext = "test_individu"
    # companynamevalue = ""
    # officialwebsitevalue = ""
    # npwptaxidvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/form/div[16]/div/div"
    # photosiupimagevalue = ""
    photonpwpcompanyimagevalue = ""
    phototdpimagevalue = ""

    #---Owner / Person in Charge info---#
    ownerpersoninchangeinfo = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[1]/span"
    ownerpersoninchangeinfotext = "Owner / Person in Charge info"
    # ---key---#
    name = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[1]/label"
    nametext = "Name:"
    npwp = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[2]/label"
    npwptext = "NPWP:"
    typeid = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[3]/label"
    typeidtext = "Type ID:"
    identitynumber = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[4]/label"
    identitynumbertext = "Identity number:"
    address2 = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[5]/label"
    address2text = "Address:"
    nationality = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[6]/label"
    nationalitytext = "Nationality:"
    phone = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[7]/label"
    phonetext = "Phone:"
    email2 = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[8]/label"
    email2text = "Email:"
    photofullfacebust = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[9]/label"
    photofullfacebusttext = "Photo PIC Full-faceBust:"
    # ---value---#
    namevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[1]/div/div"
    namevaluetext = "test_20190411"
    npwpvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[2]/div/div"
    npwpvaluetext = "test_individu"
    typeidvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[3]/div/div"
    typeidvaluetext = "KTP"
    identitynumbervalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[4]/div/div"
    identitynumbervaluetext = "test_individu"
    address2value = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[5]/div/div"
    address2valuetext = "test_individu"
    nationalityvalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[6]/div/div"
    nationalityvaluetext = "Indonesian"
    phonevalue = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[7]/div/div"
    phonevaluetext = "test_individu"
    email2value= "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[8]/div/div"
    email2valuetext = "xiangkaizheng@iapppay.com"
    photofullfacebustimage ="/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div/form/div[9]/div/div/div/div/div[1]/figure/a/img"

    #---Profile Photos---#
    profilephotos = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[4]/div[1]/span"
    profilephotostext = "Profile Photos"
    # ---key---#
    locationphoto = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[4]/div[2]/div/form/div[1]/label"
    locationphototext = "Location Photo:"
    photoofthecashiersdesk = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[4]/div[2]/div/form/div[2]/label"
    photoofthecashiersdesktext = "Photo of the cashiers desk:"
    otherphoto = "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[4]/div[2]/div/form/div[3]/label"
    otherphototext = "Other Photo:"




