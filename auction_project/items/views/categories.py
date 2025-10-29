from django.views.generic import ListView
from ..models.Category import Category
from auctions.models.Auction import Auction #ignore error


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category_template/all_categories.html'

class BaseCategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    category_title = 'base category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['auctions'] = Auction.objects.all()    #ignore IDE error
        context['subject'] = Category.objects.filter(title=self.category_title).first()
        return context

class AntiquesListView(BaseCategoryListView):
    template_name = 'category_template/antiques.html'
    category_title = "Antiques"

class ArtCraftsListView(BaseCategoryListView):
    template_name = 'category_template/art-crafts.html'
    category_title = "Art & Crafts"

class CarsListView(BaseCategoryListView):
    template_name = 'category_template/cars-trucks.html'
    category_title = "Cars"

class ClothingShoesAccessoriesListView(BaseCategoryListView):
    template_name = 'category_template/clothing-shoes-accessories.html'
    category_title = "Clothing, Shoes & Accessories"

class ElectronicsComputersListView(BaseCategoryListView):
    template_name = 'category_template/electronics-computers.html'
    category_title = "Electronics & Computers"

class FurnitureListView(BaseCategoryListView):
    template_name = 'category_template/furniture.html'
    category_title = "Furniture"

class GamesToysListView(BaseCategoryListView):
    template_name = 'category_template/games-toys.html'
    category_title = "Games & Toys"

class HomeGardenListView(BaseCategoryListView):
    template_name = 'category_template/home-garden.html'
    category_title = "Home & Garden"

class JewelryListView(BaseCategoryListView):
    template_name = 'category_template/jewelry-watches.html'
    category_title = "Jewelry"

class MusicInstrumentsListView(BaseCategoryListView):
    template_name = 'category_template/music-instruments.html'
    category_title = "Music & Instruments"

class PhotographyCamerasListView(BaseCategoryListView):
    template_name = 'category_template/photography-cameras.html'
    category_title = "Photography & Cameras"

class SportsOutdoorsListView(BaseCategoryListView):
    template_name = 'category_template/sports-outdoors.html'
    category_title = "Sports & Outdoors"

class StampsCoinsListView(BaseCategoryListView):
    template_name = 'category_template/stamps-coins.html'
    category_title = "Stamps & Coins"

class VideoGamesConsolesListView(BaseCategoryListView):
    template_name = 'category_template/video-games-consoles.html'
    category_title = "Video Games & Consoles"

class BooksMagazinesListView(BaseCategoryListView):
    template_name = 'category_template/books-magazines.html'
    category_title = "Books & Magazines"

class HandmadeListView(BaseCategoryListView):
    template_name = 'category_template/handmade.html'
    category_title = "Handmade"