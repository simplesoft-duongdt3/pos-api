from .models import Product, Category
from datetime import date, datetime


def convertDateTime(strDateTime: str):
    if strDateTime != None:
        return datetime.strptime(strDateTime, '%Y-%m-%d %H:%M:%S')
    else:
        return None


def convertDate(strDate: str):
    if strDate != None:
        return datetime.strptime(strDate, '%Y-%m-%d').date()
    else:
        return None



class ProductModel:
    def __init__(self, sku, name, price, thumbUrl):
        self.sku = sku
        self.name = name
        self.price = price
        self.thumbUrl = thumbUrl

class CategoryModel():
    def __init__(self, name, colorCode, products):
        self.name = name
        self.colorCode = colorCode
        self.products = products


def getCategoryListWithProduct():
    categories = Category.objects.all()

    categoryModels = []
    for category in categories:
        print(category)
        products = []
        productDbs = category.product_set.all()
        print(productDbs)
        for product in productDbs:
            print(product)
            productModel = ProductModel(sku=product.sku, name=product.name, price= product.price, thumbUrl=product.thumbUrl)
            products.append(productModel)
            print(productModel)
        categoryModel = CategoryModel(name= category.name, colorCode= category.colorCode, products= products)
        categoryModels.append(categoryModel)
        print(categoryModel)
        print(dir(categoryModel))

    print(categoryModels)
    print(dir(categoryModels))
    return categoryModels
