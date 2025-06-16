from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def usuarios(request):
    lista_usuarios = [
        {'nome': 'Ana', 'matricula': '001', 'idade': 20, 'cidade': 'riachuelo'},
        {'nome': 'Bruno', 'matricula': '002', 'idade': 22, 'cidade': 'boa saúde'},
        {'nome': 'bruno', 'matricula': '003', 'idade': 25, 'cidade': 'serra caiada'},
        {'nome': 'felipe', 'matricula': '004', 'idade': 23, 'cidade': 'bom jesus'},
        {'nome': 'Elisa', 'matricula': '005', 'idade': 21, 'cidade': 'macaíba'},
    ]
    return render(request, 'usuarios.html', {'usuarios': lista_usuarios})