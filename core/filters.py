import django_filters


class AlunoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        field_name="nome",
        lookup_expr="icontains",
        label="Nome (parcial, sem distinção de maiúsculas)",
    )

    matricula = django_filters.CharFilter(
        field_name="matricula",
        lookup_expr="exact",
        label="Matrícula (exata)",
    )

    email = django_filters.CharFilter(
        field_name="email",
        lookup_expr="icontains",
        label="Email (parcial)",
    )

    class Meta:
        from apps.alunos.models import Aluno
        model = Aluno
        fields = ["nome", "matricula", "email"]


class ProfessorFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        field_name="nome",
        lookup_expr="icontains",
    )

    especialidade = django_filters.CharFilter(
        field_name="especialidade",
        lookup_expr="icontains",
        label="Especialidade (parcial)",
    )

    class Meta:
        from apps.professores.models import Professor
        model = Professor
        fields = ["nome", "especialidade"]


class DisciplinaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        field_name="nome",
        lookup_expr="icontains",
    )

    class Meta:
        from apps.disciplinas.models import Disciplina
        model = Disciplina
        fields = ["nome"]

class TurmaFilter(django_filters.FilterSet):
    professor = django_filters.UUIDFilter(
        field_name="professor__id",
        label="UUID do Professor",
    )

    disciplina = django_filters.UUIDFilter(
        field_name="disciplina__id",
        label="UUID da Disciplina",
    )

    ano_letivo = django_filters.NumberFilter(
        field_name="ano_letivo",
        lookup_expr="exact",
        label="Ano Letivo (ex: 2024)",
    )

    class Meta:
        from apps.turmas.models import Turma
        model = Turma
        fields = ["professor", "disciplina", "ano_letivo"]


class AvaliacaoFilter(django_filters.FilterSet):
    turma = django_filters.UUIDFilter(
        field_name="turma__id",
        label="UUID da Turma",
    )

    data = django_filters.DateFilter(
        field_name="data",
        lookup_expr="exact",
        label="Data exata (YYYY-MM-DD)",
    )

    data_inicio = django_filters.DateFilter(
        field_name="data",
        lookup_expr="gte",
        label="Data a partir de (YYYY-MM-DD)",
    )

    data_fim = django_filters.DateFilter(
        field_name="data",
        lookup_expr="lte",
        label="Data até (YYYY-MM-DD)",
    )

    class Meta:
        from apps.avaliacoes.models import Avaliacao
        model = Avaliacao
        fields = ["turma", "data"]

class NotaFilter(django_filters.FilterSet):
    aluno = django_filters.UUIDFilter(
        field_name="aluno__id",
        label="UUID do Aluno",
    )

    avaliacao = django_filters.UUIDFilter(
        field_name="avaliacao__id",
        label="UUID da Avaliação",
    )

    class Meta:
        from apps.notas.models import Nota
        model = Nota
        fields = ["aluno", "avaliacao"]


class FrequenciaFilter(django_filters.FilterSet):
    aluno = django_filters.UUIDFilter(
        field_name="aluno__id",
        label="UUID do Aluno",
    )

    turma = django_filters.UUIDFilter(
        field_name="turma__id",
        label="UUID da Turma",
    )

    data = django_filters.DateFilter(
        field_name="data",
        lookup_expr="exact",
        label="Data exata (YYYY-MM-DD)",
    )

    data_inicio = django_filters.DateFilter(
        field_name="data",
        lookup_expr="gte",
        label="Data a partir de (YYYY-MM-DD)",
    )

    data_fim = django_filters.DateFilter(
        field_name="data",
        lookup_expr="lte",
        label="Data até (YYYY-MM-DD)",
    )

    class Meta:
        from apps.frequencias.models import Frequencia
        model = Frequencia
        fields = ["aluno", "turma", "data"]
