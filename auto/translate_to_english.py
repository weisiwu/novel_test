def translate_to_english():
    pass


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from config_loader import loader_config

    config = loader_config()
    print(config)
    translate_to_english()
