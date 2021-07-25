from django.shortcuts import render,redirect
from app1.models import account,rule,awarenessprgm,victim,victim1a,participants,idgen1,complaint,tbl_login,tblcomp_action,tbl_child,tblpolice_comp,tbl_womencell,tbl_chat
import datetime
from django.core.mail import send_mail
from cryptography.fernet import Fernet

def index(request):
    return render(request,"header.html")

def adminheader(request):
    return render(request,"header.html")

def addaccount(request):  
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else:
        data = idgen1.objects.get(id=1)
        f=data.Acct_id 
        f=f+1
        f1="ACCT"+str(f)
        request.session['ACC_ID']=f
        return render(request,"addaccount.html",{'ff':f1})
# Create your views here.
def addaccount1(request):
    if request.method == 'POST':
        data = account()
        data.Acct_id = request.POST.get('Acct_id')
        data.role = request.POST.get('role')
        data.contact_person = request.POST.get('contact_person')
        data.phone = request.POST.get('phone')
        data.email = request.POST.get('email')
        data.address = request.POST.get('address')
        data.status ="active"
        data.save()
        s=request.session['ACC_ID']
        data2=idgen1.objects.get(id=1)
        data2.Acct_id=s
        data2.save()
        data3=tbl_login()
        data3.username=request.POST.get('Acct_id')
        data3.password=request.POST.get('phone')
        data3.category=request.POST.get('role')
        data3.save()
        send_mail('HELPING HANDS','username'+request.POST.get('Acct_id')+'password'+request.POST.get('phone'),'from@example.co',[request.POST.get('email'),])

        return redirect ('/addaccount')

def remove_acct(request):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else:
        items = account.objects.all()
        return render(request,"remove_acct.html",{'it':items})

def remove_acct1(request,id):
    items = account.objects.get(id=id)
    items.delete()
    return redirect('/remove_acct')


def addviolation(request):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else: 
        data = idgen1.objects.get(id=1)
        f=data.Rule_id 
        f=f+1
        f1="RL"+str(f)
        request.session['RL_ID']=f  
        return render(request,"addviolation.html",{'ff':f1})

def addviolation1(request):
    if request.method == 'POST':
        data = rule()
        data.Rule_id = request.POST.get('Rule_id')
        data.violations = request.POST.get('violations')
        data.rules = request.POST.get('rules')
        data.punishments = request.POST.get('punishments')
        data.save()
        s=request.session['RL_ID']
        data2=idgen1.objects.get(id=1)
        data2.Rule_id=s
        data2.save()
        return redirect ('/addviolation')


    
def remove_violation(request):
    items = rule.objects.all()
    return render(request,"remove_violation.html",{'it':items})

def remove_violation1(request,id):
    items = rule.objects.get(id=id)
    items.delete()
    return redirect('/remove_violation')


def announceprgm(request): 
        data = idgen1.objects.get(id=1)
        f=data.Awarenessprgm_id 
        f=f+1
        f1="AWRNS"+str(f)
        request.session['AWRN_ID']=f  
        return render(request,"announceprgm.html",{'ff':f1})

def announceprgm1(request):
    if request.method == 'POST':
        data = awarenessprgm()
        data.Awareness_id   = request.POST.get('Awareness_id')
        data.prg_name = request.POST.get('prg_name')
        data.description = request.POST.get('description')
        data.conducted_by = request.POST.get('conducted_by')
        data.venue = request.POST.get('venue')
        data.date = request.POST.get('date')
        data.time = request.POST.get('time')
        data.status = "active"
        data.save()
        s=request.session['AWRN_ID']
        data2=idgen1.objects.get(id=1)
        data2.Awarenessprgm_id =s
        data2.save()
        return redirect ('/announceprgm')
        

def publicheader(request):
    return render(request,"publicheader1.html")


def view_rules(request):
    items = rule.objects.all()
    return render(request,"view_rules.html",{'it':items})

def view_awarnsprg(request):
    items = awarenessprgm.objects.all()
    return render(request,"view_awarnsprg.html",{'it':items})

