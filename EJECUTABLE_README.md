# Sistema de Reservas de Hotel - Ejecutable

## 📁 Archivo Ejecutable

El archivo ejecutable `Hotel_Reservations.exe` se encuentra en la carpeta `dist/`.

## 🚀 Cómo usar el ejecutable

1. **Localizar el archivo**: Navega a la carpeta `dist/` en tu explorador de archivos
2. **Ejecutar**: Haz doble clic en `Hotel_Reservations.exe`
3. **Esperar**: La aplicación tardará unos segundos en iniciar (es normal)
4. **Navegador**: Se abrirá automáticamente tu navegador web predeterminado
5. **URL**: Si no se abre automáticamente, ve a `http://127.0.0.1:5000`

## 🔧 Características del Ejecutable

- **Tamaño**: Aproximadamente 50-70 MB
- **Dependencias**: No requiere Python instalado
- **Base de datos**: Se crea automáticamente al iniciar
- **Archivos**: Todos los templates y archivos estáticos incluidos
- **Navegador**: Se abre automáticamente Chrome/Edge/Firefox

## 🌐 Funcionalidades Incluidas

- ✅ Gestión de Hoteles (CRUD completo)
- ✅ Gestión de Habitaciones 
- ✅ Gestión de Clientes
- ✅ Sistema de Reservas
- ✅ Búsqueda y filtros
- ✅ Evaluaciones y comentarios
- ✅ Base de datos SQLite integrada

## 🛑 Cómo cerrar la aplicación

- **Método 1**: Cierra la ventana de la consola (ventana negra)
- **Método 2**: En la consola, presiona `Ctrl+C`
- **Método 3**: Cierra el navegador (la aplicación seguirá corriendo en segundo plano)

## 🔍 Resolución de Problemas

### La aplicación no inicia
- Verifica que no hay antivirus bloqueando el archivo
- Ejecuta como administrador si es necesario
- Verifica que el puerto 5000 no esté ocupado por otra aplicación

### El navegador no se abre automáticamente
- Abre manualmente tu navegador
- Ve a la dirección: `http://127.0.0.1:5000`

### Error de "Puerto ocupado"
- Cierra otras aplicaciones que puedan usar el puerto 5000
- Reinicia tu computadora si es necesario

## 📋 Información Técnica

- **Framework**: Flask 2.3.3
- **Base de datos**: SQLite (archivo `instance/hotel.db`)
- **Puerto**: 5000 (localhost)
- **Navegador**: Se abre automáticamente
- **Plataforma**: Windows 10/11 (64-bit)

## 📞 Notas Importantes

- El ejecutable es completamente portable
- No modifica el registro de Windows
- La base de datos se guarda en la carpeta `instance/`
- Todos los datos se conservan entre sesiones
- No requiere instalación adicional

## 🎯 Uso Recomendado

1. **Primera ejecución**: Crea algunos hoteles de prueba
2. **Agrega habitaciones**: Define tipos y precios
3. **Registra clientes**: Para hacer reservas
4. **Haz reservas**: Prueba el sistema completo
5. **Explora funciones**: Búsqueda, filtros, evaluaciones

---
**Desarrollado con PyInstaller y Flask**
*Sistema completo de gestión hotelera en un solo archivo ejecutable*
