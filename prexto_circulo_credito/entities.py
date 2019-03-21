class Populate(object):
    def populate(self, **kwargs):
        for key in kwargs.keys():
            value = str(kwargs[key])
            setattr(self, key, value.upper().strip())

class Persona(object):
    def __init__(self, data):
        nombre = Nombre()
        nombre.populate(**data['nombre'])

        domicilio = Domicilio()
        domicilio.populate(**data['domicilio'])

        empleo = Empleo()
        empleo.populate(**data['empleo'])

        contrato = Contrato()
        contrato.populate(**data['contrato'])

        cuenta = Cuenta()
        cuenta.populate(**data['cuenta'])

        self.nombre = nombre
        self.domicilio = domicilio
        self.empleo = empleo
        self.cuenta = cuenta
        self.contrato = contrato

class Contrato(Populate):
    def __init__(self):
        self.folio_consulta_otorgante = ''
        self.importe = ''
        self.numero_firma = ''

class Cuenta(Populate):
    def __init__(self):
        self.numero_cuenta = ''

class Nombre(Populate):
    def __init__(self):
        self.apellido_paterno = ''
        self.apellido_materno = ''
        self.apellido_adicional = ''
        self.nombre = ''
        self.fecha_nacimiento = ''
        self.rfc = ''
        self.curp = ''
        self.numero_seguro_social = ''
        self.nacionalidad = ''
        self.residencia = ''
        self.estado_civil = ''
        self.sexo = ''
        self.clave_elector_ife = ''
        self.numero_dependientes = ''

class AbstractDireccion(object):
    def __init__(self):
        self.direccion = ''
        self.colonia = ''
        self.municipio = ''
        self.ciudad = ''
        self.estado = ''
        self.codigo_postal = ''
        self.numero_telefono = ''

class Domicilio(AbstractDireccion, Populate):
    def __init__(self):
        AbstractDireccion.__init__(self)
        self.fecha_residencia = ''
        self.tipo_domicilio = ''
        self.tipo_asentamiento = ''

class Empleo(AbstractDireccion, Populate):
    def __init__(self):
        AbstractDireccion.__init__(self)
        self.empresa = ''
        self.extension = ''
        self.fax = ''
        self.puesto = ''
        self.fecha_contratacion = ''
        self.clave_moneda = ''
        self.salario_mensual = ''
