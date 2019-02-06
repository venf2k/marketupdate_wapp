from django.db import models

# Create your models here.
class Update(models.Model):
    notes_text = models.CharField(max_length=200, null=True)
    pub_date = models.DateField()
    pub_hour = models.TimeField()
   
    class Meta:
    	ordering = ['-pub_date', '-pub_hour']
   
    def __str__(self):
    	return str(self.pub_date) + '@' + str(self.pub_hour)

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200, null=True)
    update = models.ForeignKey(Update, on_delete=models.CASCADE, null=True,)
    
    class Meta:
    	ordering = ['pk']

    def __str__(self):
    	return str(self.description) + '@' + str(self.update)


class Symbol(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, )

    class Meta:
        ordering = ['pk']

    def __str__(self):
    	return str(self.description) + '@' + str(self.category)

class Value(models.Model):
    UNITS_CHOICES = (
        ('1', '%'),
        ('2', 'bps'),
        ('3', 'ticks'),
        ('4', ''),
        ('5', '€'),
        ('6', 'pts')
    )
    value = models.DecimalField(max_digits=15, decimal_places=5)
    unit = models.CharField(max_length=5, choices=UNITS_CHOICES, default='4')
    precision = models.PositiveSmallIntegerField(default=0)
    val_format = models.PositiveSmallIntegerField(default=0)
    val_sequence = models.PositiveSmallIntegerField(default=0)
    description = models.CharField(max_length=200, blank=True, null=True)
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE, blank=True, null=True, )

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return str(self.description) + '@' + str(self.symbol)


class all_last_update_v(models.Model):
	val_value = models.DecimalField(max_digits=15, decimal_places=5)
	val_unit = models.CharField(max_length=5)
	val_precision = models.PositiveSmallIntegerField(default=0)
	val_format = models.PositiveSmallIntegerField(default=0)
	val_sequence = models.PositiveSmallIntegerField(default=0)
	val_description = models.CharField(max_length=200, blank=True, null=True)
	sym_name = models.CharField(max_length=20)
	sym_des = models.CharField(max_length=200, null=True)
	cat_name = models.CharField(max_length=20)
	cat_des = models.CharField(max_length=200, null=True)
	pub_date = models.DateField()
	pub_hour = models.TimeField()

	class Meta:
		managed = False
		db_table = "all_last_update_v"

	def __str__(self):
		return str(self.pub_date) + '@' + str(self.pub_hour)