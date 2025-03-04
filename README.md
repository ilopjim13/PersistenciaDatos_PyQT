# Para la ejecucíon del comando:
```python
pyinstaller --windowed --icon=recursos/iconos/icon.ico --add-data="BD/basedatos.py:BD" --add-data="models/cliente.py:models" --add-data="recursos/iconos/engranaje.png:recursos/iconos" --add-data="recursos/iconos/usuario.png:recursos/iconos" --add-data="recursos/media/billete.jpg:recursos/media" --add-data="recursos/media/fondo.jpg:recursos/media" --add-data="billete_ui.py:." --add-data="billete.ui:." --add-data="compra.py:." --add-data="compras_ui.py:." --add-data="compras.ui:." --add-data="configuracion_ui.py:." --add-data="configuracion.py:." --add-data="configuracion.ui:." --add-data="firebase.txt:." --add-data="recursos/iconos/icon.ico:recursos/iconos" --add-data="login_ui.py:." --add-data="login.py:." --add-data="login.ui:." --add-data="menu_ui.py:." --add-data="menu.ui:." --add-data="menu.py:." --add-data="misviajes_ui.py:." --add-data="misviajes.ui:." --add-data="recursos_rc.py:." --add-data="recursos.qrc:." --add-data="viajes.db:." --add-data="vuelos_ui.py:." --add-data="vuelos.py:." --add-data="vuelos.ui:." --name "Skyberia"
```


# Estructura de pantallas : 

- 1º Login/Register (Con sus respectivos errores y cositas).
- 2º Principal con los destinos sugeridos y buscar destinos.
- 3º Los vuelos disponibles para ese destino con sus respectivos precios y avines diferentes.
- 4º Check out para decidir numero de personas malestas etc..
- 5º Ver los datos puestos y un "Boton" descargar.
- 6º Gestión de usuario.
- 7º Pantalla para editar campos, una pantalla para todos editandos los diferentes campos si es posible mediante codigo.

# Tecnologias a usar : 

Python, PyQt, BD Local (SQL que carge lo inicial), Firebase 

# Partes a realizar

- 2º Hacer una ventana con dos TextField (Uno no se puede editar) y una qtable (o alguna manera de poner una lista bonita) con los destinos y que sean clicables.

- 3º Aparecen los vuelos con los precios con los precios, las maletas y la clase. Si no están disponibles no aparecerán. Se podrá filtrar por varios campos para el orden.

- 4º Aparecerán preguntas para agregar el viaje, nombre, datos personaes, personas a viajar, (no podrá superar el espacio del avión) y elegir hotel

- 5º Aparecerán los datos del viaje, con los datos persoanes, con el vuelo, el avion y el hotel y un boton para descargar

- 6º Pantalla de usuario con boton de actualizar que aparecerán los campos con nuestros datos para actualizarlo y cancelar nuestros viajes (esto puede ser otra pantalla ) y dos botones abajo del todo para cerrar sesión y eliminar la cuenta (deberán sacarnos al login y al eliminar borrar ese usuario)

- 7º Esta pagina aún no sé, deberemos tener un lugar donde podemos agregar, actualizar y eliminar aviones, hoteles y destinos

Lógica de negocio:

- Los aviones de cada destino pueden llenarse.
- Los usuarios pueden tener acompañantes.
- Si el avion esta lleno que no salga como viaje o destino disponible, en el apartado comprar.
- No podemos comprar destino en fecha no vigentes
- Solo los admins o agentes autorizados pueden crear destinos nuevos.
- los usuarios pueden tener un historial de viajes ya realizados (opcional)

>
    IDEAS NO CONFIRMADAS, SEGUN SU COMPLEJIDAD
    (parte nico, IDEAS FUMADAS)
    - necesitamos los diferentes aeropuerto
    - Si el avion esta lleno que no salga como viaje o destino disponible, en el apartado comprar.
    - No podemos comprar destino en fecha no vigentes
    - Solo los admins o agentes autorizados pueden crear destinos nuevos.
    - los agentes autorizados tendran un apartado ventas, donde saldra el dinero, que puede cuanto dinero ha recaudado el avion y cuantos usuarios estan inscrito en ese avion.
    - los usuarios pueden tener un historial de viajes ya realizados (opcional)
    - los aviones pueden tener un historial o campo de ultima vez revisado como ITV (opcional)
    - los usuarios pueden tener diferentes tiers depende de cuantos viajes (opcional)
    - listar viajes por destinos
    - listar viajes por precio
    - listar viajes por fecha
    - listar viajes por precio,fecha
    - listar viajes por destino,precio
    - listar viajes por aeropuertos, precio y destino
    - podemos meter un hotel
    - se pueden cancelar el viaje 1 dia antes 
    - se pueden apuntar al viaje 1 dia antes como maximo
    - los aviones pueden informar si tienen X comodidades peculiares
    - el usuario tendra una cartera virtual donde puede añadir o meter dinero mediante una ventana de pago
    - el usuario podra pagar mas dinero para poder elegir asiento 
    - cuanto mas cerca sea la fecha mas caro es el precio del viaje
    (fin parte nico, IDEAS FUMADAS)

