# Proyecto fin de curso

## Objetivos del proyecto

El objetivo del proyecto es diseñar e implementar un algoritmo en Python para calcular el sueldo a pagar a un trabajador de la empresa "Horizonte". Este algoritmo debe considerar tanto las bonificaciones como los descuentos aplicables al trabajador, basándose en datos como horas extras, días de faltas, minutos de tardanzas, y el sueldo básico. El proyecto se enfoca en aplicar prácticas de desarrollo guiado por pruebas y control de versiones para asegurar la calidad y mantenibilidad del software. El resultado final será un programa capaz de ingresar datos relevantes, calcular el sueldo neto a pagar, y generar una boleta de pago detallada para cada empleado.

## Integrantes del equipo de desarrollo

| Nombre y Apellidos               | Rol           |
| -------------------------------- | ------------- |
| Calderón Espejo Eduardo Martin   | Desarrollador |
| Ferruzo Izquierdo Jocabed Isabel | Desarrollador |
| Ortega Batalla Braulio Cesar     | Desarrollador |
| Quispe Povis Diego Marlon        | Desarrollador |
| Rodriguez Santiago Luis Gerardo  | Desarrollador |

## Listado de historias de usuario

| Prioridad | Identificador | Nombre (alias)                               | Descripción                                                                                                                                | Puntos de historia (días ideales) | Responsable                      |
| --------- | ------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- | -------------------------------- |
| 1         | HU001         | Registro de nombre y sueldo básico           | Como administrador, quiero ingresar el nombre y sueldo básico del trabajador y mantener un registro actualizado                            | 5                                 | Calderon Espejo Eduardo Martin   |
| 2         | HU002         | Registro de días de faltas                   | Como administrador, quiero registrar los días de faltas de trabajador para calcular los descuentos adecuados                               | 3                                 | Rodriguez Santiago Luis Gerardo  |
| 3         | HU003         | Registro de minutos de tardanza              | Como administrador, necesito registrar los minutos de tardanza del trabajador para aplicar los descuentos correspondientes                 | 3                                 | Ferruzo Izquierdo Jocabed Isabel |
| 4         | HU004         | Registro de horas extras                     | Como administrador, quiero registrar las horas extras de los trabajadores para asegurar un cálculo correcto de su sueldo                   | 4                                 | Ortega Batalla Braulio Cesar     |
| 5         | HU005         | Cálculo de pago por horas extras             | Como administrador necesito calcular el pago por horas extras                                                                              | 8                                 | Ortega Batalla Braulio Cesar     |
| 6         | HU006         | Asignación de bonificación por movilidad     | Como administrador, quiero asignar una bonificación por movilidad de 1000 a los trabajadores elegibles                                     | 5                                 | Calderon Espejo Eduardo Martin   |
| 7         | HU007         | Cálculo de la bonificación suplementaria     | Necesito calcular la bonificación suplementaria del sueldo básico                                                                          | 6                                 | Ferruzo Izquierdo Jocabed Isabel |
| 8         | HU008         | Cálculo de bonificaciones totales            | Como administrador quiero saber la suma total de todas las bonificaciones para cada trabajador                                             | 7                                 | Calderon Espejo Eduardo Martin   |
| 9         | HU009         | Cálculo de remuneración computable           | Como administrador necesito el cálculo de la remuneración, incluyendo el sueldo básico y todas las bonificaciones excepto las horas extras | 7                                 | Quispe Povis Diego Marlon        |
| 10        | HU010         | Cálculo de descuento por faltas              | Como administrador quiero calcular el descuento aplicable por los días de faltas basado en la remuneración.                                | 8                                 | Quispe Povis Diego Marlon        |
| 11        | HU011         | Cálculo de descuento por tardanza            | Como administrador necesito calcular el descuento por tardanzas                                                                            | 8                                 | Ferruzo Izquierdo Jocabed Isabel |
| 12        | HU012         | Cálculo de descuentos totales                | Como administrador necesito calcular la suma total de todos los descuentos                                                                 | 6                                 | Ferruzo Izquierdo Jocabed Isabel |
| 13        | HU013         | Cálculo de sueldo neto                       | Como administrador necesito calcular el sueldo neto para cada trabajador sumando el sueldo básico, las bonificaciones y los descuentos     | 10                                | Quispe Povis Diego Marlon        |
| 14        | HU014         | Generación de boletas de pago                | Como administrador quiero generar boletas de pago que muestre el detalle del sueldo, bonificaciones y descuentos                           | 12                                | Ortega Batalla Braulio Cesar     |
| 15        | HU015         | Verificación y aprobación de boletas de pago | Como gerente quiero verificar y aprobar las boletas de pago antes de su emisión final                                                      | 5                                 | Rodriguez Santiago Luis Gerardo  |
