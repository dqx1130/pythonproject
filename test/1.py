from enigma.machine import EnigmaMachine

# 将此函数用于爆破Enigma设置
def brute_force_enigma(known_plaintext, known_ciphertext):
    rotors = ['I', 'II', 'III', 'IV', 'V']
    reflectors = ['B', 'C']
    possible_plugboard_settings = [
        '', 'AB CD', 'EF GH', 'IJ KL', 'MN OP', 'QR ST', 'UV WX', 'YZ',
        'AB EF', 'CD IJ', 'GH KL', 'MN OP', 'QR ST', 'UV WX', 'YZ'
    ]

    # 尝试所有转子和反射器组合
    for rotor1 in rotors:
        for rotor2 in rotors:
            for rotor3 in rotors:
                if rotor1 != rotor2 and rotor2 != rotor3 and rotor1 != rotor3:
                    for reflector in reflectors:
                        for plugs in possible_plugboard_settings:
                            # 创建Enigma机实例
                            machine = EnigmaMachine.from_key_sheet(
                                rotors=f'{rotor1} {rotor2} {rotor3}',
                                reflector=reflector,
                                plugboard_settings=plugs
                            )

                            # 设置转子的起始位置
                            for setting in range(26*26*26):
                                setting_str = f"{chr(65 + (setting // 676) % 26)}{chr(65 + (setting // 26) % 26)}{chr(65 + setting % 26)}"
                                machine.set_display(setting_str)

                                # 加密已知明文并比较结果
                                encrypted_text = machine.process_text(known_plaintext)
                                if encrypted_text == known_ciphertext:
                                    print(f'Found working configuration: Rotors {rotor1} {rotor2} {rotor3} with Reflector {reflector} and Plugs {plugs} at Setting {setting_str}')
                                    return rotor1, rotor2, rotor3, reflector, plugs, setting_str

# 使用示例
known_plaintext = 'ftye'
known_ciphertext = 'nicc'
result = brute_force_enigma(known_plaintext, known_ciphertext)
if result:
    print("Configuration found:", result)
else:
    print("No valid Enigma configuration found.")
