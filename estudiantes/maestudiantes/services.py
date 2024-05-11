from .models import Direccion, Profesor, Estudiante, Curso
from datetime import date

def crear_curso(codigo, nombre, version, profesor_id):
    """
    Crea un nuevo curso en la base de datos.

    Args:
        codigo (str): Código único del curso.
        nombre (str): Nombre del curso.
        version (int): Versión del curso.
        profesor_id (str): Rut del profesor asociado al curso.

    Returns:
        Curso: Instancia del curso creado.
    """
    profesor = Profesor.objects.get(rut=profesor_id)
    curso = Curso.objects.create(codigo=codigo,nombre=nombre,version=version, profesor=profesor)
    return curso

def crear_profesor(rut, nombre, apellido, activo, creado_por):
    """
    Crea un nuevo profesor en la base de datos.

    Args:
        rut (str): Rut del profesor.
        nombre (str): Nombre del profesor.
        apellido (str): Apellido del profesor.
        activo (bool): Estado de actividad del profesor.
        creado_por (str): Usuario que creó al profesor.

    Returns:
        Profesor: Instancia del profesor creado.
    """
    profesor = Profesor.objects.create(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creado_por=creado_por)
    return profesor

def crear_estudiante(rut, nombre, apellido, fecha_nac, activo, creado_por):
    """
    Crea un nuevo estudiante en la base de datos.

    Args:
        rut (str): Rut del estudiante.
        nombre (str): Nombre del estudiante.
        apellido (str): Apellido del estudiante.
        fecha_nac (date): Fecha de nacimiento del estudiante.
        activo (bool): Estado de actividad del estudiante.
        creado_por (str): Usuario que creó al estudiante.

    Returns:
        Estudiante: Instancia del estudiante creado.
    """
    estudiante = Estudiante.objects.create(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, activo= activo, creado_por=creado_por)
    return estudiante

def crear_direccion(calle, numero, dpto, comuna, ciudad, region, estudiante_id):
    """
    Crea una nueva dirección en la base de datos y la asocia a un estudiante.

    Args:
        calle (str): Nombre de la calle.
        numero (str): Número de la dirección.
        dpto (str): Departamento de la dirección.
        comuna (str): Comuna de la dirección.
        ciudad (str): Ciudad de la dirección.
        region (str): Región de la dirección.
        estudiante_id (str): Rut del estudiante asociado a la dirección.

    Returns:
        Direccion: Instancia de la dirección creada.
    """
    estudiante = Estudiante.objects.get(rut=estudiante_id)
    direccion = Direccion.objects.create(calle=calle, numero=numero, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region, estudiante=estudiante)
    return direccion
def obtener_estudiante(rut_estudiante):
    """
    Obtiene un estudiante de la base de datos por su rut.

    Args:
        rut_estudiante (str): Rut del estudiante a buscar.

    Returns:
        Estudiante: Instancia del estudiante encontrado.
    """
    estudiante = Estudiante.objects.get(rut=rut_estudiante)
    return estudiante

def obtener_profesor(rut_profesor):
    """
    Obtiene un profesor de la base de datos por su rut.

    Args:
        rut_profesor (str): Rut del profesor a buscar.

    Returns:
        Profesor: Instancia del profesor encontrado.
    """
    profesor = Profesor.objects.get(rut=rut_profesor)
    return profesor

def obtener_curso(codigo_curso):
    """
    Obtiene un curso de la base de datos por su código.

    Args:
        codigo_curso (str): Código del curso a buscar.

    Returns:
        Curso: Instancia del curso encontrado.
    """
    curso = Curso.objects.get(codigo=codigo_curso)
    return curso

def agregar_profesor_a_curso(profesor_id, codigo_curso):
    """
    Asocia un profesor a un curso.

    Args:
        profesor_id (str): Rut del profesor.
        codigo_curso (str): Código del curso.

    Returns:
        Curso: Instancia del curso actualizado con el profesor asociado.
    """
    profesor = Profesor.objects.get(rut=profesor_id)
    curso = Curso.objects.get(codigo=codigo_curso)
    curso.profesor = profesor
    curso.save()
    return curso

def agregar_cursos_a_estudiante(estudiante_id, codigo_curso):
    """
    Asigna un curso a un estudiante.

    Args:
        estudiante_id (str): Rut del estudiante.
        codigo_curso (str): Código del curso.

    Returns:
        Estudiante: Instancia del estudiante actualizado con el curso asignado.
    """
    estudiante = Estudiante.objects.get(rut=estudiante_id)
    curso = Curso.objects.get(codigo=codigo_curso)
    estudiante.cursos.add(curso)
    return estudiante

def imprimir_estudiante_cursos(rut_estudiante):
    try:
        estudiante = Estudiante.objects.get(rut=rut_estudiante)
        cursos = estudiante.cursos.all()
        print(f"Cursos de {estudiante.nombre} {estudiante.apellido}:")
        for curso in cursos:
            print(f"- {curso.nombre}")
    except Estudiante.DoesNotExist:
        print("Estudiante no encontrado.")
