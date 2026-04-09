agenda = {
    "Jose": {"Phone": "123456", "Mail": "jose@mail.com"},
    "Pedro" : {"Phone" : "334455", "Mail" : "pedrito@mail.com"},
    "Maria" : {"Phone" : "998647", "Mail" : "mariay@mail.com"}
}

print(agenda["Pedro"]["Mail"])

agenda["Maria"]["Phone"] = "123123"
print(agenda["Maria"]["Phone"])

del agenda["Jose"]
print(agenda)

for nombre, datos in agenda.items():
    print(f"{nombre} → Tel: {datos['Phone']} | Mail: {datos['Mail']}")