def victim_register(request):  
    data = idgen1.objects.get(id=1)
    f=data.Victim_id 
    f=f+1
    f1="VICT"+str(f)
    request.session['VIC_ID']=f  
    return render(request,"victim_register.html",{'ff':f1})

def victim_register1(request):
    if request.method == 'POST':
        data = victim()
        data.Victim_id = request.POST.get('Victim_id')
        data.name = request.POST.get('name')
        data.age = request.POST.get('age')
        data.sex = request.POST.get('sex')
        data.address = request.POST.get('address')
        data.contact = request.POST.get('contact')
        data.email = request.POST.get('email')
        data.key="key"
        data.save() 
        data1=victim1a()
        key=Fernet.generate_key()
        message=data.name
        
        encoded_message=message.encode()
        f=Fernet(key)
        encrypted_message=f.encrypt(encoded_message)
        data1.Victim_id=data.Victim_id
        data1.name=data.name
        data1.sname=encrypted_message
        data1.skey=key
        data1.save()
        s=request.session['VIC_ID']
        data2=idgen1.objects.get(id=1)
        data2.Victim_id =s
        data2.save()
        data3=tbl_login()
        data3.username=request.POST.get('Victim_id')
        data3.password=request.POST.get('contact')
        data3.category="victim"
        data3.save()
        send_mail('HELPING HANDS','username'+request.POST.get('Victim_id')+'password'+request.POST.get('contact'),'from@example.co',[request.POST.get('email'),])
        return redirect('/victim_register')

def login(request):
    return render(request,"login.html")


def register_awarns1(request,id):
    data = idgen1.objects.get(id=1)
    f=data.Participant_id
    f=f+1
    f1="PRTCP"+str(f)
    request.session['PRTI_ID']=f  
    return render(request,"register_awarns.html",{'it': id,'ff':f1})

def register_awarns2(request):
    if request.method == 'POST':
        data=participants()
        data.Participant_id  = request.POST.get('Participant_id')
        data.awarenessprgm_id = request.POST.get('Awarenessprgm_id')
        data.participant_name  = request.POST.get('participant_name')
        data.address = request.POST.get('address')
        data.age = request.POST.get('age')
        data.sex = request.POST.get('sex')
        data.contact = request.POST.get('contact')
        data.email = request.POST.get('email')
        data.status = "active"
        data.save()
        s=request.session['PRTI_ID']
        data2=idgen1.objects.get(id=1)
        data2. Participant_id =s
        data2.save()
        send_mail('HELPING HANDS','SUCCESSFULLY REGISTERD','from@example.co',[request.POST.get('email'),])
        return redirect('/view_awarnsprg')

def view_participant(request):
    items = awarenessprgm.objects.all()
    return render(request,"view_participant.html",{'it':items})


def view_participant1(request,id):
    data = participants.objects.filter(awarenessprgm_id=id)
    return render(request,"view_participant1.html",{'it':data})
       
        

def update_status(request):
    items = awarenessprgm.objects.all()
    return render(request,"update_status.html",{'it':items})

def update_status1(request,id):
    data=awarenessprgm.objects.get(Awareness_id=id)
    s = data.status
    if s=="active":
        data.status="pending"
        data.save()
    else:
        data.status="active"
        data.save()
    return redirect('/update_status')


def victimheader(request):
    return render(request,"victimheader.html")


def view_awarnsprgm(request):
    items = awarenessprgm.objects.all()
    return render(request,"view_awarnsprgm.html",{'it':items})

def register_awarnsvict1(request,id):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else: 
        data = idgen1.objects.get(id=1)
        f=data.Participant_id
        f=f+1
        f1="PRTCP"+str(f)
        request.session['PRTI_ID']=f
        uid=request.session['uid'] 
        data2=victim.objects.get(Victim_id=uid) 
        return render(request,"register_awarnsvict.html",{'it': id,'ff':f1,'data2':data2})

