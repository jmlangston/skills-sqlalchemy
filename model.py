"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):
    """Defines Model table in database."""

    __tablename__ = "models"

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    brand_name = db.Column(db.String, db.ForeignKey('brands.name'), nullable=False)
    name = db.Column(db.String, nullable=False)
    brand = db.relationship('Brand', backref=db.backref('model'))

    # JML note: line 22 throws an error ("non-keyword arg after keyword arg")
    # when written as
    # brand_name = db.Column(db.String, nullable=False, db.ForeignKey('brands.name'))

    # If the foreign key argument is written as a keyword argument there's no error
    # foreign_key = db.ForeignKey('brands.name')

    # If the foreign key argument is passed without 'foreign_key='
    # it must be positioned before the keyword argument 'nullable=false'

    def __repr__(self):
        """Show information about car model."""

        return "<Model id=%d, year=%d, brand_name=%s, name=%s, brand=%s" % (self.id, self.year, self.brand_name, self.name, self.brand)


class Brand(db.Model):

    """Defines Brand table in database. A brand can have many models."""

    __tablename__ = "brands"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    founded = db.Column(db.Integer, nullable=False)
    headquarters = db.Column(db.String, nullable=False)
    discontinued = db.Column(db.Integer)

    # def __repr__(self):
    #     """Show information about brand."""

    #     return "<Brand id=%d name=%s founded=%d headquarters=%s discontinued=%d>" % (self.id, self.name, self.founded, self.headquarters, self.discontinued)


# End Part 1
##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
