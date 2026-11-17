from decimal import Decimal

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Base, Order, Product, User

DATABASE_URL = "sqlite:///orders.db"


def seed_and_demo() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        # Recreate the same predictable dataset each time the script runs.
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        anna = User(name="Анна")
        boris = User(name="Борис")

        keyboard = Product(name="Клавиатура", price=Decimal("3500.00"))
        mouse = Product(name="Мышь", price=Decimal("1200.00"))
        monitor = Product(name="Монитор", price=Decimal("18000.00"))

        order_1 = Order(
            total_price=Decimal("4700.00"),
            user=anna,
            products=[keyboard, mouse],
        )
        order_2 = Order(
            total_price=Decimal("19200.00"),
            user=anna,
            products=[mouse, monitor],
        )
        order_3 = Order(
            total_price=Decimal("3500.00"),
            user=boris,
            products=[keyboard],
        )

        session.add_all([order_1, order_2, order_3])
        session.commit()

        print("Заказы пользователей (User -> Order):")
        for user in session.scalars(select(User).order_by(User.id)):
            print(f"- {user.name}:")
            for order in user.orders:
                print(
                    f"  Заказ #{order.id}, сумма {order.total_price}: "
                    f"{', '.join(product.name for product in order.products)}"
                )

        print("\nПользователи и заказы для каждого товара (Product -> Order -> User):")
        for product in session.scalars(select(Product).order_by(Product.id)):
            orders = ", ".join(
                f"#{order.id} ({order.user.name})" for order in product.orders
            )
            print(f"- {product.name}: {orders}")


if __name__ == "__main__":
    seed_and_demo()
