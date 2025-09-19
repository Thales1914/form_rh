from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

DESTINATARIOS = settings.EMAIL_DESTINATARIOS or [
    "rh@omegadistribuidora.com.br",
]

def _enviar_email(**kwargs):
    try:
        send_mail(**kwargs)
        logger.info(f"E-mail enviado com sucesso: {kwargs.get('subject')}")
    except Exception as e:
        logger.error(f"Erro ao enviar e-mail: {e}")

def notificar_admissao(obj, usuario):
    assunto = "📥 Nova admissão registrada"
    mensagem = (
        f"Nome: {obj.nome}\n"
        f"Código RCA: {obj.codigo}\n"
        f"Data de Admissão: {obj.data_admissao.strftime('%d/%m/%Y') if obj.data_admissao else '-'}\n"
        f"Cargo: {obj.cargo or '-'}\n"
        f"Supervisor Responsável: {obj.supervisor_responsavel or '-'}\n"
        f"Registrado por: {usuario.get_username()}"
    )
    _enviar_email(
        subject=assunto,
        message=mensagem,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=DESTINATARIOS,
        fail_silently=False,
    )

def notificar_desligamento(obj, usuario):
    assunto = "📤 Novo desligamento registrado"
    mensagem = (
        f"Nome: {obj.nome}\n"
        f"Código: {obj.codigo}\n"
        f"Área: {obj.area_atuacao or '-'}\n"
        f"Data de Demissão: {obj.demissao.strftime('%d/%m/%Y') if obj.demissao else '-'}\n"
        f"Registrado por: {usuario.get_username()}"
    )
    _enviar_email(
        subject=assunto,
        message=mensagem,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=DESTINATARIOS,
        fail_silently=False,
    )
