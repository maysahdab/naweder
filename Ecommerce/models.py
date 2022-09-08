from django.db import models
from django.contrib.auth.models import User
from currencyapp.models import Currency
from django.contrib import admin


class Tag(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50)
    description = models.CharField(max_length=250,default='', blank=True)
    descriptionar = models.CharField(max_length=250,default='', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50)
    description = models.CharField(max_length=250,default='', blank=True)
    descriptionar = models.CharField(max_length=250,default='', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50)
    description = models.CharField(max_length=250,default='', blank=True)
    descriptionar = models.CharField(max_length=250,default='', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sub Categories"


class ProductCategory(models.Model):
    categoryid = models.ForeignKey(Category, on_delete=models.PROTECT, null=False)
    subcategoryid = models.ForeignKey(SubCategory, on_delete=models.PROTECT, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Categories"


class Product(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50)
    description = models.CharField(max_length=250,default='', blank=True)
    descriptionar = models.CharField(max_length=250,default='', blank=True)
    sku = models.CharField(max_length=25)
    slug = models.SlugField( default='', blank=True)
    quantity = models.PositiveIntegerField()
    startat = models.DateField(null=True, blank=True)
    endat = models.DateField(null=True, blank=True)
    publishedat = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=1)
    percentage = models.BooleanField(default=False)
    productcategory = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, null=False)
    tag = models.ManyToManyField('Tag', through='ProductTag', blank=True)
    productalternative = models.ManyToManyField('self', symmetrical=True,
                                                  through='Alternative', related_name='alternative_product', blank=True)
    productcomlementary = models.ManyToManyField('self', symmetrical=False,
                                                  through='Complementary', related_name='complementary_product', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Alternative(models.Model):
    product1 = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_base')
    product2 = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_alternative')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product1', 'product2')


class Alternative_Inline(admin.TabularInline):
    model = Alternative
    fk_name = 'product1'
    extra = 1


class Complementary(models.Model):
    product1 = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_root')
    product2 = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_complement')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product1', 'product2')

    class Meta:
        verbose_name_plural = "Complementaries"

class Complementary_Inline(admin.TabularInline):
    model = Complementary
    fk_name = 'product1'
    extra = 1


class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class ProductTag_Inline(admin.TabularInline):
    model = ProductTag
    extra = 1


class ProductMeta(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50)
    description = models.CharField(max_length=250,default='', blank=True)
    descriptionar = models.CharField(max_length=250,default='', blank=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False)
    description = models.CharField(max_length=250, default='', blank=True)
    descriptionar = models.CharField(max_length=250, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# class ImagesProduct(models.Model):
#
#     image = models.ForeignKey(Image, on_delete=models.PROTECT, null=False)
#     product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False)
#     description = models.CharField(max_length=250, default='', blank=True)
#     descriptionar = models.CharField(max_length=250, default='', blank=True)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = "Products' Images"



class Type(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50)
    description = models.CharField(max_length=250,default='', blank=True)
    descriptionar = models.CharField(max_length=250,default='', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TypeDetail(models.Model):
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50)
    description = models.CharField(max_length=250, default='',blank=True)
    descriptionar = models.CharField(max_length=250,default='', blank=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Variant(models.Model):
    quantity = models.PositiveIntegerField()
    extraprice = models.DecimalField(max_digits=10, decimal_places=1)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False)

    typedetail = models.ManyToManyField('TypeDetail', through='VariantSpeciality')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ImagesVariant(models.Model):
    description = models.CharField(max_length=250, default='',blank=True)
    descriptionar = models.CharField(max_length=250,default='', blank=True)
    image = models.ForeignKey(Image, on_delete=models.PROTECT, null=False)
    variant = models.ForeignKey(Variant, on_delete=models.PROTECT, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Variants' Images"

class VariantSpeciality(models.Model):
    variant = models.ForeignKey(Variant, on_delete=models.PROTECT)
    typedetail = models.ForeignKey(TypeDetail, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Variant Specialities"

class VariantSpeciality_Inline(admin.TabularInline):
    model = VariantSpeciality
    extra = 1


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    orderdate = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=1)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=1)
    percentage = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=1)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=False)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    variant = models.ForeignKey(Variant, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=False)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class PaymentMethod(models.Model):
    type = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class PaymentDetail(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=1)
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT)
    method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    paymentgatwayresponse = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class RefundRequestItemOrder(models.Model):
    refunddate = models.DateField()
    orderitem = models.ForeignKey(OrderItem, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Refund(models.Model):
    description = models.CharField(max_length=250,default='', blank=True)
    descriptionar = models.CharField(max_length=250,default='', blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=1)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=False)
    refund = models.ForeignKey(RefundRequestItemOrder, on_delete=models.PROTECT, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='profile')
    cart = models.ManyToManyField('Variant', through='CartItem', related_name='cart_item')
    list = models.ManyToManyField('Variant', through='WishList', related_name='wish_list')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    variant = models.ForeignKey(Variant, on_delete=models.PROTECT)
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class CartItem_Inline(admin.TabularInline):
    model = CartItem
    extra = 1


class WishList(models.Model):
    variant = models.ForeignKey(Variant, on_delete=models.PROTECT)
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class WishList_Inline(admin.TabularInline):
    model = WishList
    extra = 1

class ReviewProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=250, blank=True)
    descriptionar = models.CharField(max_length=250, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Reviews Products"

class ReviewOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=250, blank=True)
    descriptionar = models.CharField(max_length=250, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Reviews Orders"