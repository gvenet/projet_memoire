from models.model import db, Product

# Liste de produits à ajouter à la base de données
products_data = [
    {
        "nom": "Produit 1",
        "prix": 10.99,
        "description": "Description du produit 1",
        "image_url": "https://static.goldengoose.com/image/upload/v1666257150/Style/ECOMM/GMF00102.F003987-11357"
    },
    {
        "nom": "Produit 2",
        "prix": 19.95,
        "description": "Description du produit 2",
        "image_url": "https://static.goldengoose.com/image/upload/w_400,c_scale,f_auto,q_auto/v1683204594/Style/ECOMM/GMF00327.F004619-11518-2"
    },
    {
        "nom": "Produit 3",
        "prix": 5.49,
        "description": "Description du produit 3",
        "image_url": "https://static.goldengoose.com/image/upload/w_400,c_scale,f_auto,q_auto/v1631615787/Style/ECOMM/GMF00117.F002198-10327-2"
    },
    {
        "nom": "Produit 4",
        "prix": 8.75,
        "description": "Description du produit 4",
        "image_url": "https://static.goldengoose.com/image/upload/w_auto,c_scale,f_auto,q_auto/v1643304993/Style/ECOMM/GMF00117.F002517-60324"
    },
    {
        "nom": "Produit 5",
        "prix": 14.99,
        "description": "Description du produit 5",
        "image_url": "https://static.goldengoose.com/image/upload/w_auto,c_scale,f_auto,q_auto/v1673608638/Style/ECOMM/GMF00117.F004452-11457"
    },
    {
        "nom": "Produit 6",
        "prix": 7.25,
        "description": "Description du produit 6",
        "image_url": "https://static.goldengoose.com/image/upload/w_400,c_scale,f_auto,q_auto/v1657532775/Style/ECOMM/GMF00117.F003465-50716"
    }
]

def seed_products():
    for product_data in products_data:
        product = Product(
            nom=product_data["nom"],
            prix=product_data["prix"],
            description=product_data["description"],
            image_url=product_data["image_url"]
        )
        db.session.add(product)

    db.session.commit()

if __name__ == "__main__":
    from app import create_app
    app = create_app()
    with app.app_context():
        seed_products()
