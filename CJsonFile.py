import json
import io


class JsonFile:

    def __init__(self, _json_file_name):
        self.file_name = _json_file_name

    def json_img_txt_details_conversion(self, _file_quantity, _current_number, _current_dir):
        percent = (_current_number / _file_quantity) * 100  # percent calc
        # Define data
        data = {'%': percent,
                'range': _file_quantity,
                'current': _current_number,
                'link': _current_dir}
        # Write JSON file
        with io.open(self.file_name + '.json', 'w', encoding='utf8') as outfile:
            str_ = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
            outfile.write(str_)