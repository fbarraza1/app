# Generated by Django 4.2.6 on 2023-10-23 22:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('direccion', models.CharField(blank=True, max_length=120, null=True, verbose_name='Direccion')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'Persona',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TipoMovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo de Movimiento',
                'verbose_name_plural': 'Tipos de Movimientos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Nombre')),
                ('desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='erp.persona')),
                ('username', models.CharField(max_length=25, unique=True, verbose_name='Username Ipanel')),
                ('folio_contrato', models.PositiveIntegerField(blank=True, null=True, verbose_name='Folio')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'Cliente',
                'ordering': ['id'],
            },
            bases=('erp.persona',),
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='erp.persona')),
                ('cargo', models.CharField(max_length=25, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'Empleado',
                'ordering': ['id'],
            },
            bases=('erp.persona',),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='identificador único')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d', verbose_name='Imagen')),
                ('stock', models.IntegerField(default=0, verbose_name='stock')),
                ('pvp', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio unitario')),
                ('estado', models.BooleanField(default=True, verbose_name='Incorporado')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.category', verbose_name='Categoría')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.tipoproducto', verbose_name='Tipo de producto')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.tipomovimiento')),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('movimiento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='erp.movimiento')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.cliente')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['id'],
            },
            bases=('erp.movimiento',),
        ),
        migrations.CreateModel(
            name='MovEmp',
            fields=[
                ('movimiento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='erp.movimiento')),
                ('emp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp.empleado')),
            ],
            options={
                'verbose_name': 'Movimiento Empleado',
                'verbose_name_plural': 'Movimientos Empleados',
                'ordering': ['id'],
            },
            bases=('erp.movimiento',),
        ),
        migrations.CreateModel(
            name='MovCliente',
            fields=[
                ('movimiento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='erp.movimiento')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cli', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp.cliente')),
                ('emp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp.empleado')),
            ],
            options={
                'verbose_name': 'Movimiento Cliente',
                'verbose_name_plural': 'Movimientos Clientes',
                'ordering': ['id'],
            },
            bases=('erp.movimiento',),
        ),
        migrations.CreateModel(
            name='DetSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cant', models.IntegerField(default=0)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.producto')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.sale')),
            ],
            options={
                'verbose_name': 'Detalle de Venta',
                'verbose_name_plural': 'Detalle de Ventas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetMovEmp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cant', models.IntegerField(default=0)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.producto')),
                ('movimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.movemp')),
            ],
            options={
                'verbose_name': 'Detalle de Movimiento Empleado',
                'verbose_name_plural': 'Detalle de Movimientos Empleados',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetMov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cant', models.IntegerField(default=0)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.producto')),
                ('movimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.movcliente')),
            ],
            options={
                'verbose_name': 'Detalle de Movimiento',
                'verbose_name_plural': 'Detalle de Movimientos',
                'ordering': ['id'],
            },
        ),
    ]
