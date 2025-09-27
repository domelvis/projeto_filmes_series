from django import forms
from .models import Serie


class SerieForm(forms.ModelForm):
    """
    Formulário para criar e editar séries.
    """
    
    class Meta:
        model = Serie
        fields = ['titulo', 'descricao', 'ano', 'genero', 'imagem']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título da série'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Digite a descrição da série'
            }),
            'ano': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1900',
                'max': '2030',
                'placeholder': 'Ex: 2023'
            }),
            'genero': forms.Select(attrs={
                'class': 'form-select'
            }),
            'imagem': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona classes CSS aos labels
        for field_name, field in self.fields.items():
            field.label = field.label.title()
            if field_name == 'imagem':
                field.required = False
    
    def clean_ano(self):
        """Valida o ano de lançamento."""
        ano = self.cleaned_data.get('ano')
        if ano and (ano < 1900 or ano > 2030):
            raise forms.ValidationError('O ano deve estar entre 1900 e 2030.')
        return ano
    
    def clean_titulo(self):
        """Valida o título da série."""
        titulo = self.cleaned_data.get('titulo')
        if titulo and len(titulo.strip()) < 2:
            raise forms.ValidationError('O título deve ter pelo menos 2 caracteres.')
        return titulo.strip()



