"""Dependency injection example, Cars & Engines IoC containers."""

import dependency_injector.containers as containers
import dependency_injector.providers as providers

class Engine(object):
    """Example engine base class.

    Engine is a heart of every car. Engine is a very common term and could be
    implemented in very different ways.
    """


class GasolineEngine(Engine):
    """Gasoline engine."""


class DieselEngine(Engine):
    """Diesel engine."""


class ElectroEngine(Engine):
    """Electro engine."""



class Car(object):
    """Example car."""

    def __init__(self, engine):
        """Initializer."""
        self._engine = engine  # Engine is injected


class Engines(containers.DeclarativeContainer):
    """IoC container of engine providers."""

    gasoline = providers.Factory(GasolineEngine)

    diesel = providers.Factory(DieselEngine)

    electro = providers.Factory(ElectroEngine)


class Cars(containers.DeclarativeContainer):
    """IoC container of car providers."""

    gasoline = providers.Factory(Car,
                                 engine=Engines.gasoline)

    diesel = providers.Factory(Car,
                               engine=Engines.diesel)

    electro = providers.Factory(Car,
                                engine=Engines.electro)


if __name__ == '__main__':
    gasoline_car = Cars.gasoline()
    diesel_car = Cars.diesel()
    electro_car = Cars.electro()