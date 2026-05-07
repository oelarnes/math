# Plotting library for differential geometry. Assisted by Claude

import numpy as np
import plotly.graph_objects as go


def dg_figure(
    xlim=(-4, 4),
    ylim=(-4, 4),
    zlim=(-4, 4),
    axis_labels=("x", "y", "z"),
    bgcolor="dimgrey",
    zerolinecolor="red",
    aspectmode="data",
) -> go.Figure:
    ax = {
        "backgroundcolor": bgcolor,
        "gridcolor": "darkgrey",
        "zerolinecolor": zerolinecolor,
        "showbackground": True,
    }
    fig = go.Figure()
    fig.update_layout(
        template="plotly_dark",
        scene={
            "xaxis": {**ax, "title": axis_labels[0], "range": list(xlim)},
            "yaxis": {**ax, "title": axis_labels[1], "range": list(ylim)},
            "zaxis": {**ax, "title": axis_labels[2], "range": list(zlim)},
            "aspectmode": aspectmode,
        },
        margin={"l": 0, "r": 0, "t": 30, "b": 0},
    )
    return fig


def make_point_trace(
    point,
    color: str = "gold",
    symbol: str = "circle",
    size: int = 3,
    opacity: float = 1.0,
    name: str | None = None,
) -> go.Scatter3d:
    p = np.asarray(point, dtype=float).ravel()
    return go.Scatter3d(
        x=[p[0]], y=[p[1]], z=[p[2]],
        mode="markers",
        marker={"color": color, "size": size, "symbol": symbol, "opacity": opacity},
        name=name or "",
        showlegend=name is not None,
    )


def make_vector_traces(
    vector,
    base=None,
    color: str = "black",
    line_width: float = 4.0,
    line_style: str = "solid",
    cone_scale: float = 0.2,
    opacity: float = 1.0,
    name: str | None = None,
) -> list:
    v = np.asarray(vector, dtype=float).ravel()
    b = np.asarray(np.zeros(3) if base is None else base, dtype=float).ravel()
    tip = v + b

    line = go.Scatter3d(
        x=[b[0], tip[0]], y=[b[1], tip[1]], z=[b[2], tip[2]],
        mode="lines",
        line={"color": color, "width": line_width, "dash": line_style},
        opacity=opacity,
        name=name or "",
        showlegend=name is not None,
    )
    cone = go.Cone(
        x=[tip[0]], y=[tip[1]], z=[tip[2]],
        u=[v[0]], v=[v[1]], w=[v[2]],
        colorscale=[[0, color], [1, color]],
        showscale=False,
        opacity=opacity,
        sizemode="absolute",
        sizeref=cone_scale,
        anchor="tip",
        name="",
        showlegend=False,
    )
    return [line, cone]


def make_curve_trace(
    points,
    color: str = "steelblue",
    width: float = 4.0,
    opacity: float = 1.0,
    name: str | None = None,
) -> go.Scatter3d:
    p = np.asarray(points, dtype=float)
    return go.Scatter3d(
        x=p[:, 0], y=p[:, 1], z=p[:, 2],
        mode="lines",
        line={"color": color, "width": width},
        opacity=opacity,
        name=name or "",
        showlegend=name is not None,
    )


def make_frame_traces(
    base=None,
    scale: float = 1.0,
    colors=("tomato", "limegreen", "dodgerblue"),
    line_width: float = 3.0,
    cone_scale: float = 0.08,
) -> list:
    """Traces for a 3D coordinate frame (3 unit vectors) at `base`."""
    b = np.asarray(np.zeros(3) if base is None else base, dtype=float).ravel()
    traces = []
    for axis, color in zip(np.eye(3) * scale, colors):
        traces += make_vector_traces(
            axis, base=b, color=color,
            line_width=line_width, cone_scale=cone_scale,
        )
    return traces


def add_point(fig: go.Figure, point, **kwargs) -> go.Figure:
    fig.add_trace(make_point_trace(point, **kwargs))
    return fig


def add_vector(fig: go.Figure, vector, base=None, **kwargs) -> go.Figure:
    for tr in make_vector_traces(vector, base, **kwargs):
        fig.add_trace(tr)
    return fig


def add_curve(fig: go.Figure, points, **kwargs) -> go.Figure:
    fig.add_trace(make_curve_trace(points, **kwargs))
    return fig


DEFAULT_BUTTON_STYLE = dict(
    bgcolor="#2a2a2a",
    bordercolor="#666",
    borderwidth=1,
    font=dict(color="white", size=13),
    pad=dict(l=6, r=6, t=4, b=4),
)