def register_awarnsvict2(request):
    if request.method == 'POST':
        data=participants()
        data.Participant_id  = request.POST.get('Participant_id')
        data.awarenessprgm_id = request.POST.get('Awarenessprgm_id')
        data.participant_name  = request.POST.get('participant_name')
        data.address = request.POST.get('address')
        data.age = request.POST.get('age')
        data.sex = request.POST.get('sex')
        data.contact = request.POST.get('contact')
        data.email = request.POST.get('email')
        data.status = "active"
        data.save()
        s=request.session['PRTI_ID']
        data2=idgen1.objects.get(id=1)
        data2. Participant_id =s
        data2.save()
        send_mail('HELPING HANDS','SUCCESSFULLY REGISTERD','from@example.co',[request.POST.get('email'),])
        return redirect('/view_awarnsprgm')
        
def view_rule(request):
    items = rule.objects.all()
    return render(request,"view_rule.html",{'it':items})

def gen_comp(request): 
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else:  
        data = idgen1.objects.get(id=1)
        f=data.Complaint_id
        f=f+1
        f1="COMP"+str(f)
        request.session['COM_ID']=f 
        vid=request.session['uid'] 
        return render(request,"gen_comp.html",{'ff':f1,'vid':vid})

def gen_comp1(request):
    if request.method == 'POST':
        data = complaint()
        data.Complaint_id  = request.POST.get('Complaint_id')
        data.Victim_id = request.POST.get('Victim_id')
        data.complaint = request.POST.get('complaint')
        data.complaint_date = request.POST.get('complaint_date')
        data.remark = request.POST.get('remark')
        data.action = ""
        data.status = "pending"
        data.save()
        s=request.session['COM_ID']
        data2=idgen1.objects.get(id=1)
        data2.Complaint_id =s
        data2.save()
        return redirect ('/gen_comp')
        
def admin1(request):
    return render(request,"admin.html")

def supporter1(request):
    return render(request,"supporter.html")

def womencell1(request):
    return render(request,"womencell.html")

def childwelfare1(request):
    return render(request,"childwelfare.html")

def police1(request):
    return render(request,"police.html")

def victim1(request):
    return render(request,"victim.html")

def logins(request):
    return render(request,"logins.html")

def logins1(request):
    if request.method == 'POST':
        data = tbl_login.objects.all()
        Username=request.POST.get('username')
        Password=request.POST.get('password')
        flag=0
        for da in data:
            if  Username==da.username and Password==da.password:
                type=da.category
                flag=1
                request.session['uid']=Username
                if type=="admin":
                    return redirect('/admin1')
                elif type=="supporter":
                    return redirect('/supporter1')
                elif type=="womencell":
                    return redirect('/womencell1')
                elif type=="childwelfare":
                    return redirect('/childwelfare1')
                elif type=="police":
                    return redirect('/police1')    
                elif type=="victim":
                    return redirect('/victim1')

                else:
                    return HttpResponse("invalid acct type")
        if flag==0:
            return HttpResponse("User doesn't exist")     

def verify_comp(request):
    items = complaint.objects.filter(status="pending")
    return render(request,"verify_comp.html",{'it':items})

def take_action1(request,id):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else: 
        data = idgen1.objects.get(id=1)
        f=data.Action_id 
        f=f+1
        f1="ACT"+str(f)
        request.session['AC_ID']=f  
        sid=request.session['uid']
        return render(request,"takeaction.html",{'it': id,'ff':f1,'sid':sid})

def take_action2(request):
    if request.method == 'POST':
        data=tblcomp_action()
        data.Action_id = request.POST.get('Action_id')
        data.Complaint_id = request.POST.get('Complaint_id')
        data.action = request.POST.get('action')
        data.takenby = request.POST.get('takenby')
        data.remark = request.POST.get('remark')
        data.redirectto = request.POST.get('redirectto')
        now=datetime.datetime.now()
        data.action_date=now.strftime("%Y-%m-%d")  
        data.status="pending"    
        data.save()
        s=request.session['AC_ID']
        data2=idgen1.objects.get(id=1)
        data2.Action_id =s
        data2.save()
        data3=complaint.objects.get(Complaint_id=request.POST.get('Complaint_id'))
        data3.status="passed"
        data3.save()
        return redirect('/verify_comp')      



