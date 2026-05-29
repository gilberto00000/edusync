from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class ECoordenador(BasePermission):

    def has_permission(self, request, view):

        print(request.user)
        print(request.user.perfil)

        return (
            request.user.is_authenticated
            and request.user.perfil == "COORDENADOR"
        )

class EProfessor(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.perfil == "PROFESSOR"
        )

class EAluno(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.perfil == "ALUNO"
        )


class ECoordenadorOuProfessor(BasePermission):

    def has_permission(self, request, view):
        
        return ( 
            request.user.is_authenticated
            and request.user.perfil in [
                "COORDENADOR",
                "PROFESSOR"
            ]
        )

class EAlunoSomenteLeitura(BasePermission):

    def has_permission(self, request, view):
        
        return (
            request.user.is_authenticated
            and request.user.perfil == "ALUNO"
            and request.method in SAFE_METHODS
        )

class NotaPermissao(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        if request.user.perfil == "COORDENADOR":
            return True

        if request.user.perfil == "PROFESSOR":
            return True

        if (
            request.user.perfil == "ALUNO"
            and request.method in SAFE_METHODS
        ):
            return True

        return False