import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class CartItem(SqlAlchemyBase, SerializerMixin, UserMixin):
    __tablename__ = 'cartitems'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('user.id'), nullable=False)
    product_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('product.id'), nullable=False)
    quantity = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=1)
