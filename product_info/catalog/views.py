from django.shortcuts import render

# Create your views here.
from .models import Product, Tag, Category

def main_page(request):
    """Creates the main product search page, with description, category and tag filters."""
    # get p (product description), categories and tags, and remove nonsense inputs
    p = request.GET.get('p', '')
    cats = request.GET.getlist('cats')
    cats = [c for c in cats if c.isdigit()]
    tags = request.GET.getlist('tags')
    tags = [t for t in tags if t.isdigit()]

    # Get the list of all products
    prods = Product.objects.select_related('category').prefetch_related('tags')

    if p:
        # Filter on product description
        prods = prods.filter(description__icontains = p)
    if cats:
        # Filter on matching ANY category
        prods = prods.filter(category__id__in = cats)
    if tags:
        # Filter on matching EVERY tag
        for t in tags:
            prods = prods.filter(tags__id = t)

    # Context for template
    context = {
        'prods': prods,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'p': p,
        'selected_cats': cats,
        'selected_tags': tags,
    }
    return render(request, 'catalog/main_page.html', context)
