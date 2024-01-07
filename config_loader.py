import yaml


# 读取yml内容，并导出
def loader_config():
    with open("./project.yml", "r", encoding="utf8") as f:
        return yaml.load(f.read(), Loader=yaml.Loader)

    # config = config_data
    # input_file, input_path, background_music, output_file, output_type, ouput_path = (
    #     config.input.file_name,
    #     config.input.save_path,
    #     config.background_music,
    #     config.out.name,
    #     config.out.file_type,
    #     config.out.save_path,
    # )