def _pi_fraction_label(numerator: int, denominator: int) -> str:
    from math import gcd
    g = gcd(numerator, denominator)
    n, d = numerator // g, denominator // g
    if n == 0:
        return "0"
    num = "" if n == 1 else f"{n}"
    den = "" if d == 1 else f"/{d}"
    return f"{num}π{den}"


def pi_slider_steps(n_frames: int, label_every: int = 6, t_units_per_frame_pi: tuple = (1, 24)):
    """
    Slider steps with π-fraction labels. Default: t = i * π/24 (so n_frames=48 covers [0, 2π)).
    `t_units_per_frame_pi = (num, den)` means each frame advances t by num*π/den.
    """
    num, den = t_units_per_frame_pi
    return [
        dict(
            method="animate",
            label=(_pi_fraction_label(i * num, den) if i % label_every == 0 else ""),
            args=[[str(i)], dict(frame=dict(duration=0, redraw=True), mode="immediate")],
        )
        for i in range(n_frames)
    ]


def play_pause_buttons(frame_duration_ms: int = 80) -> list:
    return [
        dict(label=" ▶ ", method="animate",
             args=[None, dict(frame=dict(duration=frame_duration_ms, redraw=True),
                              fromcurrent=True, mode="immediate")]),
        dict(label=" ❚❚ ", method="animate",
             args=[[None], dict(frame=dict(duration=0, redraw=False), mode="immediate")]),
    ]


def case_visibility_buttons(cases, vis_for_case) -> list:
    """One button per case; clicking sets the visibility pattern returned by vis_for_case(case)."""
    return [
        dict(label=f" {case} ", method="restyle", args=[{"visible": vis_for_case(case)}])
        for case in cases
    ]


def traces_to_frame_data(traces) -> list:
    """Convert full Plotly traces to position-only frame-data dicts.

    Frame data omits properties like `visible` so per-trace visibility set via
    button restyle is preserved during animation.
    """
    out = []
    for tr in traces:
        if isinstance(tr, go.Scatter3d):
            out.append(dict(type="scatter3d", x=tr.x, y=tr.y, z=tr.z))
        elif isinstance(tr, go.Cone):
            out.append(dict(type="cone",
                            x=tr.x, y=tr.y, z=tr.z,
                            u=tr.u, v=tr.v, w=tr.w))
        elif isinstance(tr, go.Scatter):
            out.append(dict(type="scatter", x=tr.x, y=tr.y))
        else:
            out.append(tr)
    return out


def apply_animation_layout(
    fig: go.Figure,
    case_buttons: list,
    n_frames: int,
    *,
    height: int = 620,
    button_style: dict | None = None,
    slider_label_every: int = 6,
    t_units_per_frame_pi: tuple = (1, 24),
    frame_duration_ms: int = 80,
) -> go.Figure:
    """Apply standard widget layout: case buttons (top), play/pause (below), π-labeled slider (bottom)."""
    style = button_style if button_style is not None else DEFAULT_BUTTON_STYLE
    fig.update_layout(
        height=height,
        updatemenus=[
            dict(type="buttons", buttons=case_buttons, direction="right",
                 active=0, showactive=True,
                 x=0.0, y=1.18, xanchor="left", yanchor="bottom",
                 **style),
            dict(type="buttons", buttons=play_pause_buttons(frame_duration_ms),
                 direction="right", showactive=False,
                 x=0.0, y=1.04, xanchor="left", yanchor="bottom",
                 **style),
        ],
        sliders=[dict(
            steps=pi_slider_steps(n_frames, label_every=slider_label_every,
                                  t_units_per_frame_pi=t_units_per_frame_pi),
            active=0,
            currentvalue=dict(prefix="t = ", font=dict(size=14, color="white"),
                              xanchor="left"),
            bgcolor="#444", bordercolor="#666",
            font=dict(color="#ddd", size=12),
            tickcolor="#888",
            pad=dict(b=10, t=30), len=0.92, x=0.04, y=0,
        )],
        margin=dict(l=10, r=10, t=110, b=20),
    )
    return fig


def fig_2d(
    xlim=(-1, 1),
    ylim=(-1, 1),
    axis_labels=("x", "y"),
    bgcolor="dimgrey",
    zerolinecolor="red",
):
    ax = {
        "backgroundcolor": bgcolor,
        "gridcolor": "darkgrey",
        "zerolinecolor": zerolinecolor,
        "showbackground": True,
    }
    fig = go.Figure()
    fig.update_layout(
        template="plotly_dark",
        scene={
            "xaxis": {**ax, "title": axis_labels[0], "range": list(xlim)},
            "yaxis": {**ax, "title": axis_labels[1], "range": list(ylim)},
        },
    )
    return fig
