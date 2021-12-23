import os
import base64
import json
import random
from project.cipher import Cipher
from string import Template, ascii_letters, digits


def encrypt_connection(key_security_token: str, decrypted: dict) -> str:
    iv = os.urandom(16) + os.urandom(8)
    key = base64.b64decode(key_security_token)
    ciphertext_hex: str = Cipher.aes_encrypt_to_hex(
        json.dumps(decrypted).encode('utf-8'), iv, key)
    return base64.b64encode(json.dumps({
        "ciphertext": ciphertext_hex,
        "iv": iv.hex(),
    }).encode()).decode()


def make_id(length):
    letters_and_digits = ascii_letters + digits
    result_str = ''.join((random.choice(letters_and_digits) for _ in range(length)))
    return result_str


def make_vott_file(logger, config, file_name, vott_path, vott_input_path):

    template = config.get_config( 'VOTT', 'template')
    if template is None:
        return False

    security_token_name = config.get_config('VOTT', 'security_token_name')
    if security_token_name is None:
        return False

    security_token_key = config.get_config('VOTT', 'security_token_key')
    if security_token_key is None:
        return False

    vott_outpt_path = vott_path + '/output/'
    os.makedirs(vott_outpt_path)

    encrypt_data = {'folderPath': vott_input_path}
    logger.info(f'>> vott input dict : {encrypt_data}')
    enc_input_path = encrypt_connection(security_token_key, encrypt_data)

    encrypt_data = {'folderPath': vott_outpt_path}
    logger.info(f'>> vott output dict : {encrypt_data}')
    enc_output_path = encrypt_connection(security_token_key, encrypt_data)

    format_encrypted = {'assetState': 'visited', 'includeImages': True}
    logger.info(f'>> vott format dict : {format_encrypted}')
    enc_format_encrypted = encrypt_connection(security_token_key, format_encrypted)

    with open(template, 'r') as r:
        cfg_template = r.read()
    t = Template(cfg_template)
    new_cfg = t.substitute(project_name=file_name,
                           security_token=security_token_name,
                           input_connection=f'{file_name}_input',
                           input_encrypted=enc_input_path,
                           input_id=make_id(9),
                           output_connection=f'{file_name}_output',
                           output_encrypted=enc_output_path,
                           format_encrypted=enc_format_encrypted,
                           output_id=make_id(9),
                           format_id=make_id(9)
                           )

    logger.info(f'>> make vott file : {vott_outpt_path}{file_name}.vott')
    with open(f'{vott_outpt_path}{file_name}.vott', 'w') as w:
        w.write(new_cfg)
    return True
