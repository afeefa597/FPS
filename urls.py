"""Helpinghands URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('adminheader/',views.adminheader),
    path('addaccount/',views.addaccount),
    path('addaccount1/',views.addaccount1), 
    path('remove_acct/',views.remove_acct),
    path('remove_acct1/<int:id>',views.remove_acct1),
    path('addviolation/',views.addviolation),
    path('addviolation1/',views.addviolation1), 
    path('remove_violation/',views.remove_violation),
    path('remove_violation1/<int:id>',views.remove_violation1),
    path('announceprgm/',views.announceprgm),
    path('announceprgm1/',views.announceprgm1), 
    path('publicheader/',views.publicheader),
    path('view_rules/',views.view_rules),
    path('view_awarnsprg/',views.view_awarnsprg),
    path('victim_register/',views.victim_register),
    path('victim_register1/',views.victim_register1), 
    path('tbl_login/',views.tbl_login),
    path('register_awarns1/<str:id>',views.register_awarns1),
    path('register_awarns2/',views.register_awarns2),
    path('view_participant/',views.view_participant),
    path('view_participant1/<str:id>',views.view_participant1),
    path('update_status/',views.update_status),
    path('update_status1/<str:id>',views.update_status1),
    path('victimheader/',views.victimheader),
    path('view_awarnsprgm/',views.view_awarnsprgm),
    path('register_awarnsvict1/<str:id>',views.register_awarnsvict1),
    path('register_awarnsvict2/',views.register_awarnsvict2),
    path('view_rule/',views.view_rule),
    path('gen_comp/',views.gen_comp),
    path('gen_comp1/',views.gen_comp1), 
    path('admin1/',views.admin1),
    path('supporter1/',views.supporter1),
    path('womencell1/',views.womencell1),
    path('childwelfare1/',views.childwelfare1),
    path('police1/',views.police1),
    path('victim1/',views.victim1),
    path('logins/',views.logins),                        
    path('logins1/',views.logins1),
    path('verify_comp/',views.verify_comp),
    path('take_action1/<str:id>',views.take_action1),
    path('take_action2/',views.take_action2),
    path('redirect_womencell/',views.redirect_womencell),
    path('redirect_women1/<str:id>',views.redirect_women1),
    path('redirect_women2/',views.redirect_women2),
    path('redirect_childwelfare/',views.redirect_childwelfare),
    path('redirect_childwel1/<str:id>',views.redirect_childwel1),
    path('redirect_childwel2/',views.redirect_childwel2),
    path('redirect_to_police/',views.redirect_to_police),  
    path('redirect_poli1/<str:id>',views.redirect_poli1),
    path('redirect_poli2/',views.redirect_poli2),
    path('chat_victim/',views.chat_victim),
    path('chat_vict1/<str:id>',views.chat_vict1),
    path('chat_vict2/',views.chat_vict2),
    path('chat_box/',views.chat_box),
    path('give_response1/<str:id>',views.give_response1),
    path('give_response2/<str:id>',views.give_response2),
    path('chat_victchild/',views.chat_victchild),
    path('chat_victchi1/<str:id>',views.chat_victchi1),
    path('chat_victchi2/',views.chat_victchi2),
    path('view_resposup/',views.view_resposup),
    path('view_respchi/',views.view_respchi),
    path('view_comp/',views.view_comp),
    path('view_compchi1/<str:id>',views.view_compchi1),
    path('view_compchi2/<str:id>',views.view_compchi2),
    path('view_complnt/',views.view_complnt),
    path('view_complntpo1/<str:id>',views.view_complntpo1),
    path('view_complntpo2/<str:id>',views.view_complntpo2),
    path('view_complaint/',views.view_complaint),
    path('view_compwmn1/<str:id>',views.view_compwmn1),
    path('view_compwmn2/<str:id>',views.view_compwmn2),
    path('chat_victwmn/',views.chat_victwmn),
    path('chat_victwmen1/<str:id>',views.chat_victwmen1),
    path('chat_victwmen2/',views.chat_victwmen2),
    path('view_respwmn/',views.view_respwmn),
    path('view_action/',views.view_action),
    path('view_compwmact1/<str:id>',views.view_compwmact1),
    path('view_compwmact2/',views.view_compwmact2),
    path('redirect_poliwm1/<str:id>',views.redirect_poliwm1),
    path('redirect_poliwm2/',views.redirect_poliwm2),
    path('complaint1/',views.complaint1),
    path('awareness_program/',views.awareness_program),
    path('index/',views.index),
    path('logout/',views.logout),
    path('view_complaintschat1/<str:id>',views.view_complaintschat1),
    path('view_complaintschat2/',views.view_complaintschat2),
    path('view_complaintchichat1/<str:id>',views.view_complaintchichat1),
    path('view_complaintchichat2/',views.view_complaintchichat2),
    path('victim_details1/<str:id>',views.victim_details1),
    path('helplineno/',views.helplineno),
    path('typesofdomestic/',views.typesofdomestic),
    path('victimdetailw1/<str:id>',views.victimdetailw1),
    path('victimdetailc1/<str:id>',views.victimdetailc1),
    path('victimdetailp1/<str:id>',views.victimdetailp1),
    
   
]