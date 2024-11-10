from .pyg import get_pyg_renderer
from .utils.my_logger import log_function, set_up_logger

logger = set_up_logger()


@log_function(logger)
def analyze_data(dfs, uploaded_spec=None):
    """
    Analyze data from uploaded file and spec.

    Parameters
    ----------
    uploaded_file : Union[BytesIO, str]
        The uploaded file.
    uploaded_spec : Union[None, str], optional
        The uploaded spec, by default None.

    Returns
    -------
    pygexplorer.renderer.Renderer
        The renderer for the data.
    """
    # Load data
    # dfs = change_column_type("Дата выдачи", "datetime", dfs)
    # dfs = change_column_type("ДАТА ВЫДАЧИ", "datetime", dfs)
    # Check if uploaded_spec is not None
    if uploaded_spec is not None:
        # Create a renderer
        renderer = get_pyg_renderer(dfs, spec=uploaded_spec)
    else:
        # Create a renderer
        renderer = get_pyg_renderer(dfs)
    # Create a renderer
    return renderer
