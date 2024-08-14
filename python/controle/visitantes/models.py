from django.db import models

class Visitante(models.Model):
    usuario = models.OneToOneField(
        "usuarios.Usuario",
        verbose_name = "Usuário",
        on_delete = models.PROTECT
    )

    nome_completo = models.CharField(
        verbose_name = "Nome Completo",
        max_length = 100,
    )

    cpf = models.CharField(
        verbose_name = "CPF",
        max_length = 11,
    )

    data_nascimento = models.DateField(
        verbose_name = "Data de Nascimento",
        auto_now = False,
        auto_now_add = False,
    )

    numero_da_casa = models.CharField(
        verbose_name = "Número da Casa",
        max_length = 11,
    )

    placa_do_carro = models.CharField(
        verbose_name = "Placa do Carro",
        max_length = 11,
    )
    
    numero_da_casa = models.CharField(
        verbose_name = "Número da Casa",
        max_length = 11,
    )

    hora_da_chegada = models.TimeField(
        verbose_name = "Hora da Chegada",
        max_length = 11,
        auto_now_add=False,
    )
    
    hora_da_saida = models.TimeField(
        verbose_name = "Hora da Saída",
        max_length = 11,
        auto_now_add=False,
    )

    hora_da_autorizacao = models.TimeField(
        verbose_name = "Hora da Autorização",
        max_length = 11,
        auto_now_add=False,
    )

    nome_do_morador = models.CharField(
        verbose_name = "Nome do Morador",
        max_length = 100,
    )

    porteiro_que_autorizou = models.CharField(
        verbose_name = "Porteiro que Autorizou",
        max_length = 100,
    )

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"


