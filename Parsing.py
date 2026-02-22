from pydantic import BaseModel, Field, model_validator


class Parsing(BaseModel):
    width: int = Field(
        ge=10, description="width conf should be greater than 10"
        )
    height: int = Field(
        ge=10, description="height conf should be greater than 10"
    )
    entry: tuple = Field(
        description="enty should be valid cordinates (x,y)"
    )
    exit: tuple = Field(
        description="exit should be valid cordinates (x,y)"
    )
    output_file: str = Field(
        max_length=10,
        description="output file should be of type string with max length 10"
    )
    perfect: bool = Field(
        description="perfect argument should be valid boolian (True or False)"
    )

    @staticmethod
    def get_conf(data: str) -> dict:
        conf: dict = {}
        filtered: list = data.split('\n')
        for ele in filtered:
            key: str = ele.strip().split('=')[0].lower()
            val: str = ele.strip().split('=')[1]
            conf[key] = val
        return conf

    @staticmethod
    def valid_numbers(n: str) -> int:
        for el in n:
            if el not in '0123456789':
                return False
        return True

    @staticmethod
    def to_int(data: tuple) -> tuple:
        return (int(data[0]), int(data[1]))

    @model_validator(mode='after')
    def finishing(s) -> 'Parsing':
        s.entry = s.to_int(s.entry)
        s.exit = s.to_int(s.exit)
        return s

    @model_validator(mode='before')
    @staticmethod
    def preparation(data: dict) -> dict:
        if 'width' not in data:
            raise ValueError("there is no width on configuration file")
        elif 'height' not in data:
            raise ValueError("there is no height on configuration file")
        if not Parsing.valid_numbers(data['width']):
            raise ValueError("width value not a valid number")
        elif not Parsing.valid_numbers(data['height']):
            raise ValueError("height value not a valid number")
        if 'entry' not in data:
            raise ValueError("no entry provided on configuration file")
        elif 'exit' not in data:
            raise ValueError("no entry provided on configuration file")

        data['width'] = int(data['width'])
        data['height'] = int(data['height'])
        data['entry'] = tuple(data['entry'].strip().split(','))
        data['exit'] = tuple(data['exit'].strip().split(','))
        if len(data['entry']) != 2:
            raise ValueError("the provided enty not valid")
        for ele in data['entry']:
            if not Parsing.valid_numbers(ele):
                raise ValueError("the provided enty not valid")
        for ele in data['exit']:
            if not Parsing.valid_numbers(ele):
                raise ValueError("the provided enty not valid")
        if len(data['exit']) != 2:
            raise ValueError("the provided exit not valid")
        if 'perfect' not in data:
            raise ValueError("perfect filed is required")
        return data