Nombre de la aplicación:
- Skyberia 

# Documentación de `WindowManager`

## Descripción

La clase `WindowManager` se encarga de gestionar las ventanas de la aplicación. Permite mostrar diferentes ventanas, manejar la ventana actual y almacenar información relevante sobre el usuario y el token de autenticación.

## Atributos

- `current_window`: Almacena la instancia de la ventana actualmente visible.
- `ventanas`: Un diccionario que mapea los nombres de las ventanas a sus respectivas instancias. Las ventanas actualmente registradas son:
  - `menu`: Instancia de la ventana de menú.
  - `configuracion`: Instancia de la ventana de configuración.
- `token`: Variable para almacenar el token de autenticación del usuario. Inicialmente se establece en `None`.
- `usuario`: Variable para almacenar la información del usuario actual. Inicialmente se establece en `None`.

## Métodos

### `__init__(self)`

Constructor de la clase. Inicializa los atributos y crea instancias de las ventanas registradas.

### `mostrarVentana(self, nombre: str)`

Muestra la ventana especificada por el nombre. Si la ventana actual está abierta, se cierra antes de mostrar la nueva ventana.

**Parámetros:**
- `nombre` (str): El nombre de la ventana que se desea mostrar.


# Documentación de `Configuracion`

## Descripción

La clase `Configuracion` representa la ventana de configuración de la aplicación. Permite a los usuarios actualizar su información personal, como nombre, apellido y DNI. La clase también gestiona la conexión con una base de datos SQLite para almacenar y recuperar la información del usuario.

## Atributos

- `manager`: Instancia de la clase `WindowManager`, utilizada para gestionar las ventanas de la aplicación.
- `QTENombre`: Campo de texto que permite al usuario ingresar su nuevo nombre.
- `QTEApellido`: Campo de texto que permite al usuario ingresar su nuevo apellido.
- `QTEDNI`: Campo de texto que permite al usuario ingresar su nuevo DNI.
- `QPBVolver`: Botón para volver al menú principal.

## Métodos

### `__init__(self, manager)`

Constructor de la clase. Inicializa los atributos y carga la interfaz de usuario desde el archivo `configuracion.ui`. También establece la conexión del botón "Volver" con el método `obtenerUsuarioPorId`.

### `irAMenu(self)`

Cierra la ventana de configuración y muestra la ventana del menú principal.

### `actualizarUsuario(self)`

Obtiene los valores ingresados en los campos de texto y actualiza la información del usuario en la base de datos. Luego muestra un mensaje de confirmación con los datos actualizados.

### `obtenerUsuarioPorId(self, correo)`

Recupera la información del usuario de la base de datos utilizando el correo electrónico como identificador. Crea una instancia de la clase `Cliente` con la información del usuario recuperado y la asigna al atributo `usuario` del `manager`.

**Parámetros:**
- `correo` (str): El correo electrónico del usuario que se desea recuperar.

# Documentación de `Menu`

## Descripción

La clase `Menu` representa la ventana principal del menú de la aplicación. Desde esta ventana, los usuarios pueden acceder a diferentes secciones de la aplicación, como "Mis Viajes", "Destinos" y "Configuración". La clase utiliza la interfaz gráfica creada con Qt Designer y gestiona las acciones de los botones y etiquetas en la ventana.

## Atributos

- `manager`: Instancia de la clase `WindowManager`, utilizada para gestionar la navegación entre diferentes ventanas de la aplicación.
- `QLabelUsuario`: Etiqueta que muestra el ícono del usuario.
- `QLabelConfiguracion`: Etiqueta que muestra el ícono de configuración.
- `BMisViajes`: Botón para acceder a la sección "Mis Viajes".
- `BViajes`: Botón para acceder a la sección de "Compras".

## Métodos

### `__init__(self, manager)`

Constructor de la clase. Inicializa los atributos y carga la interfaz de usuario desde el archivo `menu.ui`. También establece las conexiones de los botones y etiquetas a sus respectivos métodos.

### `irAMisViajes(self)`

Cierra la ventana actual y muestra la ventana de "Mis Viajes".

### `irACompras(self)`

Cierra la ventana actual y muestra la ventana de "Compras". *(Este método está definido pero no utilizado en la implementación actual.)*

### `mousePressEventLabel(self, event)`

Maneja el evento de clic en la etiqueta de configuración (`QLabelConfiguracion`). Llama al método `irAConfiguracion` para mostrar la ventana de configuración.

### `irAConfiguracion(self)`

Cierra la ventana actual y muestra la ventana de "Configuración".

## Ejemplo de uso

```python
if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    from window_manager import WindowManager  # Asegúrate de que este import esté correcto

    app = QApplication(sys.argv)
    manager = WindowManager()
    menu = Menu(manager)
    menu.show()
    sys.exit(app.exec())
