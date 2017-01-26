from django.db import models


class TimeStampedModelMixin(models.Model):
	"""
	Provides created and updated fields for model.
	"""

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
