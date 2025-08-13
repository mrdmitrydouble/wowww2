def safe_execute(fn, *args, **kwargs):
    """Execute a function and catch exceptions."""
    try:
        return fn(*args, **kwargs)
    except Exception as exc:
        print(f"Guardrail caught exception: {exc}")
        return None
