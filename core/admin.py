from django.contrib import admin
from .models import Marca, Veiculo, Pessoa 
from .models import Parametros, MovRotativo, Mensalista, MovMensalista

# personalizando grid
class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'checkin', 'checkout', 'valor_hora', 'veiculo', 'pago', 
        'horas_total','total')
    
class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pgto', 'total')
   

# Register your models here.
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)
