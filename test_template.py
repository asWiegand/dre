import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.template.loader import render_to_string

try:
    render_to_string('moviment_list.html', {'moviments': [], 'field': 'value'})
    print("moviment_list.html - OK")
except Exception as e:
    print("moviment_list.html - ERROR")
    import traceback
    traceback.print_exc()

try:
    from django import forms
    class DummyForm(forms.Form):
        value = forms.CharField()
    render_to_string('moviment_form.html', {'form': DummyForm()})
    print("moviment_form.html - OK")
except Exception as e:
    print("moviment_form.html - ERROR")
    import traceback
    traceback.print_exc()
