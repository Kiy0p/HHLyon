#!/usr/bin/env python3

from .models import Illness

class SearchIllness:
    def retrieve():
        return(Illness.objects.all())
    
    def search(rawInput):
        input = rawInput.POST.get("illnessName")
        listOfIllness = []

        data = SearchIllness.retrieve()
        inputList = input.split(" ")
        for i in data:
            for j in inputList:
                if j.lower() in i.name.lower() or j.lower() in i.symptoms.lower():
                    listOfIllness.append({
                        'name': i.name,
                        'symptoms': i.symptoms,
                        'description': i.description,
                        'more': i.more
                    })
                    break
        return {'list': listOfIllness}
