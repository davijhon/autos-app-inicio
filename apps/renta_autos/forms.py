from django import forms

from .models import Cliente

# AUTO_COLOR_CHOICES = {}
# AUTO_CHOICES = {}
# AUTO_MODELO_CHOICES = {}
# AUTO_TIPO_CHOICES = {}


# try:
# 	choices_values = Cliente.objects.values(
# 		'auto', 'auto_modelo', 
# 		'auto_color', 'auto_tipo')

# 	all_auto_color_values = choices_values.values_list('auto_color', flat=True)
# 	for idx, value in enumerate(all_auto_color_values):
# 		if value not in AUTO_COLOR_CHOICES.values():
# 			AUTO_COLOR_CHOICES.update({idx: value})


# 	all_auto_values = choices_values.values_list('auto', flat=True)
# 	for idx, value in enumerate(all_auto_values):
# 		if value not in AUTO_CHOICES.values():
# 			AUTO_CHOICES.update({idx: value})

# 	all_auto_modelo_values = choices_values.values_list('auto_modelo', flat=True)
# 	for idx, value in enumerate(all_auto_modelo_values):
# 		if value not in AUTO_MODELO_CHOICES.values():
# 			AUTO_MODELO_CHOICES.update({idx: value})

# 	all_auto_tipo_values = choices_values.values_list('auto_tipo', flat=True)
# 	for idx, value in enumerate(all_auto_tipo_values):
# 		if value not in AUTO_TIPO_CHOICES.values():
# 			AUTO_TIPO_CHOICES.update({idx: value})

# except Exception as e:
# 	pass




class ClientFilterForm(forms.Form):
    pass
	# color_choices = forms.MultipleChoiceField(
	# 	choices=tuple(AUTO_COLOR_CHOICES.items()), 
	# 	required=False,
	# 	widget=forms.CheckboxSelectMultiple(
	# 		attrs={
	# 			'class': 'form-control mb-3 form-filter-input'}))

	# auto_choices = forms.MultipleChoiceField(
	# 		choices=tuple(AUTO_CHOICES.items()), 
	# 		required=False,
	# 		widget=forms.CheckboxSelectMultiple(
	# 			attrs={
	# 				'class': 'form-control mb-3 form-filter-input'}))

	# auto_modelo_choices = forms.MultipleChoiceField(
	# 	choices=tuple(AUTO_MODELO_CHOICES.items()), 
	# 	required=False,
	# 	widget=forms.CheckboxSelectMultiple(
	# 		attrs={
	# 			'class': 'form-control mb-3 form-filter-input'}))

	# auto_tipo_choices = forms.MultipleChoiceField(
	# 	choices=tuple(AUTO_TIPO_CHOICES.items()), 
	# 	required=False,
	# 	widget=forms.CheckboxSelectMultiple(
	# 		attrs={
	# 			'class': 'form-control mb-3 form-filter-input'}))

	# fec_alta = forms.DateField(
	# 	widget=forms.DateInput(
	# 		attrs={'class': 'form-control form-control-sm',
	# 			'type': 'date'}), 
	# 		label="Fecha de alta:",
	# 		required=False,
	# 		)