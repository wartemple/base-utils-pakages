from register import Registers


class Model:
    pass


@Registers.model.register(
    {"index": "kk",
    "search_field": {
        "content": "text",
        "name": "text"
    }}
)
class Model1(Model):
    pass


@Registers.model.register('3')
class Model2(Model):
    pass


@Registers.model.register
class Model3(Model):
    pass
