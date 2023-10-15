from django import forms

def RequiredValidator(val, raise_error=True, field_name=''):
    if (isinstance(val, str) and val.strip() and val=='') or val is None:
        if raise_error:
            forms.ValidationError('{} is required'.format(field_name))
        else:
            return False
    return True
