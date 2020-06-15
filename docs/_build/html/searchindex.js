Search.setIndex({docnames:["Wallet","credits","credits.migrations","index","manage","modules","transfers","transfers.migrations","wallets","wallets.migrations"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":2,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,sphinx:56},filenames:["Wallet.rst","credits.rst","credits.migrations.rst","index.rst","manage.rst","modules.rst","transfers.rst","transfers.migrations.rst","wallets.rst","wallets.migrations.rst"],objects:{"":{Wallet:[0,0,0,"-"],credits:[1,0,0,"-"],manage:[4,0,0,"-"],transfers:[6,0,0,"-"],wallets:[8,0,0,"-"]},"Wallet.errors":{BaseError:[0,1,1,""],BeneficiaryNotExistError:[0,1,1,""],ChangeAccountNumberError:[0,1,1,""],InsufficientFundsError:[0,1,1,""],LowerZeroError:[0,1,1,""],NoOfferIdError:[0,1,1,""]},"Wallet.errors.BaseError":{get_details_response:[0,2,1,""]},"Wallet.errors.BeneficiaryNotExistError":{get_details_response:[0,2,1,""]},"Wallet.errors.ChangeAccountNumberError":{get_details_response:[0,2,1,""]},"Wallet.errors.InsufficientFundsError":{get_details_response:[0,2,1,""]},"Wallet.errors.LowerZeroError":{get_details_response:[0,2,1,""]},"Wallet.errors.NoOfferIdError":{get_details_response:[0,2,1,""]},"Wallet.tests":{BaseTest:[0,3,1,""],BaseTestWithWallets:[0,3,1,""]},"Wallet.tests.BaseTest":{client:[0,4,1,""],model_create:[0,2,1,""],setUp:[0,2,1,""]},"Wallet.tests.BaseTestWithWallets":{setUp:[0,2,1,""]},"credits.admin":{CreditAdmin:[1,3,1,""]},"credits.admin.CreditAdmin":{media:[1,2,1,""]},"credits.apps":{CreditsConfig:[1,3,1,""]},"credits.apps.CreditsConfig":{name:[1,4,1,""]},"credits.migrations":{"0001_initial":[2,0,0,"-"]},"credits.migrations.0001_initial":{Migration:[2,3,1,""]},"credits.migrations.0001_initial.Migration":{dependencies:[2,4,1,""],initial:[2,4,1,""],operations:[2,4,1,""]},"credits.models":{Credit:[1,3,1,""],Offer:[1,3,1,""],OfferComment:[1,3,1,""]},"credits.models.Credit":{DoesNotExist:[1,1,1,""],MultipleObjectsReturned:[1,1,1,""],amount:[1,4,1,""],credit_ballance:[1,4,1,""],get_type_display:[1,2,1,""],id:[1,4,1,""],is_paid:[1,4,1,""],objects:[1,4,1,""],rates:[1,4,1,""],type:[1,4,1,""]},"credits.models.Offer":{DoesNotExist:[1,1,1,""],MultipleObjectsReturned:[1,1,1,""],id:[1,4,1,""],objects:[1,4,1,""],offercomment_set:[1,4,1,""],text:[1,4,1,""],title:[1,4,1,""]},"credits.models.OfferComment":{DoesNotExist:[1,1,1,""],MultipleObjectsReturned:[1,1,1,""],author:[1,4,1,""],author_id:[1,4,1,""],comment:[1,4,1,""],id:[1,4,1,""],objects:[1,4,1,""],offer:[1,4,1,""],offer_id:[1,4,1,""],rate:[1,4,1,""]},"credits.serializers":{CreditDataSerializer:[1,3,1,""],OfferAvgRate:[1,3,1,""],OfferAvgRateSerializer:[1,3,1,""]},"credits.serializers.CreditDataSerializer":{Meta:[1,3,1,""]},"credits.serializers.CreditDataSerializer.Meta":{exclude:[1,4,1,""],model:[1,4,1,""]},"credits.tests":{OfferAvgRateTest:[1,3,1,""]},"credits.tests.OfferAvgRateTest":{setUp:[1,2,1,""],test_avg_rate:[1,2,1,""],test_no_offer_id_error:[1,2,1,""],url:[1,4,1,""]},"credits.views":{CreditViewSet:[1,3,1,""],OfferAvgRateViewSet:[1,3,1,""]},"credits.views.CreditViewSet":{basename:[1,4,1,""],description:[1,4,1,""],detail:[1,4,1,""],name:[1,4,1,""],queryset:[1,4,1,""],serializer_class:[1,4,1,""],suffix:[1,4,1,""]},"credits.views.OfferAvgRateViewSet":{avg:[1,2,1,""],basename:[1,4,1,""],description:[1,4,1,""],detail:[1,4,1,""],get_avg_rate:[1,2,1,""],get_offer_title:[1,2,1,""],name:[1,4,1,""],suffix:[1,4,1,""]},"transfers.apps":{TransfersConfig:[6,3,1,""]},"transfers.apps.TransfersConfig":{name:[6,4,1,""]},"transfers.migrations":{"0001_initial":[7,0,0,"-"]},"transfers.migrations.0001_initial":{Migration:[7,3,1,""]},"transfers.migrations.0001_initial.Migration":{dependencies:[7,4,1,""],initial:[7,4,1,""],operations:[7,4,1,""]},"transfers.models":{Transfer:[6,3,1,""]},"transfers.models.Transfer":{DoesNotExist:[6,1,1,""],MultipleObjectsReturned:[6,1,1,""],amount:[6,4,1,""],beneficiary_account:[6,4,1,""],currency:[6,4,1,""],get_currency_display:[6,2,1,""],get_next_by_transfer_date:[6,2,1,""],get_previous_by_transfer_date:[6,2,1,""],id:[6,4,1,""],objects:[6,4,1,""],source_account:[6,4,1,""],title:[6,4,1,""],transfer_date:[6,4,1,""]},"transfers.serializers":{TransfersDataSerializer:[6,3,1,""]},"transfers.serializers.TransfersDataSerializer":{Meta:[6,3,1,""]},"transfers.serializers.TransfersDataSerializer.Meta":{exclude:[6,4,1,""],model:[6,4,1,""]},"transfers.tests":{SimpleTransferTest:[6,3,1,""]},"transfers.tests.SimpleTransferTest":{test_beneficiary_not_exist_error:[6,2,1,""],test_insufficient_funds_error:[6,2,1,""],test_lower_zero_error:[6,2,1,""],test_transfer:[6,2,1,""],url:[6,4,1,""]},"transfers.views":{TransferViewSet:[6,3,1,""]},"transfers.views.TransferViewSet":{basename:[6,4,1,""],create:[6,2,1,""],description:[6,4,1,""],detail:[6,4,1,""],name:[6,4,1,""],suffix:[6,4,1,""],transfer_saldo_changes:[6,2,1,""]},"wallets.admin":{WalletAdmin:[8,3,1,""]},"wallets.admin.WalletAdmin":{media:[8,2,1,""]},"wallets.apps":{WalletsConfig:[8,3,1,""]},"wallets.apps.WalletsConfig":{name:[8,4,1,""]},"wallets.common":{get_all_from_table:[8,5,1,""],get_all_ids:[8,5,1,""],get_model_by_id:[8,5,1,""],get_user:[8,5,1,""],get_wallet_by_account_number:[8,5,1,""],get_zus_amount:[8,5,1,""],not_exist:[8,5,1,""]},"wallets.migrations":{"0001_initial":[9,0,0,"-"]},"wallets.migrations.0001_initial":{Migration:[9,3,1,""]},"wallets.migrations.0001_initial.Migration":{dependencies:[9,4,1,""],initial:[9,4,1,""],operations:[9,4,1,""]},"wallets.models":{CompanyData:[8,3,1,""],Wallet:[8,3,1,""]},"wallets.models.CompanyData":{DoesNotExist:[8,1,1,""],MultipleObjectsReturned:[8,1,1,""],company_start_date:[8,4,1,""],get_next_by_company_start_date:[8,2,1,""],get_previous_by_company_start_date:[8,2,1,""],id:[8,4,1,""],nip:[8,4,1,""],objects:[8,4,1,""],regon:[8,4,1,""],wallet:[8,4,1,""]},"wallets.models.Wallet":{DoesNotExist:[8,1,1,""],MultipleObjectsReturned:[8,1,1,""],account_number:[8,4,1,""],active:[8,4,1,""],ballance:[8,4,1,""],company_data:[8,4,1,""],company_data_id:[8,4,1,""],country:[8,4,1,""],creation_date:[8,4,1,""],id:[8,4,1,""],is_company:[8,4,1,""],objects:[8,4,1,""],user:[8,4,1,""],user_id:[8,4,1,""]},"wallets.serializers":{CompanyDataSerializer:[8,3,1,""],GroupSerializer:[8,3,1,""],UserSerializer:[8,3,1,""],WalletSerializer:[8,3,1,""]},"wallets.serializers.CompanyDataSerializer":{Meta:[8,3,1,""]},"wallets.serializers.CompanyDataSerializer.Meta":{exclude:[8,4,1,""],model:[8,4,1,""]},"wallets.serializers.GroupSerializer":{Meta:[8,3,1,""]},"wallets.serializers.GroupSerializer.Meta":{fields:[8,4,1,""],model:[8,4,1,""]},"wallets.serializers.UserSerializer":{Meta:[8,3,1,""]},"wallets.serializers.UserSerializer.Meta":{fields:[8,4,1,""],model:[8,4,1,""]},"wallets.serializers.WalletSerializer":{Meta:[8,3,1,""],update:[8,2,1,""]},"wallets.serializers.WalletSerializer.Meta":{fields:[8,4,1,""],model:[8,4,1,""]},"wallets.tests":{CRUDWalletTest:[8,3,1,""],EnglishWalletTest:[8,3,1,""],UpdateWalletTest:[8,3,1,""],ZusDayTest:[8,3,1,""]},"wallets.tests.CRUDWalletTest":{test_crud_1:[8,2,1,""],test_crud_2:[8,2,1,""],url:[8,4,1,""]},"wallets.tests.EnglishWalletTest":{test_get_query_params:[8,2,1,""],url:[8,4,1,""]},"wallets.tests.UpdateWalletTest":{get_company_data_by_nip:[8,2,1,""],get_wallet_company_data:[8,2,1,""],request:[8,4,1,""],test_update_company_data_1:[8,2,1,""],test_update_company_data_2:[8,2,1,""],test_update_company_data_3:[8,2,1,""],url:[8,4,1,""]},"wallets.tests.ZusDayTest":{test_zus_day_method:[8,2,1,""],url:[8,4,1,""]},"wallets.views":{GroupViewSet:[8,3,1,""],UserViewSet:[8,3,1,""],WalletViewSet:[8,3,1,""]},"wallets.views.GroupViewSet":{basename:[8,4,1,""],description:[8,4,1,""],detail:[8,4,1,""],name:[8,4,1,""],queryset:[8,4,1,""],serializer_class:[8,4,1,""],suffix:[8,4,1,""]},"wallets.views.UserViewSet":{basename:[8,4,1,""],description:[8,4,1,""],detail:[8,4,1,""],name:[8,4,1,""],queryset:[8,4,1,""],serializer_class:[8,4,1,""],suffix:[8,4,1,""]},"wallets.views.WalletViewSet":{basename:[8,4,1,""],create:[8,2,1,""],create_billnumber:[8,2,1,""],description:[8,4,1,""],detail:[8,4,1,""],get_queryset:[8,2,1,""],list:[8,2,1,""],name:[8,4,1,""],serializer_class:[8,4,1,""],suffix:[8,4,1,""],update:[8,2,1,""],zus_day:[8,2,1,""]},Wallet:{asgi:[0,0,0,"-"],errors:[0,0,0,"-"],fin:[0,0,0,"-"],settings:[0,0,0,"-"],tests:[0,0,0,"-"],urls:[0,0,0,"-"],wsgi:[0,0,0,"-"]},credits:{admin:[1,0,0,"-"],apps:[1,0,0,"-"],migrations:[2,0,0,"-"],models:[1,0,0,"-"],serializers:[1,0,0,"-"],tests:[1,0,0,"-"],views:[1,0,0,"-"]},manage:{main:[4,5,1,""]},transfers:{admin:[6,0,0,"-"],apps:[6,0,0,"-"],migrations:[7,0,0,"-"],models:[6,0,0,"-"],serializers:[6,0,0,"-"],tests:[6,0,0,"-"],views:[6,0,0,"-"]},wallets:{admin:[8,0,0,"-"],apps:[8,0,0,"-"],common:[8,0,0,"-"],migrations:[9,0,0,"-"],models:[8,0,0,"-"],serializers:[8,0,0,"-"],tests:[8,0,0,"-"],views:[8,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","exception","Python exception"],"2":["py","method","Python method"],"3":["py","class","Python class"],"4":["py","attribute","Python attribute"],"5":["py","function","Python function"]},objtypes:{"0":"py:module","1":"py:exception","2":"py:method","3":"py:class","4":"py:attribute","5":"py:function"},terms:{"0001_initi":[1,5,6,8],"02t16":8,"41z":8,"class":[0,1,2,6,7,8,9],"default":8,"new":8,"return":8,"static":[0,8],"true":[2,6,7,8,9],"while":8,For:0,ZUS:8,__first__:[2,9],accessor:[1,8],account:8,account_numb:[8,9],action:8,activ:[8,9],admin:[0,5],admin_sit:[1,8],administr:4,alia:[1,6,8],all:[0,1,8],allow:[1,8],amount:[1,2,6,7],api:[0,1,8],apicli:0,apiexcept:0,apitestcas:0,app:5,app_label:[2,7,9],app_modul:[1,6,8],app_nam:[1,6,8],appconfig:[1,6,8],applic:0,arg:[6,8],asgi:5,auth:[2,8,9],author:[1,2],author_id:1,autofield:[2,7,9],avg:1,avg_rat:1,ballanc:[8,9],base:[0,1,2,6,7,8,9],baseerror:0,basenam:[1,6,8],basetest:[0,1],basetestwithwallet:[0,6,8],basic:0,below:1,beneficiari:0,beneficiary_account:[6,7],beneficiarynotexisterror:0,bigintegerfield:9,booleanfield:[2,9],built:1,callabl:0,changeaccountnumbererror:0,charfield:[1,2,6,7,9],charg:8,check:8,child:[1,8],children:[1,8],client:0,com:0,command:4,comment:[1,2],common:5,compani:0,company1:8,company2:8,company_data:[8,9],company_data_id:8,company_start_d:[8,9],companydata:[8,9],companydataseri:8,config:[0,1,6,8],contain:[0,8],content:[3,5],contrib:[1,8],core:[1,6,8],countri:[8,9],creat:[0,1,6,8],create_billnumb:8,create_forward_many_to_many_manag:1,createmodel:[2,7,9],creation_d:[8,9],credit:[3,5],credit_bal:[1,2],creditadmin:1,creditdataseri:1,creditsconfig:1,creditviewset:1,crudwallettest:8,currenc:[6,7],data:[0,1,6,8],datetimefield:[6,7,8,9],decimalfield:[7,9],defer:[1,6,8],defin:1,deleg:1,delet:8,depend:[2,7,9],deploy:0,descript:[1,6,8],detail:[1,6,8],dict:0,django:[0,1,2,4,6,7,8,9],djangoproject:0,doc:0,doesnotexist:[1,6,8],dynam:1,edit:[1,8],email:8,empti:[1,6,8],endpoint:[1,8],england:8,englishwallettest:8,error:5,exampl:[1,8],except:[0,1,6,8],exclud:[1,6,8],execut:[1,6,8],expos:0,fals:[6,8],fee:8,field:[1,2,6,7,8,9],file:0,fin:5,first:[1,6,8],foreignkei:[1,2,8,9],forward:[1,8],forwardmanytoonedescriptor:[1,8],forwardonetoonedescriptor:[1,8],from:[1,6,8],full:0,gener:[0,8],get_all_from_t:8,get_all_id:8,get_avg_r:1,get_company_data_by_nip:8,get_currency_displai:6,get_details_respons:0,get_model_by_id:8,get_next_by_company_start_d:8,get_next_by_transfer_d:6,get_offer_titl:1,get_previous_by_company_start_d:8,get_previous_by_transfer_d:6,get_queryset:8,get_type_displai:1,get_us:8,get_wallet_by_account_numb:8,get_wallet_company_data:8,get_zus_amount:8,group:8,groupseri:8,groupviewset:8,handl:8,howto:0,http:0,hyperlinkedmodelseri:8,iban:8,implement:1,index:3,inform:0,initi:[2,7,9],instanc:[0,1,6,8],insufficientfundserror:0,integerfield:2,is_compani:[8,9],is_next:[6,8],is_paid:[1,2],kwarg:[1,6,8],level:0,like:0,line:4,list:[0,8],load:[1,6,8],lowerzeroerror:0,main:4,manag:[1,3,5,6,8],mani:[1,8],media:[1,8],meta:[1,6,8],method:[0,8],methodnam:[0,1,6,8],migrat:[1,5,6,8],model:[0,2,5,7,9],model_cr:0,model_id:8,modeladmin:[1,8],modelseri:[1,6,8],modelviewset:[1,6,8],modifi:8,modul:[3,5],more:0,most:1,multipleobjectsreturn:[1,6,8],name:[0,1,2,6,7,8,9],nip:[8,9],none:[1,6,8],noofferiderror:0,not_exist:8,number:8,object:[0,1,6,8],objectdoesnotexist:[1,6,8],offer:[1,2],offer_id:[0,1],offer_nam:1,offer_r:1,offeravgr:1,offeravgrateseri:1,offeravgratetest:1,offeravgrateviewset:1,offercom:[1,2],offercomment_set:1,one:[1,8],onetoonefield:[8,9],oper:[2,7,9],option:[1,8],packag:[3,5],page:3,param:[0,8],paramet:[0,8],params_list:0,parent:[1,8],place:8,poland:8,post:8,prepar:0,project:0,properti:[1,8],provid:[0,8],put:8,queri:[1,6,8],queryset:[1,8],rate:[1,2],read:[1,6,8],ref:0,regon:[8,9],relat:[1,2,8,9],related_nam:[1,8],request:[1,6,8],rest_framework:[0,1,6,8],restaur:8,revers:[1,8],reversemanytoonedescriptor:1,reverseonetoonedescriptor:8,row:0,runtest:[0,1,6,8],search:3,see:0,serial:5,serializer_class:[1,8],set:5,setup:[0,1],side:[1,8],simpletransfertest:6,source_account:[6,7],start_dat:8,startproject:0,str:8,subclass:[1,8],submodul:5,subpackag:5,suffix:[1,6,8],task:4,test:5,test_avg_r:1,test_beneficiary_not_exist_error:6,test_crud_1:8,test_crud_2:8,test_get_query_param:8,test_insufficient_funds_error:6,test_lower_zero_error:6,test_no_offer_id_error:1,test_transf:6,test_update_company_data_1:8,test_update_company_data_2:8,test_update_company_data_3:8,test_zus_day_method:8,text:[1,2],textfield:2,thi:[0,1,6,8],time:[1,6,8],titl:[1,2,6,7],topic:0,transfer:[3,5],transfer_d:[6,7],transfer_saldo_chang:6,transfersconfig:6,transfersdataseri:6,transferviewset:6,type:[1,2],ulr:8,updat:8,updatewallettest:8,url:[1,5,6,8],user1:8,user2:8,user3:8,user:[0,1,8,9],user_id:8,usernam:8,userseri:8,userviewset:8,using:0,util:4,validated_data:8,valu:[0,1,6,8],variabl:0,via:[1,8],view:5,viewset:[1,6,8],wallet:[1,6],walletadmin:8,walletsconfig:8,walletseri:8,walletviewset:8,when:[1,6,8],wrapper:[1,6,8],wsgi:5,zus_dai:8,zusdaytest:8},titles:["Wallet package","credits package","credits.migrations package","Welcome to Virtual Wallet\u2019s documentation!","manage module","Virtual Wallet","transfers package","transfers.migrations package","wallets package","wallets.migrations package"],titleterms:{"0001_initi":[2,7,9],admin:[1,6,8],app:[1,6,8],asgi:0,common:8,content:[0,1,2,6,7,8,9],credit:[1,2],document:3,error:0,fin:0,indic:3,manag:4,migrat:[2,7,9],model:[1,6,8],modul:[0,1,2,4,6,7,8,9],packag:[0,1,2,6,7,8,9],serial:[1,6,8],set:0,submodul:[0,1,2,6,7,8,9],subpackag:[1,6,8],tabl:3,test:[0,1,6,8],transfer:[6,7],url:0,view:[1,6,8],virtual:[3,5],wallet:[0,3,5,8,9],welcom:3,wsgi:0}})