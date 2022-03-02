# Copyright 2022 Cadwork Informatique Inc.
# All rights reserved.
# This file is part of ProdDifferentiator,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import attribute_controller, element_controller, menu_controller, utility_controller

selected_user_attribute = utility_controller.get_user_int('Which user attribute number should be used?')

active_elements = element_controller.get_active_identifiable_element_ids()

production_number_map = {}

for element in active_elements:
    current_production_number = attribute_controller.get_production_number(element)

    if current_production_number > 0:
        if current_production_number in production_number_map.keys():
            production_number_map[current_production_number].append(element)
        else:
            production_number_map[current_production_number] = []
            production_number_map[current_production_number].append(element)

for production_number in production_number_map:
    incrementation_number = 1
    for element in production_number_map[production_number]:
        attribute_controller.set_user_attribute([element], selected_user_attribute, str(incrementation_number))
        incrementation_number += 1
