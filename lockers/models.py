from django.db import models


class Locker(models.Model):
    owner = models.ForeignKey('tangent.Member', blank=True, null=True)

    locker_number = models.IntegerField(unique=True, primary_key=True)
    current_combo = models.CharField(max_length=6)
    combo_number = models.IntegerField()

    combo0 = models.CharField(max_length=6)
    combo1 = models.CharField(max_length=6)
    combo2 = models.CharField(max_length=6)
    combo3 = models.CharField(max_length=6)
    combo4 = models.CharField(max_length=6)

    def cycle_combo(self):
        self.current_combo += 1
        num = self.combo_number
        self.set_combo(num)

    def set_combo(self, num):
        if num == 0:
            self.combo_number = self.combo0
        elif num == 1:
            self.combo_number = self.combo1
        elif num == 2:
            self.combo_number = self.combo2
        elif num == 3:
            self.combo_number = self.combo3
        else:  # num == 4 or more
            self.combo_number = self.combo4

    def __str__(self):
        owner = self.owner.__str__() if self.owner else ""
        return str(self.locker_number) + "  " + owner