class CustomSesionState:
    def __init__(self, st):
        self.session_state = st.session_state

    # get item from session state
    def get(self, key):
        return self.session_state.get(key)

    # set item in session state
    def set(self, key, value):
        self.session_state[key] = value
        return self.session_state[key]

    # remove item from session state
    def remove(self, key):
        if key in self.session_state:
            del self.session_state[key]
        else:
            raise KeyError(f"{key} not in session state")

    # clear session state
    def clear(self):
        self.session_state.clear()

    # get all items in session state
    def items(self):
        return self.session_state.items()

    # update session state
    def update(self, **kwargs):
        self.session_state.update(kwargs)
