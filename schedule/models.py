from django.db import models


class Document(models.Model):
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Clinic(models.Model):
    name = models.CharField(verbose_name='Название клиники', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиника"
        verbose_name_plural = "Клиники"


class Doctor(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, verbose_name='Клиника')
    efio = models.CharField(verbose_name='Имя врача', max_length=150)
    espec = models.CharField(verbose_name='Специальность врача', max_length=30, blank=True, null=True)

    def __str__(self):
        return self.efio

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"


class Cell(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, editable=True, verbose_name='Доктор')
    date = models.CharField(verbose_name='Дата ячейки', max_length=10)
    time_start = models.CharField(verbose_name='Время начала ячейки', max_length=5)
    time_end = models.CharField(verbose_name='Время окончания ячейки', max_length=5)
    free = models.BooleanField(verbose_name='Ячейка свободна', default=True)

    def __str__(self):
        return self.date + ' ' + self.time_start

    class Meta:
        verbose_name = "Ячейкa"
        verbose_name_plural = "Ячейки"