def redirect_womencell(request):
    items = tblcomp_action.objects.filter(redirectto="womencell").filter(status="pending")
    return render(request,"redirect_womencell.html",{'it':items})

def redirect_women1(request,id):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else: 
        data = idgen1.objects.get(id=1)
        f=data.Womencell_id 
        f=f+1
        f1="WMNC"+str(f)
        request.session['WM_ID']=f  
        data=tblcomp_action.objects.get(Action_id=id)
        mid=data.Complaint_id
        return render(request,"redirect_women.html",{'it': id,'ff':f1,'mid':mid})

def redirect_women2(request):
    if request.method == 'POST':
        data=tbl_womencell()
        data.Womencell_id = request.POST.get('Womencell_id')
        data.Action_id  = request.POST.get('Action_id')
        data.Complaint_id = request.POST.get('Complaint_id')
        data.findings = request.POST.get('findings')
        now=datetime.datetime.now()
        data.redirect_date=now.strftime("%Y-%m-%d")      
        data.action = ""
        data.status = "pending"    
        data.save()
        s=request.session['WM_ID']
        data2=idgen1.objects.get(id=1)
        data2.Womencell_id =s
        data2.save()
        data3=tblcomp_action.objects.get(Complaint_id=request.POST.get('Complaint_id'))
        data3.status="redirect"
        data3.save()
        return redirect('/redirect_womencell')                      


def redirect_childwelfare(request):
    items = tblcomp_action.objects.filter(redirectto="childwelfare").filter(status="pending")
    return render(request,"redirect_childwelfare.html",{'it':items})
    

def redirect_childwel1(request,id):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else: 
        data = idgen1.objects.get(id=1)
        f=data.Child_id
        f=f+1
        f1="CHLD"+str(f)
        request.session['CH_ID']=f  
        return render(request,"redirect_childwel.html",{'it': id,'ff':f1})

def redirect_childwel2(request):
    if request.method == 'POST':
        data=tbl_child()
        data.Child_id  = request.POST.get('Child_id')
        data.Complaint_id = request.POST.get('Complaint_id')
        data.findings  = request.POST.get('findings')
        now=datetime.datetime.now()
        data.redirect_date=now.strftime("%Y-%m-%d") 
        data.action = ""
        data.status = "pending"   
        data.save()
        s=request.session['CH_ID']
        data2=idgen1.objects.get(id=1)
        data2.Child_id=s
        data2.save()
        data3=tblcomp_action.objects.get(Complaint_id=request.POST.get('Complaint_id'))
        data3.status="redirect"
        data3.save()
        return redirect('/redirect_childwelfare')   

def redirect_to_police(request):
    items = tblcomp_action.objects.filter(redirectto="police").filter(status="pending")
    return render(request,"redirect_to_police.html",{'it':items}) 

def redirect_poli1(request,id):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else: 
        data = idgen1.objects.get(id=1)
        f=data.Policecomp_id 
        f=f+1
        f1="POLI"+str(f)
        request.session['PL_ID']=f  
        return render(request,"redirect_poli.html",{'it': id,'ff':f1})

def redirect_poli2(request):
    if request.method == 'POST':
        data=tblpolice_comp()
        data.Policecomp_id  = request.POST.get('Policecomp_id')
        data.Complaint_id = request.POST.get('Complaint_id')
        data.findings  = request.POST.get('findings')
        now=datetime.datetime.now()
        data.redirect_date=now.strftime("%Y-%m-%d") 
        data.action = ""
        data.status = "pending"   
        data.save()
        s=request.session['PL_ID']
        data2=idgen1.objects.get(id=1)
        data2.Policecomp_id =s
        data2.save()
        data3=tblcomp_action.objects.get(Complaint_id=request.POST.get('Complaint_id'))
        data3.status="redirect"
        data3.save()
        return redirect('/redirect_to_police')    

def chat_victim(request):
    items = victim.objects.all()
    return render(request,"chat_victim.html",{'it':items})

