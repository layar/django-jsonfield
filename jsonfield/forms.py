from django.utils import simplejson as json

from django import forms
from django.forms.util import ValidationError
from django.utils.translation import ugettext_lazy as _

class JSONFormField(forms.Field):
    def clean(self, value):
        if not value and not self.required:
            return None

        value = super(JSONFormField, self).clean(value)

        if isinstance(value, basestring):
            try:
                json.loads(value)
            except ValueError:
                raise ValidationError(_("Enter valid JSON"))
        return value
