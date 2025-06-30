# MedicSystem
Este repositorio contiene la implementación del backend para un Sistema de Citas Médicas, desarrollado como parte de la Tarea T02.03: Construcción de aplicación de software. El objetivo de este proyecto es crear una API robusta y escalable que gestione las operaciones fundamentales de un sistema de salud, siguiendo los estándares de diseño y requisitos especificados en los documentos complementarios.

## Integrantes
- Adriana Morales
- Geovanny Urgiles
- Danilo Morocho
- Keira Ramos

## Tecnología Clave
Framework Web: FastAPI para construir la API de manera rápida y eficiente.

Base de Datos: Principalmente diseñado para PostgreSQL (mediante psycopg2-binary), pero compatible con otras bases de datos soportadas por SQLAlchemy.

Object-Relational Mapper (ORM): SQLAlchemy para la interacción con la base de datos de manera programática.

Validación de Datos: Pydantic para la definición de esquemas de datos y validación automática.

Autenticación y Autorización: Se planea integrar soluciones como python-jose y passlib para la gestión segura de usuarios y roles.

Documentación API: Swagger UI y ReDoc son generados automáticamente por FastAPI para una documentación interactiva y fácil de usar.
