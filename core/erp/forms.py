from datetime import datetime

from django.forms import *

from core.erp.models import Category, Cliente , Sale, Producto, Movimiento, TipoMovimiento, TipoProducto, Empleado, MovEmp, MovCliente, Proveedor, OrdenCompra, Conformidad, Poste

 
class TipoProdForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = TipoProducto
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class TestForm(Form):
    categories = ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    products = ModelChoiceField(queryset=Producto.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    # search = CharField(widget=TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Ingrese una descripción'
    # }))

    search = ModelChoiceField(queryset=Producto.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

class PosteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Poste
        fields = '__all__'
        widgets = {

           
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'tipo_cruceta': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'tipo_abrazadera': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class PosteFormEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
        #    form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['name'].widget.attrs['readonly'] = True

     # Establ

    class Meta:
        model = Poste
        fields = '__all__'
        widgets = {

           
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'tipo_cruceta': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'tipo_abrazadera': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
            
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data