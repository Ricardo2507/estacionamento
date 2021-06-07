from django.forms import  ModelForm
from . models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista, 
    MovMensalista
)

# ModelForm serve para criar o formulário de um Model
# o Form é um formulário comum que não tem relação com seu
# banco de dados (model).
class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        
class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
        
class MovRotativoForm(ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__'
        
class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'
        
class MovMensalistaForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'
