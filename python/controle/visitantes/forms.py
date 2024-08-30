from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = (
            "nome_completo",
            "cpf",
            "data_nascimento",
            "numero_casa",
            "placa_veiculo",
        )

        error_messages = {
            "nome_completo": {
                "required": "O nome completo é obrigatório"
            },
            "cpf": {
                "required": "O CPF é um campo obrigatório"
            },
            "data_nascimento": {
                "required": "A data é obrigatória",
                "invalid": "A data precisa ter o formato DD/MM/YYYY"
            },
            "numero_casa": {
                "required": "O número da casa é um campo obrigatório"
            }
        }
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'numero_casa': forms.TextInput(attrs={'class': 'form-control'}),
            'placa_veiculo': forms.TextInput(attrs={'class': 'form-control'}),
        }
        criar_mensagens = {
            "nome_completo":{
                "required": "O nome completo é obrigatório"
            },
            "cpf": {
                "required": "O CPF é um campo obrigatório"
            },
            "data_nascimento":{
                "required": "A data é obrigatória",
                "invalid": "A data precisa ter o formato DD/MM/AAAA"
            },
            "numero_casa": {
                "required": "O número da casa é um campo obrigatório"
            },
        }
       