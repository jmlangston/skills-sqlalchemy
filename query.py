"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *


# init_app()

# JML note: is line 17 necessary?

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.

SELECT * FROM Brands WHERE id = 8;

Brand.query.filter_by(id=8)

b = db.session.query(Brand).filter_by(id=8).all()
print b[0].name


# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

SELECT * FROM Models WHERE name = 'Corvette' AND brand_name = 'Chevrolet';

Model.query.filter_by(brand_name='Chevrolet', name='Corvette')

cc = db.session.query(Model).filter_by(brand_name='Chevrolet', name='Corvette').all()

>>> len(cc)
12

for c in cc:
    print c.name, c.brand_name


# Get all models that are older than 1960.

SELECT * FROM Models WHERE year < 1960;

>>> Model.query.filter_by(year < 1960).all()
NameError: name 'year' is not defined

old = db.session.query(Model).filter_by(year < '1960').all()

>>> old = db.session.query(Model).filter_by(Model.year == '1960').all()
TypeError: filter_by() takes exactly 1 argument (2 given)


# Get all brands that were founded after 1920.

SELECT * FROM Brands WHERE founded > 1920;


# Get all models with names that begin with "Cor".

SELECT * FROM Models WHERE name LIKE 'Cor%';


# Get all brands with that were founded in 1903 and that are not yet discontinued.

SELECT * FROM Brands WHERE founded = 1903 AND discontinued IS NULL;


# Get all brands with that are either discontinued or founded before 1950.

SELECT * FROM Brands WHERE discontinued NOT NULL OR founded < 1950;


# Get any model whose brand_name is not Chevrolet.

SELECT * FROM Models WHERE brand_name != 'Chevrolet';


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    a = db.session.query(Model.name, Model.brand_name, Brand.headquarters).filter(year=year)

    >>> a = db.session.query(Model.name, Model.brand_name, Brand.headquarters).filter(Model.year=1960)
    File "<stdin>", line 1
    SyntaxError: keyword cant be an expression


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    pass

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

>>> Brand.query.filter_by(name='Ford')
<flask_sqlalchemy.BaseQuery object at 0x1014db550>
>>> b = Brand.query.filter_by(name='Ford')
>>> type(b)
<class 'flask_sqlalchemy.BaseQuery'>
>>> print b
SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued 
FROM brands 
WHERE brands.name = :name_1

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
