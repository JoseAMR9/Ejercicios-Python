'''
Check if permisos_usuario is a subset of permisos_admin using .issubset().
Add the permission "exportar" to the admin role.
Create a set permisos_nuevo_rol with the permissions {"leer", "exportar", "reportes"} and find which permissions this role has that the normal user does not.
Clear the user's permissions using .clear() and display the result.
'''

permisos_admin = {"leer", "escribir", "eliminar", "configurar"}
permisos_usuario = {"leer", "escribir"}

if permisos_usuario.issubset(permisos_admin): #a.issubset(b): devuelve true si -> a contiene algo de b
    print("Is subset")
else:
    print("Is not subset")

permisos_admin.add("exportar")

permisos_nuevo_rol = {"leer", "exportar", "reportes"}

print(permisos_nuevo_rol.difference(permisos_usuario))

permisos_usuario.clear()
print(permisos_usuario)