from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class ECoordenador(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.perfil == "coordenador"
        )

class EProfessor(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.perfil == "professor"
        )

class EAluno(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.perfil == "aluno"
        )


class ECoordenadorOuProfessor(BasePermission):

    def has_permission(self, request, view):
        
        return ( 
            request.user.is_authenticated
            and request.user.perfil in [
                "coordenador",
                "professor"
            ]
        )

class EAlunoSomenteLeitura(BasePermission):

    def has_permission(self, request, view):
        
        return (
            request.user.is_authenticated
            and request.user.perfil == "aluno"
            and request.method in SAFE_METHODS
        )

class NotaPermissao(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        if request.user.perfil == "coordenador":
            return True

        if request.user.perfil == "professor":
            return True

        if (
            request.user.perfil == "aluno"
            and request.method in SAFE_METHODS
        ):
            return True

        return False