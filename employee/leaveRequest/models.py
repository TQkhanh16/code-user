from django.db import models

# Create your models here.
class LeaveRequest(models.Model):
    leaveRequestId = models.CharField(max_length=255,default = None)
    userId = models.CharField(max_length=255,default = None)
    startDate = models.DateTimeField(default = None)
    endDate = models.DateTimeField(default = None)
    reason = models.CharField(max_length=255,default = None)
    status = models.CharField(max_length=255,default = None)
    rejectedReason = models.CharField(max_length=255,default = None)
    remainingDay = models.CharField(max_length=255,default = None)
    def _str_(self):
        return self.leaveRequestId