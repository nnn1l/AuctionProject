# Auction Shop

Auction Shop is a web application for running online auctions where users can create auctions for their items, place bids on other auctions, and automatically receive winnings once the auction ends.


### Technologies

* Python 3.12
* Django
* PostgreSQL 
* Redis
* Celery (automatic auction ending)
* Django Ninja (REST API)
* Docker & Docker Compose


### Installation

1. Clone the repository:

git clone https://github.com/nnn1l/AuctionProject
cd Auction_shop

2. Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate  # MacOS/Linux
.venv\Scripts\activate     # Windows

3. Install dependencies:

pip install --upgrade pip
pip install -r requirements.txt

4. Start Docker containers:

cd auction_project
docker compose up --build


### Database & Migrations

To set up the database, run:
docker compose run web python manage.py migrate


### Running the Project

Django server: docker compose up

Celery (automatic auction ending every minute): docker compose up celery


### Features

* User registration and authentication
* Auction creation with associated items
* Bidding system: users can increase auction prices
* Automatic auction completion via Celery
* User wallet balance management
* REST API (ninja) for integration and data management


### API Endpoints

##### Examples of available endpoints:

1. Users:

    GET /api/users/ _— list all users_

    GET /api/users/{id}/ _— view user profile_

    PATCH /api/users/{id}/ _— update profile_

2. Auctions:

    GET /api/auctions/ _— list all auctions_

    POST /api/auctions/ _— create a new auction_

    PATCH /api/auctions/{id}/ _— update auction_

3. Bids:

    GET /api/bids/ _— list all bids_

    POST /api/bids/ _— place a bid_