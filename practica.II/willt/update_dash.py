import os

file_path = r"c:\Users\BORJA\Documents\GitHub\practica.II\willt\core\templates\dashboard.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

import re

nav_replacement = """<nav>
                    <a href="#panel-persona" class="active"><i class="fa-solid fa-id-card"></i> Personas</a>
                    <a href="#panel-icono"><i class="fa-solid fa-image"></i> Iconos</a>
                    <a href="#panel-rol"><i class="fa-solid fa-user-shield"></i> Roles</a>
                    <a href="#panel-perfil"><i class="fa-solid fa-users"></i> Perfiles</a>
                    <a href="#panel-rolpermiso"><i class="fa-solid fa-key"></i> Permisos de Rol</a>
                </nav>"""
content = re.sub(r'<nav>.*?</nav>', nav_replacement, content, flags=re.DOTALL)

panels_replacement = """<!-- Tabla Persona -->
                <div class="crud-panel" id="panel-persona">
                    <div class="crud-header">
                        <h2><i class="fa-solid fa-id-card"></i> Personas</h2>
                        <button class="btn-new" data-bs-toggle="modal" data-bs-target="#modalPersona"><i class="fa-solid fa-plus"></i> Nueva Persona</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table-dark-custom">
                            <thead><tr><th>ID</th><th>DNI</th><th>Nombres</th><th>Acciones</th></tr></thead>
                            <tbody>
                                <tr>
                                    <td>1</td><td>72834912</td><td>Juan Perez</td>
                                    <td>
                                        <div class="action-btns">
                                            <button class="btn-icon btn-edit" title="Editar" data-bs-toggle="modal" data-bs-target="#modalPersona"><i class="fa-solid fa-pen"></i></button>
                                            <button class="btn-icon btn-delete" title="Eliminar" data-bs-toggle="modal" data-bs-target="#modalEliminar"><i class="fa-solid fa-trash"></i></button>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Tabla Icono -->
                <div class="crud-panel" id="panel-icono">
                    <div class="crud-header">
                        <h2><i class="fa-solid fa-image"></i> Iconos</h2>
                        <button class="btn-new" data-bs-toggle="modal" data-bs-target="#modalIcono"><i class="fa-solid fa-plus"></i> Nuevo Icono</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table-dark-custom">
                            <thead><tr><th>ID</th><th>Nombre</th><th>Recurso</th><th>Acciones</th></tr></thead>
                            <tbody>
                                <tr>
                                    <td>1</td><td>Icono Admin</td><td><span class="text-secondary">/media/iconos/admin.png</span></td>
                                    <td>
                                        <div class="action-btns">
                                            <button class="btn-icon btn-edit" title="Editar" data-bs-toggle="modal" data-bs-target="#modalIcono"><i class="fa-solid fa-pen"></i></button>
                                            <button class="btn-icon btn-delete" title="Eliminar" data-bs-toggle="modal" data-bs-target="#modalEliminar"><i class="fa-solid fa-trash"></i></button>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Tabla Rol -->
                <div class="crud-panel" id="panel-rol">
                    <div class="crud-header">
                        <h2><i class="fa-solid fa-user-shield"></i> Roles</h2>
                        <button class="btn-new" data-bs-toggle="modal" data-bs-target="#modalRol"><i class="fa-solid fa-plus"></i> Nuevo Rol</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table-dark-custom">
                            <thead><tr><th>ID</th><th>Nivel de Acceso</th><th>Etiqueta</th><th>Icono</th><th>Acciones</th></tr></thead>
                            <tbody>
                                <tr>
                                    <td>1</td><td>Administrador</td><td>Admin General</td><td>Icono Admin</td>
                                    <td>
                                        <div class="action-btns">
                                            <button class="btn-icon btn-edit" title="Editar" data-bs-toggle="modal" data-bs-target="#modalRol"><i class="fa-solid fa-pen"></i></button>
                                            <button class="btn-icon btn-delete" title="Eliminar" data-bs-toggle="modal" data-bs-target="#modalEliminar"><i class="fa-solid fa-trash"></i></button>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Tabla Perfil -->
                <div class="crud-panel" id="panel-perfil">
                    <div class="crud-header">
                        <h2><i class="fa-solid fa-users"></i> Perfiles</h2>
                        <button class="btn-new" data-bs-toggle="modal" data-bs-target="#modalPerfil"><i class="fa-solid fa-plus"></i> Nuevo Perfil</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table-dark-custom">
                            <thead><tr><th>ID</th><th>Usuario (Auth)</th><th>Persona</th><th>Rol</th><th>Acciones</th></tr></thead>
                            <tbody>
                                <tr>
                                    <td>1</td><td>admin_user</td><td>Juan Perez</td><td>Administrador</td>
                                    <td>
                                        <div class="action-btns">
                                            <button class="btn-icon btn-edit" title="Editar" data-bs-toggle="modal" data-bs-target="#modalPerfil"><i class="fa-solid fa-pen"></i></button>
                                            <button class="btn-icon btn-delete" title="Eliminar" data-bs-toggle="modal" data-bs-target="#modalEliminar"><i class="fa-solid fa-trash"></i></button>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Tabla RolPermiso -->
                <div class="crud-panel" id="panel-rolpermiso">
                    <div class="crud-header">
                        <h2><i class="fa-solid fa-key"></i> Permisos de Rol</h2>
                        <button class="btn-new" data-bs-toggle="modal" data-bs-target="#modalRolPermiso"><i class="fa-solid fa-plus"></i> Asignar Permiso</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table-dark-custom">
                            <thead><tr><th>ID</th><th>Rol</th><th>Permiso (Auth)</th><th>Acciones</th></tr></thead>
                            <tbody>
                                <tr>
                                    <td>1</td><td>Administrador</td><td>Can view user</td>
                                    <td>
                                        <div class="action-btns">
                                            <button class="btn-icon btn-edit" title="Editar" data-bs-toggle="modal" data-bs-target="#modalRolPermiso"><i class="fa-solid fa-pen"></i></button>
                                            <button class="btn-icon btn-delete" title="Eliminar" data-bs-toggle="modal" data-bs-target="#modalEliminar"><i class="fa-solid fa-trash"></i></button>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
"""

