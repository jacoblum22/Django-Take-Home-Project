from django.test import TestCase
from .models import Category, Product, Tag
from django.urls import reverse

# Create your tests here.
class Tests(TestCase):
    @classmethod
    def setUpTestData(cls):

        # Test categories
        cls.electronics = Category.objects.create(
            name = "Electronics"
        )
        cls.books = Category.objects.create(
            name = "Books & Stationery"
        )
        cls.fitness = Category.objects.create(
            name = "Fitness & Outdoors"
        )

        # Test products
        cls.headphones = Product.objects.create(
            name = "Noise-Canceling Headphones",
            category = cls.electronics,
            description = "Over-ear headphones with active noise cancellation for travel and focus.",
        )
        cls.btspeaker = Product.objects.create(
            name = "Portable Bluetooth Speaker",
            category = cls.electronics,
            description = "Compact speaker built for outdoor gatherings and poolside listening."
        )
        cls.charger = Product.objects.create(
            name = "USB-C Fast Charger",
            category = cls.electronics,
            description = "High-wattage wall adapter for rapid charging of laptops and phones."
        )
        cls.pen_kit = Product.objects.create(
            name = "Fountain Pen Starter Kit",
            category = cls.books,
            description = "Smooth-writing fountain pen with refillable ink cartridges for daily notes."
        )
        cls.notebook = Product.objects.create(
            name = "Dotted Hardcover Notebook",
            category = cls.books,
            description = "Thick-paper dot-grid journal for sketching, planning, and bullet journaling."
        )
        cls.handbook = Product.objects.create(
            name = "SQL & Data Modeling Handbook",
            category = cls.books,
            description = "Practical reference book covering relational schemas, indexing, and query design."
        )
        cls.shoes = Product.objects.create(
            name = "Trail Running Shoes",
            category = cls.fitness,
            description = "Breathable running shoes with grippy soles for dirt trails and gravel paths."
        )

        # Test tags
        cls.wireless = Tag.objects.create(name = "Wireless")
        cls.bestseller = Tag.objects.create(name = "Bestseller")
        cls.portable = Tag.objects.create(name = "Portable")
        cls.waterproof = Tag.objects.create(name = "Waterproof")
        cls.new_arrival = Tag.objects.create(name = "New arrival")
        cls.beginner_friendly = Tag.objects.create(name = "Beginner-friendly")
        cls.gift_idea = Tag.objects.create(name = "Gift idea")
        cls.eco_friendly = Tag.objects.create(name = "Eco-friendly")
        cls.sale = Tag.objects.create(name = "Sale")
        cls.lightweight = Tag.objects.create(name = "Lightweight")

        # Add tags to products
        cls.headphones.tags.set([cls.wireless, cls.bestseller])
        cls.btspeaker.tags.set([cls.wireless, cls.portable, cls.waterproof])
        cls.charger.tags.set([cls.portable, cls.new_arrival])
        cls.pen_kit.tags.set([cls.beginner_friendly, cls.gift_idea])
        cls.notebook.tags.set([cls.eco_friendly, cls.new_arrival])
        cls.handbook.tags.set([cls.sale, cls.beginner_friendly])
        cls.shoes.tags.set([cls.bestseller, cls.lightweight])

    def test_site_responsive(self):
        """Site is up."""
        response = self.client.get(reverse("main_page"))
        self.assertEqual(response.status_code, 200)

    def test_description_search(self):
        """Description filter works alone."""
        response = self.client.get(reverse("main_page"), {"p": "Over-ear"})
        products = response.context["prods"]
        self.assertIn(self.headphones, products)
        self.assertEqual(len(products), 1)

    def test_tag_AND_filter(self):
        """Tag filter works alone."""
        response = self.client.get(reverse("main_page"), {"tags": [str(self.wireless.pk), str(self.portable.pk)]})
        products = response.context["prods"]
        self.assertIn(self.btspeaker, products)
        self.assertEqual(len(products), 1)

    def test_category_OR_filter(self):
        """Category filter works alone."""
        response = self.client.get(reverse("main_page"), {"cats": [str(self.electronics.pk), str(self.books.pk)]})
        products = response.context["prods"]
        self.assertIn(self.headphones, products)
        self.assertIn(self.btspeaker, products)
        self.assertIn(self.charger, products)
        self.assertIn(self.pen_kit, products)
        self.assertIn(self.notebook, products)
        self.assertIn(self.handbook, products)
        self.assertNotIn(self.shoes, products)
        self.assertEqual(len(products), 6)

    def test_incoherent_cat(self):
        """An incoherent category in the URL doesn't crash."""
        response = self.client.get(reverse("main_page"), {"cats": ["abc"]})
        products = response.context["prods"]
        self.assertEqual(len(products), 7)

    def test_incoherent_tag(self):
        """An incoherent tag in the URL doesn't crash."""
        response = self.client.get(reverse("main_page"), {"tags": ["abc"]})
        products = response.context["prods"]
        self.assertEqual(len(products), 7)

    def test_combine_filters(self):
        """Filters work properly together."""
        response = self.client.get(reverse("main_page"), {"p": "with", "cats": [str(self.electronics.pk)], "tags": [str(self.wireless.pk)]})
        products = response.context["prods"]
        self.assertIn(self.headphones, products)
        self.assertEqual(len(products), 1)