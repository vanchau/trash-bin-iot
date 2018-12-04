# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: touchtag.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='touchtag.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0etouchtag.proto\"M\n\ndebug_data\x12\x15\n\rupdate_period\x18\x01 \x01(\r\x12\x13\n\x0b\x64\x65\x62ug_var_1\x18\x02 \x01(\r\x12\x13\n\x0b\x64\x65\x62ug_var_2\x18\x03 \x01(\r\"\xb0\x01\n\x06sample\x12\x16\n\x0e\x63onfig_version\x18\x01 \x02(\r\x12\x13\n\x0btemperature\x18\x02 \x02(\x11\x12\x12\n\nfw_version\x18\x03 \x02(\r\x12\x14\n\x0ctrigger_code\x18\x04 \x01(\r\x12\x17\n\x0ftrigger_counter\x18\x05 \x01(\r\x12\r\n\x05pitch\x18\x06 \x01(\x11\x12\x0c\n\x04roll\x18\x07 \x01(\x11\x12\x19\n\x04\x64\x61ta\x18\x08 \x01(\x0b\x32\x0b.debug_data\"S\n\rtrigger_setup\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x10\n\x08option_1\x18\x02 \x01(\r\x12\x10\n\x08option_2\x18\x03 \x01(\r\x12\x10\n\x08option_3\x18\x04 \x01(\r\"\x89\x01\n\nset_config\x12\x16\n\x0e\x63onfig_version\x18\x01 \x02(\r\x12\x11\n\ttimestamp\x18\x02 \x02(\r\x12\x1c\n\x14\x64\x65vice_update_period\x18\x03 \x01(\r\x12\x10\n\x08\x64\x61tarate\x18\x04 \x01(\r\x12 \n\x08settings\x18\x08 \x03(\x0b\x32\x0e.trigger_setup\"\x10\n\x0eget_debug_dataB\x02H\x02')
)




_DEBUG_DATA = _descriptor.Descriptor(
  name='debug_data',
  full_name='debug_data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_period', full_name='debug_data.update_period', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debug_var_1', full_name='debug_data.debug_var_1', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debug_var_2', full_name='debug_data.debug_var_2', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=95,
)


_SAMPLE = _descriptor.Descriptor(
  name='sample',
  full_name='sample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config_version', full_name='sample.config_version', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='sample.temperature', index=1,
      number=2, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fw_version', full_name='sample.fw_version', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trigger_code', full_name='sample.trigger_code', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trigger_counter', full_name='sample.trigger_counter', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='sample.pitch', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roll', full_name='sample.roll', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='sample.data', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=274,
)


_TRIGGER_SETUP = _descriptor.Descriptor(
  name='trigger_setup',
  full_name='trigger_setup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='trigger_setup.code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='option_1', full_name='trigger_setup.option_1', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='option_2', full_name='trigger_setup.option_2', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='option_3', full_name='trigger_setup.option_3', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=359,
)


_SET_CONFIG = _descriptor.Descriptor(
  name='set_config',
  full_name='set_config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config_version', full_name='set_config.config_version', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='set_config.timestamp', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_update_period', full_name='set_config.device_update_period', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datarate', full_name='set_config.datarate', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='settings', full_name='set_config.settings', index=4,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=499,
)


_GET_DEBUG_DATA = _descriptor.Descriptor(
  name='get_debug_data',
  full_name='get_debug_data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=517,
)

_SAMPLE.fields_by_name['data'].message_type = _DEBUG_DATA
_SET_CONFIG.fields_by_name['settings'].message_type = _TRIGGER_SETUP
DESCRIPTOR.message_types_by_name['debug_data'] = _DEBUG_DATA
DESCRIPTOR.message_types_by_name['sample'] = _SAMPLE
DESCRIPTOR.message_types_by_name['trigger_setup'] = _TRIGGER_SETUP
DESCRIPTOR.message_types_by_name['set_config'] = _SET_CONFIG
DESCRIPTOR.message_types_by_name['get_debug_data'] = _GET_DEBUG_DATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

debug_data = _reflection.GeneratedProtocolMessageType('debug_data', (_message.Message,), dict(
  DESCRIPTOR = _DEBUG_DATA,
  __module__ = 'touchtag_pb2'
  # @@protoc_insertion_point(class_scope:debug_data)
  ))
_sym_db.RegisterMessage(debug_data)

sample = _reflection.GeneratedProtocolMessageType('sample', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLE,
  __module__ = 'touchtag_pb2'
  # @@protoc_insertion_point(class_scope:sample)
  ))
_sym_db.RegisterMessage(sample)

trigger_setup = _reflection.GeneratedProtocolMessageType('trigger_setup', (_message.Message,), dict(
  DESCRIPTOR = _TRIGGER_SETUP,
  __module__ = 'touchtag_pb2'
  # @@protoc_insertion_point(class_scope:trigger_setup)
  ))
_sym_db.RegisterMessage(trigger_setup)

set_config = _reflection.GeneratedProtocolMessageType('set_config', (_message.Message,), dict(
  DESCRIPTOR = _SET_CONFIG,
  __module__ = 'touchtag_pb2'
  # @@protoc_insertion_point(class_scope:set_config)
  ))
_sym_db.RegisterMessage(set_config)

get_debug_data = _reflection.GeneratedProtocolMessageType('get_debug_data', (_message.Message,), dict(
  DESCRIPTOR = _GET_DEBUG_DATA,
  __module__ = 'touchtag_pb2'
  # @@protoc_insertion_point(class_scope:get_debug_data)
  ))
_sym_db.RegisterMessage(get_debug_data)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\002'))
# @@protoc_insertion_point(module_scope)
