from django.shortcuts import render
from .models import CorteMujer
from .models import Portada
from .models import Info_Color
from .models import Portada_dos
from .models import Trabajos
from .models import Horario
from .models import Promociones
from .models import Recomendaciones

# Create your views here.
def inicio(request):
	cortemujer = CorteMujer.objects.all()
	portada = Portada.objects.all()
	portadados = Portada_dos.objects.all()
	trabajos = Trabajos.objects.all()
	horario = Horario.objects.all()
	promociones = Promociones.objects.all()
	recomendaciones = Recomendaciones.objects.all()
	return render(request, 'articulos/inicio.html',{'cortemujer':cortemujer,'portada':portada,'portadados':portadados,
		'trabajos':trabajos,'horario':horario,'recomendaciones':recomendaciones,'promociones':promociones})



def colores(request, pk):
	info_color.objects.get(pk=pk)
	return render(request,'articulos/colores.html',{'info_color':info_color})

