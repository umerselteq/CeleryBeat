from django.db import models
from django_softdelete.models import SoftDeleteModel


class BaseModel(SoftDeleteModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Candidate(BaseModel):
    parentId = models.ForeignKey('Candidate', related_name='childCandidates', null=True, blank=True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100, null=False, blank=False)
    lastName = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return f"candidate {self.id} - {self.firstName}"


class CandidateStatus(BaseModel):
    STATUS_CHOICES = [("review pending", "Review Pending"), ("registered", "Registered"), ("completed", "Completed"),
                      ("pending", "Pending"), ("suspended", "Suspended"), ("applied", "Applied"),
                      ("flow assigned", "Flow Assigned")]
    candidateId = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='status')
    status = models.CharField(choices=STATUS_CHOICES, default="registered", max_length=20)