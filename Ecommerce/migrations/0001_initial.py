# Generated by Django 3.2.15 on 2022-08-20 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('currencyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('namear', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Complementary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Complementaries',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderdate', models.DateField()),
                ('total', models.DecimalField(decimal_places=1, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=1, max_digits=10)),
                ('percentage', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='currencyapp.currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=1, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='currencyapp.currency')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.order')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='currencyapp.currency')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.order')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('namear', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250)),
                ('sku', models.CharField(max_length=25)),
                ('slug', models.SlugField(blank=True, default='')),
                ('quantity', models.PositiveIntegerField()),
                ('startat', models.DateField(blank=True, null=True)),
                ('endat', models.DateField(blank=True, null=True)),
                ('publishedat', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=1, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=1, max_digits=10)),
                ('percentage', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='currencyapp.currency')),
                ('productalternative', models.ManyToManyField(related_name='_Ecommerce_product_productalternative_+', through='Ecommerce.Alternative', to='Ecommerce.Product')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('namear', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('namear', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('namear', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('namear', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.type')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('extraprice', models.DecimalField(decimal_places=1, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='currencyapp.currency')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.product')),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.userprofile')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.variant')),
            ],
        ),
        migrations.CreateModel(
            name='VariantSpeciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('typedetail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.typedetail')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.variant')),
            ],
            options={
                'verbose_name_plural': 'Variant Specialities',
            },
        ),
        migrations.AddField(
            model_name='variant',
            name='typedetail',
            field=models.ManyToManyField(through='Ecommerce.VariantSpeciality', to='Ecommerce.TypeDetail'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cart',
            field=models.ManyToManyField(related_name='cart_item', through='Ecommerce.CartItem', to='Ecommerce.Variant'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='list',
            field=models.ManyToManyField(related_name='wish_list', through='Ecommerce.WishList', to='Ecommerce.Variant'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ReviewProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=250)),
                ('descriptionar', models.CharField(blank=True, max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reviews Products',
            },
        ),
        migrations.CreateModel(
            name='ReviewOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=250)),
                ('descriptionar', models.CharField(blank=True, max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reviews Orders',
            },
        ),
        migrations.CreateModel(
            name='RefundRequestItemOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refunddate', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('orderitem', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.orderitem')),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250)),
                ('amount', models.DecimalField(decimal_places=1, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='currencyapp.currency')),
                ('refund', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.refundrequestitemorder')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.product')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.tag')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('namear', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.category')),
                ('subcategoryid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.subcategory')),
            ],
            options={
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='productcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='productcomlementary',
            field=models.ManyToManyField(related_name='complementary_product', through='Ecommerce.Complementary', to='Ecommerce.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(through='Ecommerce.ProductTag', to='Ecommerce.Tag'),
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=1, max_digits=10)),
                ('paymentgatwayresponse', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.paymentmethod')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.payment')),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.variant'),
        ),
        migrations.CreateModel(
            name='ImagesVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.image')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.variant')),
            ],
            options={
                'verbose_name_plural': "Variants' Images",
            },
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.product'),
        ),
        migrations.AddField(
            model_name='complementary',
            name='product1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_root', to='Ecommerce.product'),
        ),
        migrations.AddField(
            model_name='complementary',
            name='product2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_complement', to='Ecommerce.product'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.userprofile'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ecommerce.variant'),
        ),
        migrations.AddField(
            model_name='alternative',
            name='product1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_base', to='Ecommerce.product'),
        ),
        migrations.AddField(
            model_name='alternative',
            name='product2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_alternative', to='Ecommerce.product'),
        ),
        migrations.AlterUniqueTogether(
            name='alternative',
            unique_together={('product1', 'product2')},
        ),
    ]