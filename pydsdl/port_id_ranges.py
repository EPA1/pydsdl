#
# Copyright (C) 2018  UAVCAN Development Team  <uavcan.org>
# This software is distributed under the terms of the MIT License.
#

_STANDARD_ROOT_NAMESPACE = 'uavcan'

_STANDARD_MESSAGES = 62804, 65535
_VENDOR_MESSAGES   = 57344, 59391

_STANDARD_SERVICES = 384, 511
_VENDOR_SERVICES   = 256, 319


def is_valid_regulated_subject_id(regulated_id: int,
                                  root_namespace: str) -> bool:
    is_standard = root_namespace.strip() == _STANDARD_ROOT_NAMESPACE
    applicable_range = _STANDARD_MESSAGES if is_standard else _VENDOR_MESSAGES
    return applicable_range[0] <= int(regulated_id) <= applicable_range[1]


def is_valid_regulated_service_id(regulated_id: int,
                                  root_namespace: str) -> bool:
    is_standard = root_namespace.strip() == _STANDARD_ROOT_NAMESPACE
    applicable_range = _STANDARD_SERVICES if is_standard else _VENDOR_SERVICES
    return applicable_range[0] <= int(regulated_id) <= applicable_range[1]


def _unittest_pid_ranges() -> None:
    assert is_valid_regulated_subject_id(regulated_id=58000, root_namespace='sirius_cybernetics_corp')
    assert not is_valid_regulated_subject_id(regulated_id=58000, root_namespace='uavcan')
    assert is_valid_regulated_subject_id(regulated_id=64000, root_namespace='uavcan')
    assert not is_valid_regulated_subject_id(regulated_id=64000, root_namespace='sirius_cybernetics_corp')
    assert not is_valid_regulated_subject_id(regulated_id=30000, root_namespace='uavcan')
    assert not is_valid_regulated_subject_id(regulated_id=30000, root_namespace='sirius_cybernetics_corp')

    assert is_valid_regulated_service_id(regulated_id=260, root_namespace='sirius_cybernetics_corp')
    assert not is_valid_regulated_service_id(regulated_id=260, root_namespace='uavcan')
    assert is_valid_regulated_service_id(regulated_id=400, root_namespace='uavcan')
    assert not is_valid_regulated_service_id(regulated_id=400, root_namespace='sirius_cybernetics_corp')
    assert not is_valid_regulated_service_id(regulated_id=600, root_namespace='uavcan')
    assert not is_valid_regulated_service_id(regulated_id=600, root_namespace='sirius_cybernetics_corp')