def chat_vict1(request,id):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else: 
        data = idgen1.objects.get(id=1)
        f=data.Chat_id
        f=f+1
        f1="CHT"+str(f)
        request.session['CH_ID']=f  
        aid=request.session['uid']
        return render(request,"chat_vict.html",{'it': id,'ff':f1,'aid':aid})

def chat_vict2(request):
    if request.method == 'POST':
        data=tbl_chat()
        data.Chat_id  = request.POST.get('Chat_id')
        data.Victim_id = request.POST.get('Victim_id')
        data.Authority_id = request.POST.get('Authority_id')
        data.chat  = request.POST.get('chat')
        now=datetime.datetime.now()
        data.date=now.strftime("%Y-%m-%d")   
        data.time = request.POST.get('time')
        data.response = "" 
        data.status="pending"   
        data.save()
        s=request.session['CH_ID']
        data2=idgen1.objects.get(id=1)
        data2.Chat_id=s
        data2.save()
        return redirect('/chat_victim')  

def chat_box(request):
    vid=request.session['uid']
    items = tbl_chat.objects.filter(Victim_id=vid).filter(status="pending")
    return render(request,"chat_box.html",{'it':items})

def give_response1(request,id):   
    return render(request,"give_response.html",{'cid':id})

def give_response2(request,id):
    data=tbl_chat.objects.get(Chat_id=id)
    if request.method=='POST':
        data.response =request.POST.get('response')
        data.status="completed"   
        data.save()
        return redirect('/chat_box')  

def chat_victchild(request):
    items = tblcomp_action.objects.filter(redirectto='childwelfare')
    return render(request,"chat_victchild.html",{'it':items})

def chat_victchi1(request,id):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else: 
        data = idgen1.objects.get(id=1)
        f=data.Chat_id
        f=f+1
        f1="CHT"+str(f)
        request.session['CH_ID']=f  
        aid=request.session['uid']
        return render(request,"chat_victchi.html",{'it': id,'ff':f1,'aid':aid})

def chat_victchi2(request):
    if request.method == 'POST':
        data=tbl_chat()
        data.Chat_id  = request.POST.get('Chat_id')
        data.Victim_id = request.POST.get('Victim_id')
        data.Authority_id = request.POST.get('Authority_id')
        data.chat  = request.POST.get('chat')
        now=datetime.datetime.now()
        data.date=now.strftime("%Y-%m-%d")   
        data.time = request.POST.get('time')
        data.response = "" 
        data.status="pending"   
        data.save()
        s=request.session['CH_ID']
        data2=idgen1.objects.get(id=1)
        data2.Chat_id=s
        data2.save()
        return redirect('/chat_victchild')  


def view_resposup(request):
    sid=request.session['uid']
    items = tbl_chat.objects.filter(status="completed").filter(Authority_id=sid)
    return render(request,"view_resposup.html",{'it':items})
   
def view_respchi(request):
    sid=request.session['uid']
    items = tbl_chat.objects.filter(status="completed").filter(Authority_id=sid)
    return render(request,"view_respchi.html",{'it':items})

def view_comp(request):
    items = tbl_child.objects.filter(status="pending")
    return render(request,"view_comp.html",{'it':items})

def view_compchi1(request,id):
    items = complaint.objects.get(Complaint_id=id)
    return render(request,"view_compchi.html",{'items':items})

def view_compchi2(request,id):   
    data1=tbl_child.objects.get(Complaint_id=request.POST.get('Complaint_id'))
    data1.action=request.POST.get('action')
    data1.status="completed"
    data1.save()
    data2=complaint.objects.get(Complaint_id=request.POST.get('Complaint_id'))
    data2.action=request.POST.get('action')
    data2.status="completed"
    data2.handle_by=request.POST.get('handle_by')
    uid=request.session['uid']
    data3=tbl_login.objects.get(username=uid)
    category=data3.category
    data2.handle_by=category
    data2.save()
    return redirect('/view_comp')  

def view_complnt(request):
    items = tblpolice_comp.objects.filter(status="pending")
    return render(request,"view_complnt.html",{'it':items})

