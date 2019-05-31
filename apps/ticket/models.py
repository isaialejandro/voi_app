import datetime

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

from apps.applicant.models import Applicant
from apps.application.models import Application


now = datetime.datetime.now()


REGISTRATION = 'registration'
UNSUBSCRIBE = 'unsubscribe'
TYPE_REQUEST = (
    (REGISTRATION, 'Registration'),
    (UNSUBSCRIBE, 'Unsubscribe'),
)


class Ticket(models.Model):

    OPEN = 'open'
    PENDING = 'pending'
    IN_PROGRESS = 'in progress'
    ASSIGNED = 'assigned'
    APPROVAL_PROCCESS_PROVIDER = 'provider approval proccess'
    CLOSED = 'closed'
    STATUS = (
        (OPEN, 'Open'),
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (ASSIGNED, 'Assigned'),
        (APPROVAL_PROCCESS_PROVIDER, 'Provider Approval Proccess'),
        (CLOSED, 'Closed'),
    )

    LOW = 'low'
    MID = 'mid'
    HIGH = 'high'
    PRIORITY = (
        (LOW, 'Low'),
        (MID, 'Mid'),
        (HIGH, 'High'),
    )

    YES = 'yes'
    NO = 'no'
    APPROVE = (
        (YES, 'Yes'),
        (NO, 'No'),
    )

    APPROVAL = 'approval'
    APPROVAL_OWNER = (
        (APPROVAL, 'Approval'),
    )

    ITEM = 'item'
    ITEM_TYPE = (
        (ITEM, 'Item'),
    )

    title = models.CharField(max_length=50, blank=True)
    folio_number = models.CharField(max_length=20, blank=True)
    priority = models.CharField(max_length=15, choices=PRIORITY, default=LOW)
    status = models.CharField(max_length=50, choices=STATUS, default=OPEN)
    registry_date = models.DateTimeField(auto_now_add=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.DO_NOTHING, default='')
    application = models.ForeignKey(Application, on_delete=models.DO_NOTHING, default='')
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_assigned", blank=False)

    request_type = models.CharField(max_length=25, choices=TYPE_REQUEST, default=REGISTRATION)
    beneficiary_name = models.CharField(max_length=50, blank=True)
    beneficiary_last_name = models.CharField(max_length=50, blank=True)
    approval_owner = models.CharField(max_length=15, choices=APPROVAL_OWNER, default=APPROVAL)
    approval_executor = models.CharField(max_length=50, choices=APPROVE, default=YES)
    approve = models.CharField(max_length=3, choices=APPROVE, default=YES)
    created_by = models.CharField(max_length=50, blank=True)
    item_type = models.CharField(max_length=10,choices=ITEM_TYPE, default=ITEM)
    path = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=450, blank=True, null=True)
    solution_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    close_comment = models.TextField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')

    def __str__(self):
        return self.folio_number + '  |  ' + '{}'.format(self.status.upper()) + '  |  ' + '{}'.format(self.application)

    class Meta:

        permissions = (
            ('view_ticket_list', 'Can view the tickets list'),
            ('create_ticket', 'Can create new ticket'),
            ('update_ticket', 'Can update current ticket'),
            ('close_ticket', 'Can close current ticket'),
            ('view_ticket_detail', 'Can visualize current ticket detail'),
            ('disable_ticket', 'Can disable ticket'),
        )


class TicketHistory(models.Model):

    """
    History for save each ticket change done for a different user and show a ticket detail when
    one different user take the current open/pending/assigned/in_progress ticket.
    """

    ticket = models.ForeignKey('Ticket', on_delete=models.DO_NOTHING, default='')
    summary = models.TextField(max_length=450)
    registry_date = models.DateTimeField(auto_now=now)
    update = models.BooleanField(default=True)     #Bandera que indica si el registro se actualizó o no.
    #not_finished_type = models.BooleanField(default=False)  #Indica si no se ha finalizado en el registro actual guardado. -
    #reemplazado por el de abajo
    finished = models.BooleanField(default=False)  #Indica si no se ha finalizado en el registro actual guardado.
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')
