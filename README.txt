vers 00 creada la base de datos y la tabla de cabanas (no completa con todos los campos)
la dejamos así

de ahora en mas trabajamos en 

vers 01
empezamos a trabajar con git

-----------------------------------------------------------------------------------------------------------
--- CREAR ENTORNO VIRTUAL
python -m venv venv

    -- ACTIVAR ENTORNO VIRTUAL
    - ir a carpeta venv / Scripts
    ./activate

    -- ACTUALIR ENTORNO VIRTUAL
    - ir al raíz del proyecto
    pip install -r requirements.txt

------------------------------------------------------------------------------------------------------------
-- CREAR las TABLAS en la  LA BASE DE datos 
  (crea carpeta MIGRATIONS)
flask db init

-- IMPORTAR los MODELOS 
-- en línea 41 (o cerca) en env.py MODIFICAR  
from app.models import pagos
from app.models import *  

y luego

flask db migrate -m "cartel puto que dice boludeces"

(si da ERROR de version ... entrar a MYSQL y borrar el directorio "alembic" .... suele ocurrir al BORRARR la carpeta "migrations")

- finalmente (actualiza la base de datos)

flask db upgrade

-------------------------------------------------------------------------------------------------------------

-- GIT HUB

git log -> muestra los logs anteriores (se sale con la tecla 'q' )

git add .  ----> agrega todos los archivos 

git commit -m "ajustamos tablas pagos, y creamos los schemas de pagos y reservas "

git push origin master

-------------------------------------------------------------------------------------------------------------

Lo que definimos en mappping/Schemas ... es la comunicación bidireccional cliente-Servidor y ....
qué datos van a ser serializados/deserializados 
y qué datos NO van a ser serializados/deserializados

(atributos dump_only, required, load_only) -----> ver estos atributos un poco mejor para entenderlos



