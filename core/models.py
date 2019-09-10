from django.db import models

class Organization(models.Model):
	name = models.CharField(max_length=150)
	type = models.CharField(max_length=45)
	status = models.CharField(max_length=45)
	description = models.TextField()
	address = models.CharField(max_length=500)
	geo_lat = models.FloatField(null=True, blank=True)
	geo_lng = models.FloatField(null=True, blank=True)
	logo = models.CharField(max_length=255)
	ecobuilder_id  = models.ForeignKey("Organization", on_delete=models.CASCADE)