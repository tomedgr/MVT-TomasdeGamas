from django.http import HttpResponse
from django.template import loader
from primerasvistas.models import Hermana, Madre, Padre

def familia(request):
    
    template1 = loader.get_template('prueba.html')
    
    padre = Padre(nombre='Juan Carlos', edad=67, fecha_nacimiento='1955-1-6')
    
    madre = Madre(nombre='Monica', edad=72, fecha_nacimiento='1950-7-4')
    
    hermana = Hermana(nombre='Lucila', edad=34, fecha_nacimiento='1988-2-1')
    
    render1 = template1.render({'padre': padre, 'madre': madre,
                            'hermana': hermana,})
    
    
    return HttpResponse(render1)