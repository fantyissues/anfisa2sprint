from django.contrib import admin

from .models import Category, IceCream, Topping, Wrapper


class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0


@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


admin.site.register(Topping)
admin.site.register(Wrapper)
admin.site.empty_value_display = 'Не задано'