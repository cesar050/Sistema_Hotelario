CORRER LA RAMA MARCO

# Primer paso INSTALAR requeriment.txt con el comando 
#### pip install -r requirements.txt
estando en el documento donde se encuantre el manage.py
![image](https://github.com/cesar050/Sistema_Hotelario/assets/166522774/c196f7f0-0a1c-4eea-8129-01f5a66516c6)

# Sistema Hotelario

Este proyecto es una aplicación web desarrollada con Django. La estructura del proyecto es la siguiente:

## Estructura del Proyecto

- `SistemaHotelario`: Carpeta principal del proyecto.
  - `adminHotel`: Módulo para la gestión de administradores del hotel.
  - `recepcion_panel`: Módulo para el panel de recepción.
  - `reservation_manager`: Módulo para la gestión de reservas.
  - `user_manager`: Módulo para la gestión de usuarios.

Cada módulo contiene los siguientes archivos:
- `models.py`: Define los modelos de datos.
- `views.py`: Contiene las vistas de la aplicación.
- `forms.py`: Define los formularios.
- `tests.py`: Contiene las pruebas unitarias.
- `admin.py`: Registro de los modelos para el administrador de Django.
- `apps.py`: Configuración de la aplicación.
- `urls.py`: Define las rutas URL de la aplicación.

Además, cada módulo puede tener una carpeta `templates` que contiene los archivos HTML para las vistas, y una carpeta `migrations` que contiene los archivos de migración de la base de datos.

Metodos para instalar nuestro programa.
1.  Asegurarse de tener instalada la ultima version de Python, en caso de que el SDK o tenga otro problema con el entorno en pycharm, debe ir a la pagina de Python y descargar la ultima version.
![image](https://github.com/cesar050/Sistema_Hotelario/assets/166522713/6cb54ef2-b5e3-4848-841a-c18006029158)

Link de descarga https://www.python.org/getit/

2.  Una vez descargado, hacen doble click y seleccionan lo que se ve en la imagen.

![image](https://github.com/cesar050/Sistema_Hotelario/assets/166522713/2d3842d6-929a-429f-a49a-69900d20c2f7)


3.  Una vez selecionnado eso le dan click a Install Now y lo tendran cargando asi.

![image](https://github.com/cesar050/Sistema_Hotelario/assets/166522713/3bafe55e-5202-4fb8-90ac-ab3c9edaa07f)

Una vez terminado tendran esto.

![image](https://github.com/cesar050/Sistema_Hotelario/assets/166522713/18499d44-1dbb-4d07-8b80-a4ed69270d85)

Le dan a close y ahora van al Pycharm.

4.  Una vez dentro de Pycharm actualizan el Python interprete 

![image](https://github.com/cesar050/Sistema_Hotelario/assets/166522713/7f2d0ee3-c44c-4466-bf12-074b43adfc6a)

5.  Seleccionan uno y ya estaria cambiado.

![image](https://github.com/cesar050/Sistema_Hotelario/assets/166522713/9c51c0f7-fdaa-483e-9a4b-09a658a1c69c)

6.  luego de eso en la terminal escriben el comando, pip install -r requerimentes.txt les debe salir de la siguiente manera

![image](https://github.com/cesar050/Sistema_Hotelario/assets/166522713/028a18f7-117c-4d71-a2c5-eac3064a7ca5)

7.  Una vez hecho eso escriben en la terminal cd SistemaHotelario y finalmente, en la terminal nuevamente python manage.py runserver, les debe quedar tal que asi

![image](https://github.com/cesar050/Sistema_Hotelario/assets/166522713/a24dcbac-776c-4552-ba85-c9a286e49745)

8.  Finalmente acceden con la ip http://127.0.0.1:8000/admin, el super usuario es: marco1, clave: 1234, una vez dentro podran acceder y comprobar que todo funciona correctamente, al igual que pueden acceder a la diferentes secciones de las siguientes maneras, http://127.0.0.1:8000/vista/, http://127.0.0.1:8000/administracion/ y otras mas.
>>>>>>> f08e6ff9ab6d9039e0de9d32ece98b806d4ebc75

RESUMEN DE COMANDOS

pip install -r requerimentes.txt

cd SistemaHotelario

python manage.py runserver
