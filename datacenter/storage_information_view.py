from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, format_duration, is_visit_long


def storage_information_view(request):
    non_closed_visits_queryset = Visit.objects.filter(leaved_at=None)
    non_closed_visits = [
        {
            "who_entered": visit.passcard.owner_name,
            "entered_at": visit.entered_at,
            "duration": format_duration(get_duration(visit)),
            "is_strange": is_visit_long(visit)
        }
        for visit in non_closed_visits_queryset
    ]

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
