from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductTag_Inline, Alternative_Inline, Complementary_Inline,)


class VariantAdmin(admin.ModelAdmin):
    inlines = (VariantSpeciality_Inline,)


class UserProfileAdmin(admin.ModelAdmin):
    inlines = (WishList_Inline, CartItem_Inline)

class ReviewProductAdmin(admin.ModelAdmin):
    fields = ( 'product', 'user', 'description', 'descriptionar',)

class ReviewOrderAdmin(admin.ModelAdmin):
    fields = ( 'order', 'user', 'description', 'descriptionar',)

admin.site.register(Tag)
admin.site.register(ProductMeta)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProductCategory)
admin.site.register(ProductTag)
admin.site.register(Image)
# admin.site.register(ImagesProduct)
admin.site.register(ImagesVariant)
admin.site.register(VariantSpeciality)
admin.site.register(TypeDetail)
admin.site.register(Type)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(Alternative)
admin.site.register(Complementary)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(PaymentMethod)
admin.site.register(PaymentDetail)
admin.site.register(RefundRequestItemOrder)
admin.site.register(Refund)
admin.site.register(CartItem)
admin.site.register(WishList)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ReviewProduct, ReviewProductAdmin)
admin.site.register(ReviewOrder, ReviewOrderAdmin)

