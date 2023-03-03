#from django.shortcuts import render
from django.http import HttpResponse

from .forms import *
from .models import *
from django.views.generic import ListView,DetailView,CreateView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
def homePage(request):
    return HttpResponse('<h1>Title Here</h1>')

def homePage1(request):
    return render(
        request,
        'events/homePage.html'
    )

def listEventsStatic(request):
    # afficher list statique
    list = [
        {
            'title': 'Event1',
            'description': 'description2'
        },
        {
            'title': 'Event2',
            'description': 'description2'
        },
        {
            'title': 'Event3',
            'description': 'description3'
        }
    ]
    return render(
        request,
        'events/listEvents.html',
        {
            'events': list
        }
    )

def listEvents(request):
    # afficher list Dynamique
    list = Event.objects.all()
    return render(
        request,
         'events/listEvents.html',
        {
            'events': list
        }         
    )

def detailEvent(request, id):
    event = Event.objects.get(id=id)
    return render(
        request,
        'events/event_detail.html',
        {
            'event': event,
        }

    )



def addEvent(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES)

        if form.is_valid():
            Event.objects.create(
                # title= form.cleaned_data.get('title'),
                # description= form.cleaned_data['description'],
                # recuperer all informations
                **form.cleaned_data
            )
            return redirect('Events_listV')
                
    return render(
        request,
        'events/event_add.html',
        {
                'form': form,
        }
    )

#ModelForm
def add_Event(request):
    form = EventModelForm()
    if request.method == 'POST':
        form = EventModelForm(request.POST,request.FILES)

        if form.is_valid():
            Event.save()
            return redirect('Events_listV')
                
    return render(
        request,
        'events/event_add.html',
        {
                'form': form,
        }
    )

def update_event(request, pk):
    event= get_object_or_404(Event,pk=pk)
    if request.method == 'POST':
        form = EventModelForm(request.POST,request.FILES, instance=event)
        if form.is_valid():
            Event.save()
            return redirect('Events_listV')
        else:
            form= EventModelForm(instance=event)
            return render(
            request,
            'events/event_update.html',
            {
                    'form': form,
            }
    )

def delete_event(request, pk):
    event= get_object_or_404(Event,pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('Events_listV')
    return render(
        request,
        'events/delete_event.html',
        {
            'event': event
        }
    )

def participate(request,pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        # Create a new Participation object for the current user and event
        participation = Participation.objects.create(person=request.user, event=event)
        event.nbParticipants += 1
        event.save()
        return redirect('Events_detailV', pk=event.pk)
    context = {'event': event}
    return render(request, 'events/participate.html', context)







class EventListView(ListView):
    model = Event
    template_name= 'events/listEvents.html'
    context_object_name= 'events'

    def get_queryset(self):
        return Event.objects.filter(state=True)



class EventDetails(DetailView):
    model = Event

class EventCreateView(CreateView):
    model = Event
    form_class= EventModelForm
    template_name= 'events/event_add.html'
    success_url = reverse_lazy('Events_listV')

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventModelForm
    template_name = 'events/event_update.html'
    success_url = reverse_lazy('Events_listV')
    