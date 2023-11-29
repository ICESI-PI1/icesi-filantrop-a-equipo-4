from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from ..forms import EventForm
from ..models import Event
from ..models import Sponsor_Event
from ..forms import CombinedForm  
from ..forms import EventSearchForm
from ..forms import SponsorEventForm
from django.contrib.auth.decorators import login_required
@login_required
def event(request):
    events = Event.objects.all()
    return render (request, 'event.html',{
        'events':events,
        'template':'event.html'
    })


@login_required
def register_event(request):
    if request.method == 'POST':
        try:
            combined_form = CombinedForm(request.POST)

            if combined_form.is_valid():
                # Obtener el nombre del evento seleccionado en el formulario
                event_name = request.POST.get('name')
                
                event_date = request.POST.get('date')
                event_type = request.POST.get('event_Type')
                event_time = request.POST.get('time')
                # Verificar si ya existe un evento con el mismo nombre
                event, created = Event.objects.get_or_create(
                    name=event_name,
                    date=event_date,
                    event_Type=event_type.upper(),  # Convierte a mayúsculas para que coincida con las opciones del modelo
                    time = event_time
                )

                # Guardar el formulario compuesto que incluye datos de evento y participación del patrocinador
                sponsor_event = combined_form.save(commit=False)

                # Obtener el ID del patrocinador seleccionado en el formulario
                sponsor_id = combined_form.cleaned_data['sponsor_name']

                # Asignar el patrocinador y el evento a la instancia de Sponsor_Event
                sponsor_event.Sponsor_id_id = sponsor_id
                sponsor_event.event_name = event

                # Guardar la instancia de Sponsor_Event
                sponsor_event.save()

                return redirect('event')
            else:
                # En caso de datos no válidos, manejar los errores de validación
                return render(request, 'register_event.html', {
                    'combined_form': combined_form,
                    'error': "Introduce datos válidos"
                })

        except Exception as e:
            # Manejar cualquier otra excepción aquí
            return render(request, 'register_event.html', {
                'combined_form': CombinedForm(),
                'error': str(e)
            })
    else:
        # Si la solicitud es GET, renderizar el formulario compuesto vacío
        combined_form = CombinedForm()

        return render(request, 'register_event.html', {
            'combined_form': combined_form
        })
@login_required            
def event_detail(request, event_id):

    if request.method == 'GET':
        event = get_object_or_404(Event, pk=event_id)
        event_form = EventForm(instance=event)

        # Obtener todas las participaciones de patrocinadores relacionadas con el evento
        sponsor_events = Sponsor_Event.objects.filter(event_name=event)

        # Crear una lista para almacenar los detalles de los patrocinadores y sus participaciones
        sponsor_details = []

        # Iterar a través de las participaciones de patrocinadores
        for sponsor_event in sponsor_events:
            sponsor = sponsor_event.Sponsor_id
            participation = sponsor_event.participation
            sponsor_details.append({'sponsor': sponsor, 'participation': participation})

        return render(request, 'event_detail.html', {
            'event': event,
            'event_form': event_form,  # Pasa el formulario del evento a la plantilla
            'template':'event_detail.html',
            'sponsor_details': sponsor_details,  # Pasa los detalles de los patrocinadores a la plantilla
        })
            
@login_required
def update_event(request, event_id):
    if request.method == 'GET':
        event=get_object_or_404(Event,pk=event_id)
        form =EventForm(instance=event)
        return render(request, 'update_event.html',
                    {
                        'form': form
                    })
    else:
       try: 
        event=get_object_or_404(Event,pk=event_id)
        form =EventForm(request.POST, instance=event)
        form.save()
        return redirect('show_events')
       except:
            return render(request, 'update_event.html',
                    {
                        'form':form,
                        'error': "Error updating event"
                    }) 
@login_required
def show_events(request):
    events = Event.objects.all()
    search_form = EventSearchForm(request.GET)

    if search_form.is_valid():
        nombre_evento = search_form.cleaned_data.get('nombre_evento')
        fecha_evento = search_form.cleaned_data.get('fecha_evento')

        if nombre_evento:
            events = events.filter(name__icontains=nombre_evento)

        if fecha_evento:
            events = events.filter(date=fecha_evento)

        if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            html = render_to_string('event_search_results.html', {'events': events})
            return JsonResponse({'html': html})

    return render(request, 'event_list.html', {'events': events, 'search_form': search_form})
     


@login_required
def delete_event(request, event_id): 
    event=get_object_or_404(Event,pk=event_id)  
    if request.method == 'POST':
        event.delete()
        return redirect('event')
        