from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory
import random
import string
from election.models import *
from election.forms import *

from django.contrib.auth.models import User


# Create your views here.
def create_user(request):
    if request.user.is_authenticated:
        return HttpResponse("Wow Mats du begynner å bli flink!")
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return HttpResponse("det funka")
        else:
            form = UserCreationForm()

    return render(request, 'election/create_user.html', {'form': form})

def dritidette(request):
    if request.user.is_authenticated:
        return HttpResponse("Why u here, u fckn logged in already???!?!?!?!")
    else:
        if request.method == 'POST':
            pass

    return render(request, 'election/login.html', {'form': form})

def dashboard(request):
    if request.user.is_authenticated:
        elections = Election.objects.filter(Owner = request.user.username)
    else:
        return HttpResponse("You must be logged in to edit elections")

    return render(request, 'election/dashboard.html', {'elections': elections})

def get_election_id(request):
    election = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
    check = Election.objects.filter(Election_ID = election)
    if request.user.is_authenticated:
         if check.count() > 0:
             return HttpResponse('hei')
         else:
            a = Election(Election_ID = election, Owner = str(request.user.username))
            a.save()
            return redirect('/dashboard/edit_election/%s' % election)
    else:
        return HttpResponse("You must be logged in to create elections")




def create_election(request, election):
    if request.user.is_authenticated:
        election = get_object_or_404(Election, Election_ID=election)
        if request.user.username == election.Owner:
            election_id = election.Election_ID
            questions = Question.objects.filter(Election_ID=election_id)
            return HttpResponse("Funka dette a?")

            #Her er det egt ikke vits i å gjøre noe mer før JS er på plass


        else:
            return HttpResponse("You do not have permission to edit this election")
    else:
        return HttpResponse("You must be logged in to edit elections")































    """if request.user.is_authenticated:
        election = get_object_or_404(Election, Election_ID=election)
        if request.user.username == election.Owner:
            extra_number = 1
            alternativeformset = formset_factory(Create_Alternative, extra=election.Number_Of_Alternatives)
            form = Choose_Election_Method_And_Name()
            formset = alternativeformset()
            add_form = Add_Alternative()
            if request.method == 'POST':
                submitted = request.POST.get('form_id', '')

                #Finds out what form is submitted,
                and uses this data to either add an extra form
                in the formset, or submit the data and create
                the election

                if submitted == 'add_alt':

                    add_form = Add_Alternative(request.POST)
                    if add_form.is_valid():
                        election.Number_Of_Questions += 1
                        election.save()
                        return redirect('/dashboard/edit_election/%s' % election)


                elif submitted == 'save':
                    form = Choose_Election_Method_And_Name(request.POST)
                    formset = alternativeformset(request.POST)
                    if form.is_valid():
                        election.Description = form.cleaned_data['Description']
                        election.Name = form.cleaned_data['Name']
                        election.Election_Method = form.cleaned_data['method']
                        election.save()
                    if formset.is_valid():
                        for form in formset:
                            a = Alternative(Election_ID=election)
                            a.Wording = form.cleaned_data['Wording']
                            a.save()
            else:
                add_form = Add_Alternative()
                form = Choose_Election_Method_And_Name()
                formset = alternativeformset()

            return render(request, 'election/election_method.html', {'form': form, 'formset': formset, 'add_form': add_form})
        else:
            return HttpResponse("You cannot edit an election you do not own")
    else:
        return HttpResponse("You must be logged in to create elections")"""




    