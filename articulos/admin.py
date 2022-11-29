from django.contrib import admin
from .models import Portada
from .models import CorteMujer
from .models import Info_Color
from .models import Portada_dos
from .models import Horario
from .models import Trabajos
from .models import Promociones
from .models import Recomendaciones

# Register your models here.
admin.site.register(Portada)
admin.site.register(CorteMujer)
admin.site.register(Info_Color)
admin.site.register(Portada_dos)
admin.site.register(Horario)
admin.site.register(Trabajos)
admin.site.register(Recomendaciones)
admin.site.register(Promociones)