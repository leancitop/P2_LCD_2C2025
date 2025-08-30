# Plan de Trabajo para la Implementación del Patrón Decorator

## Introducción

Este documento detalla el plan de trabajo para implementar el patrón Decorator en el proyecto Starbuzz Coffee. Se dividirá el trabajo en cuatro ramas de GitHub, cada una con responsabilidades específicas para asegurar una implementación organizada y eficiente.

## Ramas de GitHub

1. **feature/caramel-condiment**
   - **Responsabilidad:** Implementar el nuevo condimento `Caramel` con un costo fijo de $0.20.
   - **Tareas:**
     - Crear la clase `Caramel` en `condiments.py` siguiendo la estructura de otros decoradores como `Mocha`.
     - Actualizar `main.py` para incluir un ejemplo de pedido que utilice `Caramel`.
     - Asegurarse de que `get_description()` y `cost()` funcionen correctamente.

2. **feature/size-implementation**
   - **Responsabilidad:** Implementar tamaños para las bebidas y ajustar precios de condimentos según el tamaño.
   - **Tareas:**
     - Agregar métodos `set_size(size)` y `get_size()` en la clase `Beverage`.
     - Modificar la clase `Soy` para que el costo dependa del tamaño de la bebida.
     - Probar con ejemplos como *HouseBlend Venti + Soy* para validar la funcionalidad.

3. **feature/usability-enhancements**
   - **Responsabilidad:** Mejorar la usabilidad y realizar pruebas.
   - **Tareas:**
     - Implementar una función `build_beverage(base, size, condiments)` para simplificar la creación de bebidas decoradas.
     - Crear un decorador de presentación que transforme descripciones como `"Mocha, Mocha, Whip"` en `"Double Mocha, Whip"`.
     - Escribir pruebas con `pytest` para validar costos y descripciones de varios combos.

4. **feature/io-decorator-extension**
   - **Responsabilidad:** Implementar una extensión del patrón Decorator para I/O.
   - **Tareas:**
     - Crear un wrapper en Python para un stream de texto que convierta a minúsculas al leer, similar a `LowerCaseInputStream` en Java.
     - Documentar el proceso y las decisiones de diseño en el README.

## Entregables

- Código fuente actualizado en las ramas correspondientes.
- Casos de prueba (mínimo 3) para validar la funcionalidad.
- Un breve informe en el README explicando las decisiones de diseño y cómo se propagó el tamaño en las bebidas.

## Criterios de Evaluación

- Correctitud funcional en el cálculo de `cost()` y la composición de `get_description()`.
- Uso adecuado de composición y delegación.
- Cumplimiento del Principio Open–Closed (OCP).
- Calidad del código y pruebas.
- Implementación de extensiones como tamaños, builder, pretty print, y el decorador de I/O.