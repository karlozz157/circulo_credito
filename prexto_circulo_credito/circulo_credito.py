import requests
import os

from .utils import shell_exec, guzzle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class CirculoCredito(object):
    URL =  '172.17.1.14'
    PF_PORT = 26000 
    PM_PORT = 30010

    CLAVE_OTORGANTE = '0000821006'
    NOMBRE_USUARIO = 'IHG8728CCO'
    PASSWORD = 'pru3ba00'
    VERSION_XML = '1'

    PRODUCTO_REQUERIDO = '1'
    TIPO_CUENTA = 'F'
    CLAVE_UNIDAD_MONETARIA = 'MX'

    def __init__(self, persona, es_empresa=False, debug=False):
        self.persona = persona
        self.port = self.PM_PORT if es_empresa else self.PF_PORT
        self.debug = debug

    def request_score(self, callback=None):
        """
        Hace la petición a circulo de credito y regresa el score

        Keyword Arguments:
            callback {function} -- callback para que el usuario realicé alguna acción  (default: {None})

        Returns:
            bool -- [description]

        Raises:
            Exception -- [description]
        """
        request_as_xml = self.__get_request_as_xml()

        if self.debug:
            print(request_as_xml)

        shell_exec(self.URL)

        guzzle(self.URL, self.port, request_as_xml, callback)

        return True

    def __get_request_as_xml(self):
        """
        Setea los valores de la persona al xml para hacer la petición

        Returns:
            String
        """
        xml_template = self.__get_xml_template()

        return xml_template.format(
                self.CLAVE_OTORGANTE,
                self.NOMBRE_USUARIO,
                self.PASSWORD,
                self.VERSION_XML,

                self.persona.contrato.folio_consulta_otorgante,
                self.PRODUCTO_REQUERIDO,
                self.TIPO_CUENTA,
                self.CLAVE_UNIDAD_MONETARIA,
                self.persona.contrato.importe,
                self.persona.contrato.numero_firma,

                self.persona.nombre.apellido_paterno,
                self.persona.nombre.apellido_materno,
                self.persona.nombre.nombre,
                self.persona.nombre.fecha_nacimiento,
                self.persona.nombre.rfc,
                self.persona.nombre.curp,
                self.persona.nombre.nacionalidad,
                self.persona.nombre.residencia,
                self.persona.nombre.estado_civil,
                self.persona.nombre.sexo,
                self.persona.nombre.clave_elector_ife,
                self.persona.nombre.numero_dependientes,

                self.persona.domicilio.direccion,
                self.persona.domicilio.colonia,
                self.persona.domicilio.municipio,
                self.persona.domicilio.ciudad,
                self.persona.domicilio.estado,
                self.persona.domicilio.codigo_postal,
                self.persona.domicilio.fecha_residencia,
                self.persona.domicilio.numero_telefono,
                self.persona.domicilio.tipo_domicilio,
                self.persona.domicilio.tipo_asentamiento,

                self.persona.empleo.empresa,
                self.persona.empleo.direccion,
                self.persona.empleo.colonia,
                self.persona.empleo.municipio,
                self.persona.empleo.ciudad,
                self.persona.empleo.estado,
                self.persona.empleo.codigo_postal,
                self.persona.empleo.numero_telefono,
                self.persona.empleo.extension,
                self.persona.empleo.fax,
                self.persona.empleo.puesto,
                self.persona.empleo.fecha_contratacion,
                self.persona.empleo.clave_moneda,
                self.persona.empleo.salario_mensual,

                self.persona.cuenta.numero_cuenta
            )

    def __get_xml_template(self):
        """
        Obtiene el xml base para construir la petición

        Returns:
            String
        """
        f = open(os.path.join(BASE_DIR, 'template.xml'), 'r')
        xml_template = f.read()
        f.close()

        return xml_template