def view_complntpo1(request,id):
    items = complaint.objects.get(Complaint_id=id)
    return render(request,"view_complntpo.html",{'items':items})

def view_complntpo2(request,id):   
    data1=tblpolice_comp.objects.get(Complaint_id=request.POST.get('Complaint_id'))
    data1.action=request.POST.get('action')
    data1.status="completed"
    data1.save()
    data2=complaint.objects.get(Complaint_id=request.POST.get('Complaint_id'))
    data2.action=request.POST.get('action')
    data2.status="completed"
    data2.handle_by=request.POST.get('handle_by')
    uid=request.session['uid']
    data3=tbl_login.objects.get(username=uid)
    category=data3.category
    data2.handle_by=category
    data2.save()
    return redirect('/view_complnt')  

def view_complaint(request):
    items = tbl_womencell.objects.filter(status="pending")
    return render(request,"view_complaint.html",{'it':items})

def view_compwmn1(request,id):
    items = complaint.objects.get(Complaint_id=id)
    return render(request,"view_compwmn.html",{'items':items})

def view_compwmn2(request,id):   
    data1=tbl_womencell.objects.get(Complaint_id=request.POST.get('Complaint_id'))
    data1.action=request.POST.get('action')
    data1.status="completed"
    data1.save()
    data2=complaint.objects.get(Complaint_id=request.POST.get('Complaint_id'))
    data2.action=request.POST.get('action')
    data2.status="completed"
    data2.save()
    return redirect('/view_complaint')  

def chat_victwmn(request):
    items = tblcomp_action.objects.filter(redirectto='womencell')
    return render(request,"chat_victwmn.html",{'it':items})

def chat_victwmen1(request,id):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else: 
        data = idgen1.objects.get(id=1)
        f=data.Chat_id
        f=f+1
        f1="CHT"+str(f)
        request.session['CH_ID']=f  
        aid=request.session['uid']
        return render(request,"chat_victwmen.html",{'it': id,'ff':f1,'aid':aid})

def chat_victwmen2(request):
    if request.method == 'POST':
        data=tbl_chat()
        data.Chat_id  = request.POST.get('Chat_id')
        data.Victim_id = request.POST.get('Victim_id')
        data.Authority_id = request.POST.get('Authority_id')
        data.chat  = request.POST.get('chat')
        now=datetime.datetime.now()
        data.date=now.strftime("%Y-%m-%d")   
        data.time = request.POST.get('time')
        data.response = "" 
        data.status="pending"   
        data.save()
        s=request.session['CH_ID']
        data2=idgen1.objects.get(id=1)
        data2.Chat_id=s
        data2.save()
        return redirect('/chat_victwmn')  

def view_respwmn(request):
    sid=request.session['uid']
    items = tbl_chat.objects.filter(status="completed").filter(Authority_id=sid)
    return render(request,"view_respwmn.html",{'it':items})

def view_action(request):
    vid=request.session['uid']
    items =complaint.objects.filter(status="completed").filter(Victim_id=vid)
    return render(request,"view_action.html",{'it':items})

def view_compwmact1(request,id):
    items = complaint.objects.get(Complaint_id=id)
    return render(request,"view_compwmact.html",{'items':items})

def view_compwmact2(request):   
    data1=tbl_womencell.objects.get(Complaint_id=request.POST.get('Complaint_id'))
    data1.action=request.POST.get('action')
    data1.status="completed"
    data1.save()
    data2=complaint.objects.get(Complaint_id=request.POST.get('Complaint_id'))
    data2.action=request.POST.get('action')
    data2.handle_by=request.POST.get('handle_by')
    uid=request.session['uid']
    data3=tbl_login.objects.get(username=uid)
    category=data3.category
    data2.handle_by=category
    data2.status="completed"
    data2.save()
    return redirect('/view_complaint')  

def redirect_poliwm1(request,id):
    if 'uid' not in request.session:
        return render(request,"logins.html")
    else: 
        data=idgen1.objects.get(id=1)
        f=data.Policecomp_id
        f=f+1
        f1="POCM"+str(f)
        request.session['PC_ID']=f  
        return render(request,"redirect_poliwm.html",{'items':id,'ff':f1})

