import numpy as np
import plotly.graph_objects as go

def dg_figure(
    xlim=(-4, 4),
    ylim=(-4, 4),
    zlim=(-4, 4),
    axis_labels=("x", "y", "z"),
    bgcolor="darkgrey",
    zerolinecolor="red",
) -> go.Figure:
    ax = {
        "backgroundcolor": bgcolor,
        "gridcolor": "lightgrey",
        "zerolinecolor": zerolinecolor,
        "showbackground": True
    }

    fig = go.Figure()
    fig.update_layout(
        template="plotly_dark",
        scene={
            "xaxis": {
                **ax, 
                "title": axis_labels[0],
                "range": list(xlim)
            },
            "yaxis": {
                **ax,
                "title": axis_labels[1],
                "range": list(ylim)
            },
            "zaxis": {
                **ax,
                "title": axis_labels[2],
                "range": list(zlim)
            },
        },
        margin = {"l": 0, "r": 0, "t": 30, "b": 0},
        scene_aspectmode = "cube"
    )
    return fig


def add_point(
    fig: go.Figure,
    point: np.ndarray | list,
    color: str = "black",
    symbol: str = "circle",
    size: int = 4,
    opacity: float = 1.0,
    name: str | None = None,
) -> go.Figure:
    p = np.asarray(point, dtype=float).ravel()

    fig.add_trace(go.Scatter3d(
        x=[p[0]], y=[p[1]], z=[p[2]],
        mode="markers",
        marker={"color": color, "size": size, "symbol": symbol, "opacity": opacity},
        name=name or "",
        showlegend=name is not None
    ))
    return fig
 

def add_vector(
    fig: go.Figure,
    vector: np.ndarray | list,
    base: np.ndarray | list | None = None,
    color: str = "black",
    line_width: float = 3.0,
    line_style: str = "solid",
    cone_scale: float = 0.2,
    opacity: float = 1.0,
    name: str | None = None,
) -> go.Figure:
    v = np.asarray(vector, dtype=float).ravel()
    b = np.asarray(np.zeros(3) if base is None else base, dtype=float).ravel()

    tip = v + b

    fig.add_trace(go.Scatter3d(
        x=[b[0], tip[0]],
        y=[b[1], tip[1]],
        z=[b[2], tip[2]],
        mode="lines",
        line={"color": color, "width": line_width, "dash": line_style},
        opacity=opacity,
        name=name or "",
        showlegend=name is not None
    ))

    fig.add_trace(go.Cone(
        x=[tip[0]], y=[tip[1]], z=[tip[2]],
        u=[v[0]], v=[v[1]], w=[v[2]],
        colorscale=[[0, color], [1, color]],
        showscale=False,
        opacity=opacity,
        sizemode="absolute",
        sizeref=cone_scale,
        anchor="tip",
        name="",
        showlegend=False
    ))

    return fig
