from django.shortcuts import render
from disaster.models import main,login,givealert
from django.http import  HttpResponse
from django.http import Http404			

def index(request):
	Template_get="index.html"
	if request.method=='GET':
		govtalert={'alert':givealert.objects.last()}
		return render(request,Template_get,govtalert)
	if request.method=='POST':
		govtalert={'alert':givealert.objects.last()}
		return render(request,Template_get,govtalert)		
	
def index_post(request):
	Template_post="output.html"	
	if request.method=='POST':
		try:
			num=request.POST.get('input',None)
			selected=main.objects.get(yourlocation=num)	
			context={'data':selected}
		except main.DoesNotExist:
			raise Http404("entered location does not existed")
		return render(request,Template_post,context)

def govt_page(request):	
	Template_alert="alert.html"
	Template="login.html"
	Template_admin="admin.html"
	if request.method == 'GET':
		return render(request,Template)

	if request.method == 'POST':
		user = request.POST.get('user',False)
		pas = request.POST.get('passkey',False)				
		if login.objects.filter(username=user).exists() and login.objects.filter(password=pas).exists():
			context = {'username':user}
			return render(request,Template_admin,context)
		else:
			context={'error':"username or password is wrong"}
			return render(request,Template,context)

def delete(request):
	Template="deldata.html"
	if request.method == 'GET':
		return render(request,Template)

	if request.method == 'POST':
		user = request.POST.get('delsafeplace',False)
		if main.objects.filter(yourlocation=user).exists():
			delete = main.objects.filter(yourlocation=user).delete()
			context={'delete':"your entered location is deleted"}
			return render(request,Template,context)
		else:
			context={'delete':"entered location is not exist"}
			return render(request,Template,context)

def forgot(request):
	Template="forgotpswd.html"
	if request.method == 'GET':
		return render(request,Template)

	if request.method == 'POST':
		username = request.POST.get('username',False)
		schoolans = request.POST.get('school',False)
		user = login.objects.get(username=username)
		ans = login.objects.get(answer=schoolans)
		if user and ans:
			context={'user':login.objects.get(username=username)}
			return render(request,Template,context)

def adddata(request):
	if request.method =="GET":
		Template_alert ="enter data.html"
		return render(request,Template_alert)

	if request.method == "POST":
		Template_data="enter data.html"
		
		safeplaces1 = request.POST.get('safeplace1')
		safeplaces2 = request.POST.get('safeplace2')
		safeplaces3 = request.POST.get('safeplace3')
		safeplaces4 = request.POST.get('safeplace4')
		safeplaces5 = request.POST.get('safeplace5')
		
		transports1 = request.POST.get('transport1')
		transports2 = request.POST.get('transport2')
		transports3 = request.POST.get('transport3')
		
		rescue1 = request.POST.get('rescue1')
		rescue2 = request.POST.get('rescue2')	
		rescue3 = request.POST.get('rescue3')

		if main.objects.filter(yourlocation=safeplaces1).exists():
			context={'error':"entered location is all ready exist"}
			return render(request,Template_data,context)
		else:
			post=main(yourlocation=safeplaces1,
			      safeplacesname=safeplaces2,
			      safeplacesdistance=safeplaces3,
			      safeplacescapacity=safeplaces4,
			      safeplacescontact=safeplaces5,
			      transportname=transports1,
			      transporttypeof=transports2,
			      transportcontact=transports3,
			      rescueteammembers=rescue2,
			      rescuecontact=rescue3,
			      rescueteamtype=rescue1,
			      )
			post.save()
			return render(request,Template_data)

def govtadmin(request):
	
	Template_addgovt="add govt.html"
	return render(request,Template_addgovt)


def alert(request):
	Template_admin="alert.html"
	if request.method=="GET":
		return render(request,Template_admin)
	if request.method=="POST":
		alert = request.POST.get('alert_','True')
		instance = givealert.objects.create(alertinfo=alert)
		return render(request,Template_admin)

		