def redirect_poliwm2(request):
    if request.method == 'POST':
        data=tblpolice_comp()
        data.Policecomp_id=request.POST.get('Policecomp_id')
        data.Complaint_id=request.POST.get('Complaint_id')
        data.findings=request.POST.get('findings')
        now=datetime.datetime.now()
        data.date=now.strftime("%Y-%m-%d")   
        data.status="pending"   
        data.save()
        s=request.session['PC_ID']
        data2=idgen1.objects.get(id=1)
        data2.Policecomp_id=s
        data2.save()
        return redirect('/view_complaint')  

def complaint1(request):
    items = complaint.objects.filter(status="completed")
    return render(request,"complaint1.html",{'it':items})

def awareness_program(request):
    items = awarenessprgm.objects.all()
    return render(request,"awareness_program.html",{'it':items})

def logout(request):
    del request.session['uid']
    return render(request,"logins.html")

def index(request):
    return render(request,"index.html")

def view_complaintschat1(request,id):
    items = complaint.objects.get(Complaint_id=id)
    return render(request,"view_complaintschat.html",{'items':items})

def view_complaintschat2(request): 
    data = idgen1.objects.get(id=1)
    f=data.Chat_id
    f=f+1
    f1="CHT"+str(f)
    request.session['CH_ID']=f  
    aid=request.session['uid']
    id= request.POST.get('Victim_id')
    return render(request,"chat_victwmen.html",{'it': id,'ff':f1,'aid':aid})
    
def view_complaintchichat1(request,id):
    items = complaint.objects.get(Complaint_id=id)
    return render(request,"view_complaintchichat.html",{'items':items})

def view_complaintchichat2(request): 
    data = idgen1.objects.get(id=1)
    f=data.Chat_id
    f=f+1
    f1="CHT"+str(f)
    request.session['CH_ID']=f  
    aid=request.session['uid']
    id= request.POST.get('Victim_id')
    return render(request,"chat_victchi.html",{'it': id,'ff':f1,'aid':aid})
    
 
def victim_details1(request,id):
    data = victim.objects.get(Victim_id=id)
    data1=victim1a.objects.get(Victim_id=data.Victim_id)
    f=Fernet(data1.skey)
    name=f.decrypt(data1.sname)
    sname=name.decode('utf-8')
    print(sname)
    print("my name")
    return render(request,"victim_details.html",{'it':data,'name':sname})

def helplineno(request):
    return render(request,"helplineno.html")

def typesofdomestic(request):
    return render(request,"typesofdomestic.html")

def victimdetailw1(request,id):
    data= complaint.objects.get(Complaint_id=id)
    vid=data.Victim_id
    data=victim.objects.get(Victim_id=vid)
    data1=victim1a.objects.get(Victim_id=data.Victim_id)
    f=Fernet(data1.skey)
    name=f.decrypt(data1.sname)
    sname=name.decode('utf-8')
    print(sname)
    print("my name")
    return render(request,"victim_detailw.html",{'it':data,'name':sname,'vid':vid})

def victimdetailc1(request,id):
    data= complaint.objects.get(Complaint_id=id)
    vid=data.Victim_id
    data=victim.objects.get(Victim_id=vid)
    data1=victim1a.objects.get(Victim_id=data.Victim_id)
    f=Fernet(data1.skey)
    name=f.decrypt(data1.sname)
    sname=name.decode('utf-8')
    print(sname)
    print("my name")
    return render(request,"victim_detailc.html",{'it':data,'name':sname,'vid':vid})

def victimdetailp1(request,id):
    data= complaint.objects.get(Complaint_id=id)
    vid=data.Victim_id
    data=victim.objects.get(Victim_id=vid)
    data1=victim1a.objects.get(Victim_id=data.Victim_id)
    f=Fernet(data1.skey)
    name=f.decrypt(data1.sname)
    sname=name.decode('utf-8')
    print(sname)
    print("my name")
    return render(request,"victim_detailp.html",{'it':data,'name':sname,'vid':vid})





    

