from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from evoterid.models import Suggestion#import pymysql
from evoterid.models import User
from evoterid.models import modification
from django.template.context_processors import csrf
from django.template import RequestContext
from django.views import generic# Create your views here.

class UserListView(generic.ListView):
	model = User

class modificationListView(generic.ListView):
	model = modification

def getuserinfo(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('index.html', c)

def deluserinfo(request):
	uid = request.session.get('id')
	user = User.objects.filter(id = uid)
	for u in user:
		u.delete()
	return render_to_response('delrecord.html')

def adduserinfo(request):
    ustate = request.POST.get('state', '')
    udistrict = request.POST.get('district', '')
    uassembly = request.POST.get('assembly', '')
    unm = request.POST.get('anm', '')
    uasurnm = request.POST.get('asurnm', '')
    uarnm = request.POST.get('arnm', '')
    uarsurnm = request.POST.get('arsurnm', '')
    urelation = request.POST.get('relation', '')
    udob = request.POST.get('dob', '')
    ugender = request.POST.get('gender', '')
    ushouseno = request.POST.get('hno', '')
    uaddress = request.POST.get('street', '')
    utown = request.POST.get('town', '')
    upin = request.POST.get('pin', '')
    uemail = request.POST.get('email', '')
    umo_number = request.POST.get('mno', '')
    uphoto = request.FILES['photo']
    uageproof = request.FILES['ageproof']
    utypeageproof = request.POST.get('typeageproof', '')
    uaddproof = request.FILES['addproof']
    utypeaddproof = request.POST.get('typeaddproof', '')
    uplace = request.POST.get('place', '')
    u = User(state = ustate,district = udistrict,assembly = uassembly,name = unm,srname = uasurnm,r_name = uarnm,r_srname = uarsurnm,relation = urelation,birthday = udob,gender = ugender,houseno = ushouseno,address = uaddress,town = utown,pin = upin,email_id = uemail,mo_number = umo_number,photo = uphoto,age_p = uageproof,typeageproof = utypeageproof,add_p = uaddproof,typeaddproof = utypeaddproof,place = uplace )
    u.save()

    return HttpResponseRedirect('/evoterid/addsuccess/')

def addsuccess(request):
	u=User.objects.all()
	for i in u:
		id=str(i.id)
		name=i.name
	print(id)
	print(name)
	context={
		'users':str(id),
		'name':name
	}


	return render(request,'addrecord.html',context=context)

def form6(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('form6.html',c)

def form8(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('form8.html',c)

def form7(request):
	return render_to_response('form7.html')

def search(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('search.html',c)

def treak(request):
	return render_to_response('treak.html')

def verify(request):
	return render_to_response('verify.html')

def admin(request):
	return render_to_response('admin.html')

def about(request):
	return render_to_response('about.html')

def contact(request):
	return render_to_response('contact.html')

def soon(request):
	return render_to_response('soon.html')

def sugcom(request):
	return render_to_response('sugcom.html')

def addmodificationinfo(request):
	ustate = request.POST.get('state', '')
	udistrict = request.POST.get('district', '')
	uassembly = request.POST.get('assembly', '')
	uoldnm = request.POST.get('oldname', '')
	uoldsrnm = request.POST.get('oldsrnmae', '')
	uvoterid = request.POST.get('vidno', '')
	unm = request.POST.get('anm', '')
	uasurnm = request.POST.get('asurnm', '')
	uarnm = request.POST.get('arnm', '')
	uarsurnm = request.POST.get('arsurnm', '')
	urelation = request.POST.get('relation', '')
	udob = request.POST.get('dob', '')
	ugender = request.POST.get('gender', '')
	ushouseno = request.POST.get('hno', '')
	uaddress = request.POST.get('street', '')
	utown = request.POST.get('town', '')
	upin = request.POST.get('pin', '')
	uemail = request.POST.get('email', '')
	umo_number = request.POST.get('mno', '')
	uphoto = request.FILES['photo']
	uageproof = request.FILES['ageproof']
	utypeageproof = request.POST.get('typeageproof', '')
	uaddproof = request.FILES['addproof']
	utypeaddproof = request.POST.get('typeaddproof', '')
	uplace = request.POST.get('place', '')
	u = modification(state = ustate,district = udistrict,assembly = uassembly,oldname = uoldnm,oldsrname = uoldsrnm,voterid = uvoterid,name = unm,srname = uasurnm,r_name = uarnm,r_srname = uarsurnm,relation = urelation,birthday = udob,gender = ugender,houseno = ushouseno,address = uaddress,town = utown,pin = upin,email_id = uemail,mo_number = umo_number,photo = uphoto,age_p = uageproof,typeageproof = utypeageproof,add_p = uaddproof,typeaddproof = utypeaddproof,place = uplace )
	u.save()
	return HttpResponseRedirect('/evoterid/addsuccess/')

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	targate = request.POST.get('blo', '')
	print(username)
	print(password)
	print(targate)
	user = auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request, user)
		if targate=="verification":
			return HttpResponseRedirect('/evoterid/loggedin/',RequestContext(request))
		else:
			return HttpResponseRedirect('/evoterid/modification/',RequestContext(request))
	else:
		return HttpResponseRedirect('/evoterid/invalidlogin/',RequestContext(request))

def loggedin(request):
    return HttpResponseRedirect('/evoterid/users/',RequestContext(request))
def invalidlogin(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('verify.html',c)
def logout(request):
    auth.logout(request)
    return render_to_response('index.html')
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('verify.html', c)

def getsearchname(request):
	c = {}
	c.update(csrf(request))
	return render(request,'search.html', c)


def searchresult(request):
	uid=request.POST.get("search")
	u=User.objects.filter(id=uid)
	if u is None:
		context={
			'users':None,
			}
	else:
		users=User.objects.all()
		context={
			'users':u,
			}

	return render(request,'searchresult.html',context=context)


def suggestion(request):
	username = request.POST.get('unm', '')
	password = request.POST.get('pass', '')
	print(username)
	print(password)
	user = auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/evoterid/loggedin1/',RequestContext(request))
	else:
		return HttpResponseRedirect('/evoterid/invalidlogin1/',RequestContext(request))

def loggedin1(request):
    return HttpResponseRedirect('/evoterid/feedback/',RequestContext(request))

def invalidlogin1(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('sugcom.html',c)

def login1(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('sugcom.html', c)

def feedback(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('feedback.html',c)

def addsugcom(request):
	uname = request.POST.get('name', '')
	sugcom = request.POST.get('suggestion', '')
	u = Suggestion(name = uname,suggestion = sugcom )
	u.save()
	return HttpResponseRedirect('/evoterid/addsuccess/')

def verification(request):
	uid = request.session.get('id')
	User.objects.filter(id = uid).update(status = "verify")
	return HttpResponseRedirect('/evoterid/addsuccess/')

def update(request):
	uid = request.session['id']
	print(uid)
	M=modification.objects.get(voterid = uid)
	print(M)
	print(M.voterid)
	User.objects.filter (id = M.voterid).update(state = M.state,district = M.district,assembly = M.assembly,name = M.name,srname = M.srname,r_name = M.r_name,r_srname = M.r_srname,relation = M.relation,birthday = M.birthday,gender = M.gender,houseno = M.houseno,address = M.address,town = M.town,pin = M.pin,email_id = M.email_id,mo_number = M.mo_number,photo = M.photo,age_p = M.age_p,typeageproof = M.typeageproof,add_p = M.add_p,typeaddproof = M.typeaddproof,place = M.place )
	M.delete()
	return HttpResponseRedirect('/evoterid/addsuccess/')

def view(request):
	uid=request.POST.get("id")
	request.session['id'] = uid
	u=User.objects.filter(id=uid)
	if u is None:
		context={
			'users':None,
			}
	else:
		users=User.objects.all()
		context={
			'users':u,
			}

	return render(request,'view.html',context=context)

def updateview(request):
	uid=request.POST.get("id")
	request.session['id'] = uid
	print(uid)
	u=User.objects.filter(id=uid)
	print(u)
	M=modification.objects.filter(voterid=uid)
	print(M)
	if u is None:
		context={
			'users':None,
			}
	else:
		context={
			'users':u,
			'modification':M,
			}
	return render(request,'updateview.html',context=context)
