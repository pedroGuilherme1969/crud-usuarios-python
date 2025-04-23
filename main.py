usuarios = []

def criar_usuario(nome, email, senha, cpf):
    usuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'cpf': cpf
    }
    usuarios.append(usuario)

def listar_usuarios():
    return usuarios

def buscar_usuario_por_cpf(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def deletar_usuario(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)
            return True
    return False
