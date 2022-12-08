from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo ded tarea", max_length=200)
    description = forms.CharField(label="descripcion de la tarea",widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label = "Nombre del Project", max_length=200)