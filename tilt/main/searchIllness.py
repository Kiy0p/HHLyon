#!/usr/bin/env python3

from .models import Illness

class SearchIllness:
    def retrieve():
        return(Illness.objects.all())
    
    def search(rawInput):
        input = rawInput.POST.get("illnessName")
        listOfIllness = []

        data = SearchIllness.retrieve()
        for i in data:
            if input in i.name or input in i.symptoms:
                listOfIllness.append({
                    'name': i.name,
                    'symptoms': i.symptoms,
                    'description': i.description,
                    'more': i.more
                })
        return {'list': listOfIllness}
