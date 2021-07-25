from django.db import models

# Create your models here.

class account(models.Model):
     Acct_id =models.CharField(max_length=90)
     role = models.CharField(max_length=90)
     contact_person = models.CharField(max_length=90)
     phone = models.CharField(max_length=90)
     email = models.CharField(max_length=90)
     address = models.CharField(max_length=90)
     status = models.CharField(max_length=90)

     class Meta:
          db_table = "account"

class rule(models.Model):
     Rule_id = models.CharField(max_length=90)
     violations = models.CharField(max_length=250)
     rules = models.CharField(max_length=250)
     punishments = models.CharField(max_length=250)
     
     class Meta:
          db_table = "rule"

class awarenessprgm(models.Model):
     Awareness_id = models.CharField(max_length=90)
     prg_name = models.CharField(max_length=90)
     description = models.CharField(max_length=250)
     conducted_by = models.CharField(max_length=90)
     venue = models.CharField(max_length=90)
     date= models.CharField(max_length=90)
     time = models.CharField(max_length=90)
     status = models.CharField(max_length=90)

     class Meta:
          db_table = "awarenessprgm"

class victim(models.Model):
     Victim_id =models.CharField(max_length=90)
     name = models.CharField(max_length=255)
     age = models.CharField(max_length=90)
     sex = models.CharField(max_length=90)
     address = models.CharField(max_length=90)
     contact = models.CharField(max_length=90)
     email = models.CharField(max_length=90)
     key = models.CharField(max_length=255)

     class Meta:
          db_table = "victim"


class tbl_login(models.Model):
     
     username = models.CharField(max_length=90)
     password = models.CharField(max_length=90)
     category = models.CharField(max_length=90)
     

     class Meta:
          db_table = "tbl_login"

class participants(models.Model):
     Participant_id = models.CharField(max_length=90)
     awarenessprgm_id = models.CharField(max_length=90)
     participant_name = models.CharField(max_length=90)
     address = models.CharField(max_length=90)
     age = models.CharField(max_length=10)
     sex = models.CharField(max_length=90)
     contact = models.CharField(max_length=90)
     email = models.CharField(max_length=90)
     status = models.CharField(max_length=90)


     class Meta:
          db_table = "participants"


class idgen1(models.Model):
     Acct_id =models.IntegerField()
     Rule_id=models.IntegerField()
     Awarenessprgm_id = models.IntegerField()
     Victim_id =models.IntegerField()
     Participant_id = models.IntegerField()
     Complaint_id = models.IntegerField()
     Action_id = models.IntegerField()
     Womencell_id = models.IntegerField()
     Child_id = models.IntegerField()
     Policecomp_id = models.IntegerField()
     Chat_id = models.IntegerField()

     class Meta:
          db_table = "idgen1"  


class complaint(models.Model):
     Complaint_id = models.CharField(max_length=90)
     Victim_id = models.CharField(max_length=90)
     complaint = models.CharField(max_length=90)
     complaint_date = models.CharField(max_length=90)
     remark = models.CharField(max_length=90)
     handle_by = models.CharField(max_length=90)
     action = models.CharField(max_length=90)
     status = models.CharField(max_length=90)

     class Meta:
          db_table = "complaint"


class tblcomp_action(models.Model):
     Action_id = models.CharField(max_length=90)
     Complaint_id =models.CharField(max_length=90)
     action = models.CharField(max_length=90)
     takenby= models.CharField(max_length=90)
     remark = models.CharField(max_length=10)
     redirectto = models.CharField(max_length=90)
     action_date = models.CharField(max_length=90)
     status = models.CharField(max_length=90)
     class Meta:
          db_table = "tblcomp_action"


class tbl_womencell(models.Model):
     Womencell_id = models.CharField(max_length=90)
     Action_id =models.CharField(max_length=90)
     Complaint_id = models.CharField(max_length=90)
     findings = models.CharField(max_length=90)
     redirect_date = models.CharField(max_length=90)
     action = models.CharField(max_length=90)
     status = models.CharField(max_length=90)

     class Meta:
          db_table = "tbl_womencell"


class tbl_child(models.Model):
     Child_id= models.CharField(max_length=90)
     Complaint_id =models.CharField(max_length=90)
     findings = models.CharField(max_length=90)
     redirect_date = models.CharField(max_length=90)
     action = models.CharField(max_length=90)
     status = models.CharField(max_length=90)

     class Meta:
          db_table = "tbl_child"


class tblpolice_comp(models.Model):
     Policecomp_id = models.CharField(max_length=90)
     Complaint_id =models.CharField(max_length=90)
     findings = models.CharField(max_length=90)
     redirect_date = models.CharField(max_length=90)
     action = models.CharField(max_length=90)
     status = models.CharField(max_length=90)

     class Meta:
          db_table = "tblpolice_comp"


class tbl_chat(models.Model):
     Chat_id = models.CharField(max_length=90)
     Victim_id =models.CharField(max_length=90)
     Authority_id = models.CharField(max_length=90)
     chat = models.CharField(max_length=90)
     date = models.CharField(max_length=90)
     time = models.CharField(max_length=90)
     response = models.CharField(max_length=90)
     status = models.CharField(max_length=90)

     class Meta:
          db_table = "tbl_chat"


class victim1a(models.Model):
    Victim_id =  models.CharField(max_length=30)
    name = models.CharField(max_length=225)
    sname = models.BinaryField()
    skey = models.BinaryField()
    class Meta:
        db_table = "victim1a"
