from django.shortcuts import render, redirect
from django.views import generic
from .models import Maghale, Professor, AboutUs, Student
from .forms import AddmaghaleForm
from django.http import HttpResponse


class MaghaleView(generic.ListView):
    template_name = 'APP1/home.html'
    context_object_name = 'maghalelist'

    def get_queryset(self):
        return Maghale.objects.raw('select * from APP1_maghale')


class MaghaleDetails(generic.DetailView):
    model = Maghale
    template_name = 'APP1/Details.html'


class About(generic.ListView):
    template_name = 'APP1/AboutUs.html'
    context_object_name = 'aboutUs'

    def get_queryset(self):
        return AboutUs.objects.raw('select * from APP1_aboutus')


def Addmaghale(request):
    if request.method == "POST":
        form = AddmaghaleForm(request.POST, request.FILES)
        if form.is_valid():
            name_s = form.cleaned_data['name_s']
            name_p = form.cleaned_data['name_p']
            number_of_Student = form.cleaned_data['number_of_Student']
            title_Maghale = form.cleaned_data['title_Maghale']
            Code_Maghale = form.cleaned_data['Code_Maghale']
            Grouping_Maghale = form.cleaned_data['Grouping_Maghale']
            file = form.cleaned_data['file']
            ShortExplanation = form.cleaned_data['ShortExplanation']
            prof = Professor.objects.raw('select * from APP1_professor where name_p = %s', [name_p])
            proff = prof[0]
            student = Student.objects.get(number_of_student=number_of_Student)
            
            maghale = Maghale.objects.create(Code_Maghale=Code_Maghale, title_Maghale=title_Maghale,ShortExplanation=ShortExplanation,
                                             Grouping_Maghale=Grouping_Maghale, Professor_Maghale=proff, student=student, file=file)

            maghale.save()
            return HttpResponse('maghale created')

    else:
        form = AddmaghaleForm()
        blog = Maghale.objects.raw('select * from APP1_maghale')

    context = {'form': form}
    return render(request, 'APP1/addMaghale.html', context)


def search(request):
    maghale = Maghale.objects.all()
    if request.method == 'POST':
        title = request.POST['etitle']
        student = request.POST['estudent']
        professor = request.POST['eprofessor']

        try:
            professoremp = Professor.objects.raw('select * from APP1_professor where name_p = %s', [professor])[0]
        except:
            professoremp = None
        try:
            studentemp = Student.objects.raw('select * from APP1_student where name_s = %s', [student])[0]
        except:
            studentemp = None
        if  True:      
            if (title and not student and not professor):
                maghale = Maghale.objects.raw('select * from APP1_maghale where title_Maghale = %s', [title])
            elif(student and not title and not professor and studentemp):
                maghale = Maghale.objects.raw('select * from APP1_maghale where student_id = %s', [studentemp.id])
 
            elif(professor and not title and not student and professoremp):
                maghale = Maghale.objects.raw('select * from APP1_maghale where Professor_Maghale_id = %s', [professoremp.id])

            elif(student and professor and not title and professoremp and studentemp):
                maghale = Maghale.objects.raw('select * from APP1_maghale where student_id = %s and Professor_Maghale_id = %s', [studentemp.id, professoremp.id])

            elif(student and title and not professor and studentemp ):
                maghale = Maghale.objects.raw('select * from APP1_maghale where student_id = %s and title_Maghale = %s', [studentemp.id, title])

            elif(title and professor and not student and professoremp):
                maghale = Maghale.objects.raw('select * from APP1_maghale where title_Maghale = %s and Professor_Maghale_id = %s', [title, professoremp.id])
            elif(studentemp and professoremp and title ):
                maghale = Maghale.objects.raw(
                    'select * from APP1_maghale where student_id = %s and Professor_Maghale_id = %s and title_Maghale = %s', [studentemp.id, professoremp.id, title])
            context = {
                'maghale': maghale
            }
            return render(request, 'APP1/search.html', context)
    return render(request, 'APP1/search.html')


def PostLike(request, id):
    post = Maghale.objects.raw(f'SELECT * FROM APP1_maghale WHERE id = {id}')[0]
    user = request.user
    try:
        puser = Professor.objects.get(user=user)
        if (post.Professor_Maghale == puser):
            if puser.user.is_authenticated:

                if puser.user in post.like.all():
                    return HttpResponse('you like this post already')
                else:

                    post.like.add(puser.user)
                    post.vaziat = 'like'
                    post.save()
                    return redirect('details', id)
            else:
                return HttpResponse('you not allow like this post')
        else:
            return HttpResponse("you are not this article professor ")
    except:
        return HttpResponse("you are not professor")


def PostunLike(request, id):
    post = Maghale.objects.raw(f'SELECT * FROM APP1_maghale WHERE id = {id}')[0]
    user = request.user
    try:
        puser = Professor.objects.get(user=user)

        if puser.user.is_authenticated:

            if puser.user in post.like.all():
                post.like.remove(puser.user)
                post.vaziat = 'dislike'
                post.save()
                return redirect('details', id)
            else:
                return HttpResponse('you not like this post')
        else:
            return HttpResponse('you not allow like this post')

    except:
        return HttpResponse("you are not professor")
