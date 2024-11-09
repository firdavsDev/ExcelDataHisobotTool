from .pyg import get_pyg_renderer
from .utils.load_data import change_column_type, load_data
from .utils.my_logger import log_function, set_up_logger

logger = set_up_logger()


@log_function(logger)
def analyze_data(uploaded_file, uploaded_spec=None):
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
    dfs = load_data(uploaded_file)
    # TODO date format column(Дата выдачи) type
    dfs = change_column_type("Дата выдачи", "datetime", dfs)
    # Check if uploaded_spec is not None
    if uploaded_spec is not None:
        print(uploaded_spec)
        # Create a renderer
        renderer = get_pyg_renderer(dfs, spec=uploaded_spec)
    else:
        # Create a renderer
        renderer = get_pyg_renderer(dfs)
    # Create a renderer
    return renderer
