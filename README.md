# M10_UF2

1. Descargamos odoo en una carpeta:
   **git clone https://github.com/odoo/odoo.git**
2. Si Python 3 ya está instalado, asegúrese de que sea la versión 3.7 o más, ya que las versiones previas no son compatibles con Odoo:
   **python --version**
   **pip --version**
3. - Instalamos **pgAdmin.**

   * Abrir  **pgAdmin** .
   * Haga doble clic en el servidor para crear una conexión.
   * Seleccione **Objeto ‣ Crear ‣ Rol de Inicio se sesión/Grupo**.
   * Ingrese el nombre de usuario en el campo de **Nombre de la función** (por ejemplo, **Pau**)
   * Abra la pestaña **Definición** e ingrese la contraseña (por ejemplo, **Pau** y después haga clic en  **Guardar** .
   * Abra la pestaña de **Privilegios** y cambie **¿Puede iniciar sesión?** **SI** y **¿Crear una base de datos?** **SI**
4. Antes de instalar las dependencias, debe descargar e instalar Herramientas de creación para Visual Studio. Cuando se lo pida, seleccione herramientas de creación C++ en la pestaña de Carga de trabajo e instálelo.Navegue a la ruta de su instalación de Odoo Community (CommunityPath) y ejecute **pip** en el campo de requisitos en una terminal  **con privilegios de administrador** :

   **cd \CommunityPath**

   **pip install setuptools wheels**

   **pip install -r requirements.txt**
5. Para ejecutar el servidor Odoo seria:

   **cd \CommunityPath**

   **python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb**
