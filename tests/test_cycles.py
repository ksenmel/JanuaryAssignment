from src.cycles import has_cycle

import pytest

def test_graph_with_cycle():
    graph = {
        0: [1],
        1: [2],
        2: [3],
        3: [1],
    }
    assert has_cycle(graph) is True


def test_graph_without_cycle():
    graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [4],
        4: [],
    }
    assert has_cycle(graph) is False


def test_graph_with_self_loop():
    graph = {
        0: [1],
        1: [1],
        2: [0],
    }
    assert has_cycle(graph) is True


def test_disconnected_graph_with_cycle():
    graph = {
        0: [1],
        1: [2],
        2: [],
        3: [4],
        4: [5],
        5: [3],
    }
    assert has_cycle(graph) is True


def test_empty_graph():
    graph = {}
    assert has_cycle(graph) is False


def test_single_vertex_no_edges():
    graph = {0: []}
    assert has_cycle(graph) is False


def test_two_vertices_no_cycle():
    graph = {
        0: [1],
        1: [],
    }
    assert has_cycle(graph) is False


def test_two_vertices_with_cycle():
    graph = {
        0: [1],
        1: [0],
    }
    assert has_cycle(graph) is True


def test_complex_graph_with_cycle():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": ["E"],
        "E": ["C"],
    }
    assert has_cycle(graph) is True


def test_linear_graph():
    graph = {
        1: [2],
        2: [3],
        3: [4],
        4: [5],
        5: [],
    }
    assert has_cycle(graph) is False


def test_tree_structure():
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [],
        5: [],
        6: [],
        7: [],
    }
    assert has_cycle(graph) is False


def test_multiple_components_no_cycle():
    graph = {
        0: [1],
        1: [2],
        2: [],
        3: [4],
        4: [5],
        5: [],
    }
    assert has_cycle(graph) is False


def test_graph_with_multiple_cycles():
    graph = {
        0: [1],
        1: [0, 2],
        2: [3],
        3: [2],
    }
    assert has_cycle(graph) is True