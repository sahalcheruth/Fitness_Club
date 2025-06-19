from django.db import models
from django.utils import timezone

# =============================
#  Yoga Models
# =============================

class YogaClass(models.Model):
    title = models.CharField(max_length=100, default="Yoga")
    instructor = models.CharField(max_length=100)
    start_time = models.DateTimeField()  # Combined date and time
    total_vacancy = models.PositiveIntegerField()

    # Method to get available slots
    def available_slots(self):
        return self.total_vacancy - self.bookings.count()

    def __str__(self):
        return f"{self.title} with {self.instructor} on {self.start_time.strftime('%Y-%m-%d %H:%M')}"


class YogaBooking(models.Model):
    yoga_class = models.ForeignKey(YogaClass, related_name='bookings', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.yoga_class.title}"


# =============================
#  Zumba Models
# =============================

class ZumbaClass(models.Model):
    title = models.CharField(max_length=100, default="Zumba")
    instructor = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    total_vacancy = models.PositiveIntegerField()

    def available_slots(self):
        return self.total_vacancy - self.bookings.count()

    def __str__(self):
        return f"{self.title} with {self.instructor} on {self.start_time.strftime('%Y-%m-%d %H:%M')}"


class ZumbaBooking(models.Model):
    zumba_class = models.ForeignKey(ZumbaClass, related_name='bookings', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.zumba_class.title}"


# =============================
#  HIIT Models
# =============================

class HIITClass(models.Model):
    title = models.CharField(max_length=100, default="HIIT")
    instructor = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    total_vacancy = models.PositiveIntegerField()

    def available_slots(self):
        return self.total_vacancy - self.bookings.count()

    def __str__(self):
        return f"{self.title} with {self.instructor} on {self.start_time.strftime('%Y-%m-%d %H:%M')}"


class HIITBooking(models.Model):
    hiit_class = models.ForeignKey(HIITClass, related_name='bookings', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.hiit_class.title}"