idx_start = content.find("<!-- Tabla Categoria -->")
idx_end = content.find("<!-- Dashboard Footer -->")
if idx_start != -1 and idx_end != -1:
    content = content[:idx_start] + panels_replacement + "\n            </div>\n\n            " + content[idx_end:]

modals_replacement = """<!-- Modales CRUD -->

    <!-- Modal Persona -->
    <div class="modal fade" id="modalPersona" tabindex="-1" data-bs-theme="dark">
        <div class="modal-dialog">
            <div class="modal-content" style="background-color: var(--bg-panel); color: var(--text-primary); border: 1px solid var(--border-color);">
                <div class="modal-header border-0"><h5 class="modal-title">Gestión de Persona</h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div>
                <div class="modal-body">
                    <form>
                        <div class="mb-3"><label class="form-label">DNI</label><input type="text" name="dni" class="form-control" style="background-color: var(--bg-body); color: white; border-color: var(--border-color);"></div>
                        <div class="mb-3"><label class="form-label">Nombres</label><input type="text" name="nombres" class="form-control" style="background-color: var(--bg-body); color: white; border-color: var(--border-color);"></div>
                    </form>
                </div>
                <div class="modal-footer border-0">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                    <button type="button" class="btn btn-new" style="background-color: var(--accent-green); color: black;">Guardar Persona</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal Icono -->
    <div class="modal fade" id="modalIcono" tabindex="-1" data-bs-theme="dark">
        <div class="modal-dialog">
            <div class="modal-content" style="background-color: var(--bg-panel); color: var(--text-primary); border: 1px solid var(--border-color);">
                <div class="modal-header border-0"><h5 class="modal-title">Gestión de Icono</h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div>
                <div class="modal-body">
                    <form>
                        <div class="mb-3"><label class="form-label">Nombre</label><input type="text" name="nombre" class="form-control" style="background-color: var(--bg-body); color: white; border-color: var(--border-color);"></div>
                        <div class="mb-3"><label class="form-label">Recurso (Archivo)</label><input type="file" name="recurso" class="form-control" style="background-color: var(--bg-body); color: white; border-color: var(--border-color);"></div>
                    </form>
                </div>
                <div class="modal-footer border-0">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                    <button type="button" class="btn btn-new" style="background-color: var(--accent-green); color: black;">Guardar Icono</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal Rol -->
    <div class="modal fade" id="modalRol" tabindex="-1" data-bs-theme="dark">
        <div class="modal-dialog">
            <div class="modal-content" style="background-color: var(--bg-panel); color: var(--text-primary); border: 1px solid var(--border-color);">
                <div class="modal-header border-0"><h5 class="modal-title">Gestión de Rol</h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div>
                <div class="modal-body">
                    <form>
                        <div class="mb-3"><label class="form-label">Nivel de Acceso</label><input type="text" name="nivel_acceso" class="form-control" style="background-color: var(--bg-body); color: white; border-color: var(--border-color);"></div>
                        <div class="mb-3"><label class="form-label">Etiqueta</label><input type="text" name="etiqueta" class="form-control" style="background-color: var(--bg-body); color: white; border-color: var(--border-color);"></div>
                        <div class="mb-3"><label class="form-label">Icono</label><select name="icono" class="form-select" style="background-color: var(--bg-body); color: white; border-color: var(--border-color);"><option value="">Seleccione Icono</option></select></div>
                    </form>
                </div>
                <div class="modal-footer border-0">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                    <button type="button" class="btn btn-new" style="background-color: var(--accent-green); color: black;">Guardar Rol</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal Perfil -->
    <div class="modal fade" id="modalPerfil" tabindex="-1" data-bs-theme="dark">
        <div class="modal-dialog">
            <div class="modal-content" style="background-color: var(--bg-panel); color: var(--text-primary); border: 1px solid var(--border-color);">
                <div class="modal-header border-0"><h5 class="modal-title">Gestión de Perfil</h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div>
                <div class="modal-body">
                    <form>
                        <div class="mb-3"><label class="form-label">Usuario (Auth)</label><select name="user" class="form-select" style="background-color: var(--bg-body); color: white; border-color: var(--border-color);"><option value="">Seleccione Usuario</option></select></div>
                        <div class="mb-3"><label class="form-label">Persona</label><select name="persona" class="form-select" style="background-color: var(--bg-body); color: white; border-color: var(--border-color);"><option value="">Seleccione Persona</option></select></div>
                        <div class="mb-3"><label class="form-label">Rol</label><select name="rol" class="form-select" style="background-color: var(--bg-body); color: white; border-color: var(--border-color);"><option value="">Seleccione Rol</option></select></div>
                    </form>
                </div>
                <div class="modal-footer border-0">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                    <button type="button" class="btn btn-new" style="background-color: var(--accent-green); color: black;">Guardar Perfil</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal RolPermiso -->
    <div class="modal fade" id="modalRolPermiso" tabindex="-1" data-bs-theme="dark">
        <div class="modal-dialog">
            <div class="modal-content" style="background-color: var(--bg-panel); color: var(--text-primary); border: 1px solid var(--border-color);">
                <div class="modal-header border-0"><h5 class="modal-title">Gestión de Permiso de Rol</h5><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div>
                <div class="modal-body">
                    <form>
                        <div class="mb-3"><label class="form-label">Rol</label><select name="rol" class="form-select" style="background-color: var(--bg-body); color: white; border-color: var(--border-color);"><option value="">Seleccione Rol</option></select></div>
                        <div class="mb-3"><label class="form-label">Permiso</label><select name="permiso" class="form-select" style="background-color: var(--bg-body); color: white; border-color: var(--border-color);"><option value="">Seleccione Permiso</option></select></div>
                    </form>
                </div>
                <div class="modal-footer border-0">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                    <button type="button" class="btn btn-new" style="background-color: var(--accent-green); color: black;">Guardar Permiso</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal Eliminar -->
    <div class="modal fade" id="modalEliminar" tabindex="-1" data-bs-theme="dark">
        <div class="modal-dialog modal-sm modal-dialog-centered">
            <div class="modal-content" style="background-color: var(--bg-panel); color: var(--text-primary); border: 1px solid var(--border-color);">
                <div class="modal-body text-center py-4">
                    <i class="fa-solid fa-circle-exclamation text-danger mb-3" style="font-size: 3rem;"></i>
                    <h5 class="mb-2">¿Estás seguro?</h5>
                    <p class="text-secondary mb-4">Esta acción no se puede deshacer.</p>
                    <div class="d-flex justify-content-center gap-2">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Sí, Eliminar</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

idx_modals_start = content.find("<!-- Modales CRUD -->")
idx_script = content.find("<script", idx_modals_start)

if idx_modals_start != -1 and idx_script != -1:
    content = content[:idx_modals_start] + modals_replacement + "\n    " + content[idx_script:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("done")
