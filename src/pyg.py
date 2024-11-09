import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer


@st.cache_resource
def get_pyg_renderer(dfs, spec=""):
    """
    Get the PygRenderer.

    Parameters
    ----------
    dfs : Dict[str, pd.DataFrame]
        The dataframes.
    spec : Union[None, str], optional
        The spec, by default None.

    Returns
    -------
    pygexplorer.renderer.Renderer
        The renderer.
    """
    return StreamlitRenderer(dfs, spec=spec)
