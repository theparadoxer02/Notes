from django.utils import timezone
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect ,Http404, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Note
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import notesform,EmailForm,searchform
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages



def uploads(request):
    return render(request,'upload_sucess.html')


def showNotes(request,pk):
    note = get_object_or_404(Note, pk=pk)
    year = note.year
    branch = note.branch
    subject_name = note.subject_name
    unit = note.unit
    picture = note.picture
    context = {
            'name':subject_name,
            'picture' : picture,
            'year'    : year,
            'branch'  : branch,
            'unit'    : unit,
            }

    notes = Note.objects.all()
    paginator = Paginator(notes, 4)
    page = request.GET.get('page')
    try:
        note = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)
    return render(request,'note.html',{'notes':notes})


def addNotes(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = notesform(request.POST,request.FILES)
            if form.is_valid():
                profile = Note()
                profile.year = form.cleaned_data["year"]
                profile.branch = form.cleaned_data["branch"]
                profile.subject_name = form.cleaned_data["subject_name"]
                profile.picture = form.cleaned_data["picture"]
                post = form.save(commit=False)
                post.save()
                return redirect('uploadsucess')
        else:
            form = notesform()
        return render(request, 'newNotes.html', {'form': form})
    else:
        return redirect('/accounts/login/')



def Email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = settings.DEFAULT_FROM_EMAIL
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = "HI";
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                        [email], fail_silently=False)
            return redirect('showProfile')
    else:
        form = EmailForm()
    return render(request,'send_mail.html',{'eform':form})


def search(request):
    if request.method == 'POST':
        form = searchform(request.POST)
        if form.is_valid():
            year = form.cleaned_data["year"]
            branch = form.cleaned_data["branch"]
            subject_name = form.cleaned_data["subject_name"]
            unit = form.cleaned_data["unit"]
            print(year)
            print(branch)
            print(subject_name)
            print(unit)
            notes_list = Note.objects.all().filter(branch=branch,year=year,subject_name=subject_name,unit=unit)
            paginator = Paginator(notes_list,4)
            page = request.GET.get('page')
            try:
                notes = paginator.page(page)
            except PageNotAnInteger:
                notes = paginator.page(1)
            except EmptyPage:
                notes = paginator.page(paginator.num_pages)
            return render(request,'search.html',{ 'notes':notes})
    else:
        form = searchform()
        return  render(request,'search.html',{'form':form} )

def notes_delete(request,id):
    obj = get_object_or_404(Note,id=id)
    #if request.method == "POST":

    #messages.success(request, "This has been deleted.")
    #return HttpResponseRedirect('/search/')
    context = { "object":obj }
    obj.delete()
    return render(request,"delete_success.html",context)
    #return render(request,"confirm_delete.html",context)
