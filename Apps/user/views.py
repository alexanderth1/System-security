from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# 1. PANTALLA DE LOGIN
def vista_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        # Captura el rol seleccionado en la tarjeta de perfiles
        rol_seleccionado = request.POST.get('user_role', 'Usuario')
        request.session['user_role'] = rol_seleccionado
        return redirect('dashboard')

    return render(request, 'user/login.html')

# 2. PANTALLA DE CREAR USUARIO (REGISTRO)
def usuario_crear(request):
    # Si el usuario hace clic en el botón "Registrar Usuario" (envía el formulario)
    if request.method == 'POST':
        # Aquí en el futuro programaremos el guardado real en la base de datos.
        # Por ahora, simulamos el registro exitoso y lo mandamos al login:
        return redirect('login')
    return render(request, 'user/usuario_crear.html')

# 3. PANTALLA DEL DASHBOARD (PANEL PRINCIPAL MULTIPERFIL)
# @login_required
def dashboard(request):
    # Lee el rol guardado para decidir qué herramientas mostrar en el HTML
    rol_actual = request.session.get('user_role', 'Administrador')
    return render(request, 'user/dashboard.html', {'rol': rol_actual})

# FUNCIÓN DE APOYO: Para salir del sistema de forma segura
def cerrar_sesion(request):
    logout(request)
    return redirect('login')

#@login_required
def usuario_editar(request):
    if request.method == 'POST':
        # Aquí en el futuro programaremos el UPDATE a la base de datos
        # Por ahora, simulamos que guardó y lo regresamos al panel:
        return redirect('dashboard')

    # Si solo entra a ver, le dibujamos la pantalla
    return render(request, 'user/usuario_editar.html')

#@login_required
def registrar_supervisor(request):
    if request.method == 'POST':
        # Simulación de guardado
        return redirect('dashboard')
    return render(request, 'user/registrar_supervisor.html')