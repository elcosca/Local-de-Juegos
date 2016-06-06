from django.contrib import admin
from .models import Empleados
from .models import Clientes
from .models import TipodeTrabajo
from .models import Productos
from .models import Plataformas
from .models import Proveedor
from .models import Turnos


admin.site.register(Empleados)
admin.site.register(Clientes)
admin.site.register(TipodeTrabajo)
admin.site.register(Productos)
admin.site.register(Plataformas)
admin.site.register(Proveedor)
admin.site.register(Turnos)