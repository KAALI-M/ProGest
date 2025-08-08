from django.shortcuts import render, get_object_or_404, redirect
from .models import GroupeProjet
from .forms import GroupeProjetForm
from django.shortcuts import redirect


def groupeprojet_list(request):
    groupes = GroupeProjet.objects.all()
    return render(request, 'groupeprojects/groupeprojet_list.html', {'groupes': groupes})

def groupeprojet_detail(request, pk):
    groupe = get_object_or_404(GroupeProjet, pk=pk)
    return render(request, 'groupeprojects/groupeprojet_detail.html', {'groupe': groupe})

def groupeprojet_create(request):
    if request.method == 'POST':
        form = GroupeProjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groupeprojet_list')
    else:
        form = GroupeProjetForm()
    return render(request, 'groupeprojects/groupeprojet_form.html', {'form': form})

def groupeprojet_update(request, pk):
    groupe = get_object_or_404(GroupeProjet, pk=pk)
    if request.method == 'POST':
        form = GroupeProjetForm(request.POST, instance=groupe)
        if form.is_valid():
            form.save()
            return redirect('groupeprojet_detail', pk=groupe.pk)
    else:
        form = GroupeProjetForm(instance=groupe)
    return render(request, 'groupeprojects/groupeprojet_form.html', {'form': form})

def groupeprojet_delete(request, pk):
    groupe = get_object_or_404(GroupeProjet, pk=pk)
    if request.method == 'POST':
        groupe.delete()
        return redirect('groupeprojet_list')
    return render(request, 'groupeprojects/groupeprojet_confirm_delete.html', {'groupe': groupe})

