from app.extensions import db
class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price=db.Column(db.Decimal(10, 2), nullable=False)
    total_amount=db.Column(db.Decimal(10,2),nullable=False)
    status=db.Column(db)