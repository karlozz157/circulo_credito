from prexto_circulo_credito.circulo_credito import CirculoCredito
from prexto_circulo_credito.entities import Persona


data = {
    'contrato': {
        'folio_consulta_otorgante': '453721',
        'importe': '4500',
        'numero_firma': '0152250000123456'
    },
    'nombre': {
        'apellido_paterno': 'cervantes',
        'apellido_materno': 'luna',
        'nombre': 'araceli',
        'fecha_nacimiento': '1975-05-08',
        'rfc': 'CELA7505082I2',
        'curp': 'CELA750508MDFRRNA4',
        'nacionalidad': 'MX', #revisar documentación
        'residencia': '1', #revisar documentación
        'estado_civil': 'S', #revisar documentación
        'sexo': 'F', #revisar documentación
        'numero_dependientes': '2',
    },
    'domicilio': {
        'direccion': 'rio ayotla mz 46 lt 9',
        'colonia': 'el salado',
        'municipio': 'la paz',
        'ciudad': '',
        'estado': 'Mex',
        'codigo_postal': '56524',
        'numero_telefono': '5526135704',
        'fecha_residencia': '1999-05-12',
        'tipo_domicilio': 'C', #revisar documentación
        'tipo_asentamiento': '7', #revisar documentación
    },
    'empleo': {
        'direccion': 'unidad miguel hidalgo mz 5 lt 3',
        'colonia': 'tezozomoc',
        'municipio': 'azcapotzalco',
        'ciudad': '',
        'estado': 'cdmx',
        'codigo_postal': '02450',
        'numero_telefono': '53821420',
        'empresa': 'taller de vulcanizadora',
        'extension': '',
        'fax': '',
        'puesto': '',
        'fecha_contratacion': '1999-08-30',
        'clave_moneda': 'MX', #revisar documentación
        'salario_mensual': '7000',
    },
    'cuenta': {
        'numero_cuenta': '000110250001053856'
    }
}

persona = Persona(data)

def parse_response(res):
        print(res)

circulo_credito = CirculoCredito(persona)
circulo_credito.request_score(parse_response)
