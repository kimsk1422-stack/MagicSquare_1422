"""Boundary UI 픽스처 — Flask app·test client."""

import pytest


@pytest.fixture
def app(grid_g1):
    from src.app import create_app

    return create_app(initial_grid=grid_g1)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def client_with_g1(client, grid_g1):
    _ = grid_g1
    return client
