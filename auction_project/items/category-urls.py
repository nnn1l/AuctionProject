from django.urls import path
from .views import categories


urlpatterns = [
    path('all/', categories.CategoryListView.as_view(), name='all-categories'),
path('antiques/', categories.AntiquesListView.as_view(), name='antiques'),
path('art-crafts/', categories.ArtCraftsListView.as_view(), name='art-crafts'),
path('books-magazines/', categories.BooksMagazinesListView.as_view(), name='books-magazines'),
path('cars/', categories.CarsListView.as_view(), name='cars'),
path('clothing-shoes-accessories/', categories.ClothingShoesAccessoriesListView.as_view(), name='clothing-shoes-accessories'),
path('electronics-computers/', categories.ElectronicsComputersListView.as_view(), name='electronics-computers'),
path('furniture/', categories.FurnitureListView.as_view(), name='furniture'),
path('games-toys/', categories.GamesToysListView.as_view(), name='games-toys'),
path('handmade/', categories.HandmadeListView.as_view(), name='handmade'),
path('home-garden/', categories.HomeGardenListView.as_view(), name='home-garden'),
path('jewelry/', categories.JewelryListView.as_view(), name='jewelry'),
path('music-instruments/', categories.MusicInstrumentsListView.as_view(), name='music-instruments'),
path('photography-cameras/', categories.PhotographyCamerasListView.as_view(), name='photography-cameras'),
path('sports-outdoors/', categories.SportsOutdoorsListView.as_view(), name='sports-outdoors'),
path('stamps-coins/', categories.StampsCoinsListView.as_view(), name='stamps-coins'),
path('video-games-consoles/', categories.VideoGamesConsolesListView.as_view(), name='video-games-consoles'),
    ]