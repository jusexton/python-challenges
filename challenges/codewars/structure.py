def same_structure_as(original, other) -> bool:
    if isinstance(original, list) and isinstance(other, list):
        return len(original) == len(other) and all(
            map(same_structure_as, original, other)
        )
    else:
        return not isinstance(original, list) and not isinstance(other, list)


# First working attempt:
# def same_structure_as(original, other) -> bool:
#     original_is_list, other_is_list = __is_list(original, other)
#     if original_is_list and other_is_list:
#         if len(original) != len(other):
#             return False
#
#         return all(same_structure_as(value[0], value[1]) for value in zip(original, other))
#     elif original_is_list ^ other_is_list:
#         return False
#
#     return True
#
#
# def __is_list(*values) -> tuple:
#     return tuple([type(value) is list for value in values])
