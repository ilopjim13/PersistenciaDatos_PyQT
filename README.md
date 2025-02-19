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
