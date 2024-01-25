from rest_framework  import serializers


from leaveRequest.models import LeaveRequest

class LeaveRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeaveRequest
        fields = ('leaveRequestId', 'userId','startDate','endDate','reason','status','rejectedReason','remainingDay')