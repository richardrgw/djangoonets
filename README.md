# djangoonets
aplicacion prueba python djnago

despliguiegue aplicacion
	instalar entorno virtual
		{carpetaProyecto}>virtualenv venv
	activar entorno virtual
		{carpetaProyecto}>.\venv\Scripts\activate
	instalar dependencias
		{carpetaProyecto}>pip install -r requirements.txt
	migramos la base de datos
		{carpetaProyecto}>python manage.py migrate
	desplegamos aplicacion
		{carpetaProyecto}>python manage.py runserver 3000 