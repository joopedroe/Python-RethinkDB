from django import forms

class NewCharacterForm(forms.Form):
    nome = forms.CharField(max_length=50, required=True)
    xp = forms.IntegerField(
        label='Pontos de Experiência',
        required=True
    )
    habilidade = forms.CharField(
        label='Habilidade Especial', 
        max_length=50, 
        required=True
    )
    poder = forms.IntegerField(
        label='Nível de Poder',
        max_value=8000,
        required=False
    )


class UpdateForm(forms.Form):
    id = forms.CharField(
        label='Identificador do Personagem', 
        max_length=100,
        required=False
    )
    nome = forms.CharField(max_length=50, required=True)
    xp = forms.IntegerField(
        label='Pontos de Experiência',
        required=True
    )
    habilidade = forms.CharField(
        label='Habilidade Especial', 
        max_length=50, 
        required=True
    )
    poder = forms.IntegerField(
        label='Nível de Poder',
        max_value=8000,
        required=False
    )


class ReadForm(forms.Form):
    id = forms.CharField(
        label='Identificador do Personagem', 
        max_length=100,
        required=True
    )


class DeleteForm(forms.Form):
    id = forms.CharField(
        label='Identificador do Personagem', 
        max_length=100,
        required=True
    )