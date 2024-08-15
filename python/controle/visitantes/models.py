from django.db import models

class Visitante(models.Model):
    nome_completo = models.CharField(
        verbose_name = "Nome Completo",
        max_length = 150,
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

    hora_da_chegada = models.DateTimeField(
        verbose_name = "Hora de chegada na portaria",
        auto_now_add=True,
    )
    
    hora_da_saida = models.DateTimeField(
        verbose_name = "Hora de saída do condomínio",
        auto_now_add=False,
        blank=True,
        null=True
    )

    hora_da_autorizacao = models.DateTimeField(
        verbose_name = "Hora de autorização de entrada",
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

    registrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name="Visitante"
        verbose_name_plural="Visitantes"
        db_table="visitante"

    def __str__(self):
        return self.nome_completo
