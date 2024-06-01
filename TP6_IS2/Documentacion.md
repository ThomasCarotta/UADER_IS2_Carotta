## Documentación del Programa

### Descripción
Este programa implementa un sistema de procesamiento de pagos utilizando el patrón de diseño de cadena de responsabilidad. Permite realizar pagos a través de diferentes bancos, verificando el saldo disponible en cada uno de ellos.

### Uso
```bash
python programa.py [archivo_json] [opcion] [<monto>]
```

**Opciones:**
- `auto`: Automáticamente elige un banco para procesar el pago basado en el monto especificado.
- `lista`: Realiza múltiples pagos y los almacena en el historial.

**Ejemplo:** 
```bash
python programa.py archivo.json auto 500.0
```

### Clases Principales
- **`LectorJSONSingleton`**: Implementa un patrón Singleton para leer un archivo JSON que contiene información sobre los bancos.
- **`Banco`**: Representa un banco con su nombre, saldo inicial y token de seguridad.
- **`Pago`**: Representa un pago realizado, almacenando el número de orden, el nombre del banco, el monto y el token.
- **`HistorialPagos`**: Mantiene un historial de pagos realizados.
- **`ManejadorPagos`**: Maneja la cadena de responsabilidad para procesar los pagos a través de los bancos disponibles.
- **`CadenaBancos`**: Construye y maneja la cadena de responsabilidad de bancos.
- **`Programa`**: Representa el programa principal, maneja la interacción con el usuario y ejecuta las acciones correspondientes.

### Flujo del Programa

1. **Configuración Inicial**:
   - El programa carga la información de los bancos desde un archivo JSON.
   - Construye la cadena de responsabilidad de bancos basada en la información cargada.

2. **Interacción con el Usuario**:
   - El usuario elige entre dos opciones: realizar un pago automático o listar múltiples pagos.
   - En el modo automático, el programa selecciona un banco automáticamente para procesar el pago proporcionando el monto del pago.
   - En el modo de lista, se realizan múltiples pagos y los detalles se registran en el historial de pagos.

### Versiones
- **Versión actual:** 1.2